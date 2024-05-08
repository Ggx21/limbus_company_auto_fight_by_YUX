import pyautogui
import keyboard
import time
import winsound
import logging

# 配置日志到控制台和文件
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('log/auto_fight.log')  # 日志文件名
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(file_handler)

template_path = 'img/start.png'  # 模板图片的路径
p_key = 'p'
enter_key = 'enter'
timeout = 10  # 超时时间，单位秒
confidence = 0.9  # 模糊匹配的置信度
start_time = time.time()

# 定义继续键
continue_key = 'c'

# 设置超时监听的按键，这里以 'esc' 为例
keyboard.add_hotkey('esc', lambda: wait_for_continue_key(), suppress=True)

def play_beep():
    winsound.Beep(1200, 1000)

def play_confirm_beep():

    winsound.Beep(800, 100)
    # beep twice
    time.sleep(0.25)
    winsound.Beep(800, 100)



def log_status(message):
    # 记录状态信息
    logging.info(message)

def wait_for_continue_key():
    # 等待用户按下继续键
    log_status("Waiting for continue key ('%s')..." % continue_key)
    play_beep()
    timeout_threshold = 10  # 超时阈值
    wait_start_time = time.time()
    while not keyboard.is_pressed(continue_key):
        time.sleep(0.1)
        if time.time() - wait_start_time > timeout_threshold:
            play_beep()
            wait_start_time = time.time()
            timeout_threshold *= 2
    log_status("Continue key pressed. Resuming operation.")
    play_confirm_beep()


try:
    retry_count=0
    while True:
        if not keyboard.is_pressed('esc'):
            try:
                # 尝试在屏幕上进行模糊匹配
                pos = pyautogui.locateOnScreen(template_path, confidence=confidence, grayscale=True)
            except pyautogui.ImageNotFoundException:
                # 继续循环前等待用户输入
                if(retry_count<60):
                    time.sleep(1)
                    retry_count+=1
                    continue
                log_status("Operation timed out after 60 retries not found target.")
                wait_for_continue_key()
                retry_count=0
                continue  # 继续下一次循环
            else:
                # 成功匹配到模板，模拟点击事件
                pyautogui.click(pos)
                pyautogui.press(p_key)
                time.sleep(0.5)
                pyautogui.press(enter_key)
                time.sleep(3)
                log_status("Template found and clicked.")
                retry_count=0
                start_time = time.time()  # 重新计时
        else:
            wait_for_continue_key()
            start_time = time.time()
            retry_count=0

except KeyboardInterrupt:
    # 处理 Ctrl + C 中断
    log_status("Program interrupted by user.")
    play_beep()

# 退出程序
log_status("Program exited.")