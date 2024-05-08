# **limbus_company_auto_fight_by_YUX**

**limbus_company_auto_fight_by_YUX** is an automation tool designed to simulate user combat operations within no more than a **single combat** in game `limbus_company`. It utilizes the `pyautogui`, `keyboard`, `time`, `winsound`, and `logging` libraries to perform automated tasks.

> caution :  If you are not familiar with Python and command-line operations, please use the `.exe` file provided in the release section of this repository directly.

### warning

- you should always run the script or the .exe file in **administrator mode**
- don't edit the file in the released zipped file.

## Environment Setup

Before running the script, ensure that all required libraries are installed in your Python environment. We recommend managing your environment with Conda. Here are the steps to set up the environment:

1. Install Anaconda or Miniconda if you haven't already.
2. Clone this repository or download the `environment.yml` file.
3. Navigate to the directory containing the `environment.yml` file via the command line.
4. Run the following command to create a new Conda environment and install dependencies:

   conda env create -f environment.yml

5. Activate the environment:

   conda activate auto_fight_env

## Running the Script

After activating the corresponding Conda environment, you can run the script with the following command:

```bash
python auto_fight.py
```

## Usage & Functionality

- The script will continuously attempt to find the specified template image on the screen and simulate a click when found.
- If the template image is not found within the specified timeout period, the script will wait for the user to press the continue key (default is the 'c' key).
- Users can interrupt the script's operation by pressing the ESC key.
- After combat and after the specified timeout period, the script will beep you to inform you to continue.

## Logging

The script records operational status in both the console and a log file named `auto_fight.log`.

## Precautions

- Ensure that your game window is active and the template image is visible on the screen before running the script.
- Do not move the mouse or cover the game window during script execution to avoid disrupting the script.
- Using this script for game automation may violate the game's terms of service. Ensure you are aware of the associated risks.

## Exiting the Script

You can safely interrupt the script's execution by pressing Ctrl + C.

## Technical Support

If you encounter any issues while using the script, you can contact us through the following means:

- Submit an issue to this repository
- Email me at ggxthu21@gmail.com

Enjoy using the script!