# Process Pipeline Simulator
## _A simple educational tool for visualizing a CPU process pipeline diagram_

![Binary knowledge](https://i.imgur.com/zyBDTiC.jpg)

This desktop application allows the user to create their own fictional instructions with two basic parameters setting their name and time units required for execution. With this information and an additional input of a time limit, the application will create a pipeline diagram showing the order of execution for the instructions such that they will avoid overlapping.

For the purpuses of the educational simulation, we'll establish two different methods of execution, showing different approaches that could be taken when building a relatively simple yet optimized pipeline of operations.

The application features two possible input methods, manual and file:

_Welcome screen_
![Application welcome screen](https://i.imgur.com/Ay4CGps.png)

The manual method allows for more granular inputs, perfect for someone who's trying to play with a smaller set of:

_Manual input screen_
![Application manual input screen](https://i.imgur.com/atdlEZW.png)

Meanwhile the file method allows more flexibility and quicker iteration when testing:

_File input screen_

![Application file input screen](https://i.imgur.com/eXuq6pW.png)

![Application file input screen](https://i.imgur.com/tALrxF6.png)

Ultimately the input method is up to the user, what really matters are the results, here are two example outputs using the different approaches for building the pipeline with the same inputs:

_Simple logic_
![Application simple logic log example](https://i.imgur.com/9BGFasN.png)
_No overlap logic_
![Application no overlap logic log example](https://i.imgur.com/vxLuChN.png)


## Usage

- Run the application and choose the desired input method in the welcome screen

**Manual**
  * Insert the number of instructions desired.
  * Click the "continue" button below.
  * Define each instruction with a name and execution time.
  * Click the "continue" button below.
  * Insert the total execution time.
  * Click the "allow overlap" button to switch between the two pipeline generation logic modes.
  * Click the "generate pipeline" button below.
  * Enjoy the results!

**File**
  * Paste in a valid regular grammar in the text field.
  * Input formatting goes as follows: 
      * [INSTRUCTION NAME],[EXECUTION TIME]
      * ...
      * [INSTRUCTION NAME],[EXECUTION TIME]
      * [TOTAL TIME]
      * Where the first N lines contain instruction names and their execution time separated by a comma symbol.
      * Where the final line contains the total execution time.
  * Click the "allow overlap" button to switch between the two pipeline generation logic modes.
  * Click the "generate pipeline" button below.
  * Enjoy the results!

**Miscellaneous**
  * The back button in either screen will return to the welcome screen.
  * The reset button in either screen will return that screen to its initial state.


## Packages used

This educational application was only made possible because of these amazing packages.

| Package | Link |
| ------ | ------ |
| PyQt6 | https://pypi.org/project/PyQt6/ |
| PyInstaller | https://pypi.org/project/pyinstaller/ |

## Building the application

If you want to build the application yourself from the source code:

**Windows**
1. Download Python from https://www.python.org/downloads/ and install it
2. Open a terminal and run this command to install the dependencies:
```sh
pip install PyQt6 PyInstaller
```
3. Navigate to the source code's directory and run this command to build the application:
```sh
pyInstaller main_window.py --onefile --noconsole --icon=logo.ico --add-data "resources;resources"
```
4. Run the newly created .exe in the "dist" folder

**Linux**
1. Download and install Python using the package manager from your distro:
* Ubuntu/Debian
```sh
sudo apt install python3
```
* Fedora
```sh
sudo dnf install python3
```
* CentOS/RHEL
```sh
sudo yum install centos-release-scl
sudo yum install rh-python36
scl enable rh-python36 bash
```
* Arch
```sh
sudo pacman -S python
```
2. Download and install the Package Installer for Python (pip):
```sh
python3 get-pip.py
```
3. Download and install the dependencies:
```sh
sudo pip3 install pyinstaller pyqt6
```
4. Navigate to the source code's directory and run this command to build the application:
```sh
python3 -m PyInstaller main_window.py --onefile --noconsole --icon=logo.ico --add-data "resources:resources"
```
5. Navigate to the newly created "dist" folder
6. Run this command on the main_window binary file to grant it permission to execute
```sh
chmod +x main_window
```
7. Run the application with this command:
```sh
./main_window
```

## Compatibility

This application currently runs on Windows 10 and Linux. I am looking into the possibility of adding a macOS release but I won't make any promises.

## Future development

This application does have a few possibilities for additional features which may include:

- Different pipeline generation strategies.
- Saving manual inputs as .txt files that can be loaded later.
