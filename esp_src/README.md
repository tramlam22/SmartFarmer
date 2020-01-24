# ESP ReadMe

## Board Design

> Information about board design will come soon

## Build Environment Setup
### Pre Setup
***Ubuntu 64-bit is preferred.*** This way, the environment is set constant with little variation between the group. A virtual machine is also acceptable with Ubuntu installed by using VMWare Workstation Player.

> Note: for MacOS users, VMWare is not available. Use VirtualBox as an option.

To get started, there are some things that should be taken care of before the build environment is created. Type the following code to get started with creating the build environment:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3
```

After those commands, copy and paste this code in the terminal and run it as well.
```bash
sudo apt-get install git autoconf build-essential gperf bison flex texinfo libtool libncurses5-dev wget gawk libc6-dev-amd64 python-serial libexpat-dev
```

Lastly, install whatever IDE you find comfortable. Look this up yourself, or follow the instruction for VS Code on Linux

- Install VS Code for Linux [https://code.visualstudio.com/docs/?dv=linux64_deb](here)
- Download the Following extensions for VS Code:
    - C/C++
    - Python
    - GitLens (optional if you're familiar with Git)
    - PlatformIO (still testing, so optional)

## ESP8266/ESP32 Build Environment

To get started, the Arduino IDE is required for library setup and installation. **Despite downloading the IDE, you are free to use whatever IDE or text editor you wish. VS Code, Sublime Text, or vim is fine.** Download the Arduino IDE and follow [the instructions depicting "Installing with Boards Manager"](https://github.com/esp8266/Arduino/blob/master/README.md).

Next, follow the instructions [https://github.com/plerup/makeEspArduino](here) in order to setup the makefile environment. Scroll down to **installing**. To make the call to the makefile easier, make an alias by typing the following line in terminal:

```bash
alias espmake="make -f ~/makeEspArduino/makeEspArduino.mk"
```
Again, note that the installed makefile should be in the correct path as the command above.

> Note: Within the esp_src directory, 
*THE config.mk FILE MUST REMAIN AND STAY IN THIS DIRECTORY. THIS FILE LINKS THE ARDUINO LIBRARIES TO THE PROJECT.*

> Note 2: If you are using VS Code, you can edit c_cpp_properties.json to your own content and link to libaries in order to avoid IDE conflicts.

The following Arduino Libraries are required:
```
- Adafruit_GFX_Library
- Adafruit_SSD1306 (for display)
- Adafruit Unified Sensor
- DHT sensor library
- Adafruit seesaw library
```

In order to build and flash the code, build the code using

```bash
$ alias espmake="make -f ~/makeEspArduino/makeEspArduino.mk"
```

From here, the following commands can be as followed:
```
In order to compile the code:
- espmake SKETCH=<insert the .ino filename here>

In order to flash the code to a specific board:
- UPLOAD_PORT=<insert /dev/ttyUSB# here>

To add build flags:
- BUILD_EXTRA_FLAGS=<insert flags>

Entire Build command:
- espmake flash SKETCH=<> UPLOAD_PORT=<> BUILD_EXTRA_FLAGS=<>

Possible Build Flags
-D_ENABLE_POST_DEBUG // to debug the post to an internal network
-D_ENABLE_WIFI_DEBUG // to enable wifi debug messages
-
```

Here is an example of what to type out to flash the board to ttyUSB0: 
```bash
$ espmake flash SKETCH=head_node.ino UPLOAD_PORT=/dev/ttyUSB0 BUILD_EXTRA_FLAGS="-D_POST_TEST -D_ESP8266"
```


Side Notes:
```
espmake SKETCH=posting_data.ino BUILD_EXTRA_FLAGS="-D_ENABLE_POST_DEBUG -D_ENABLE_WIFI_DEBUG"

```