# Sample IoT Project

The goal of this project is to upload temperature data to a local server and store the data on said server. The server may be held on a Raspberry Pi (which should also act as the access point for the board). The board should be able to automatically water the plants and display any diagnostics on its mini screen. 

The current steps in this projects are the following:
- [x] Design the board (completed)
- [ ] Establish the build-environment
- [ ] Code the display
- [ ] Code the DHT Sensor
- [ ] Code the soil moister (tentative)
- [ ] Code the Wifi Module to send data
- [ ] Code the server to accept and ack the data
- Others

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
sudo apt-get install build-essential
sudo apt-get install git
```

After those commands, copy and paste this code in the terminal and run it as well.
```bash
sudo apt-get install git autoconf build-essential gperf bison flex texinfo libtool libncurses5-dev wget gawk libc6-dev-amd64 python-serial libexpat-dev
```

Lastly, install whatever IDE you find comfortable. Look this up yourself, or follow the instruction for VS Code on Linux

- Install VS Code for Linux [https://code.visualstudio.com/docs/?dv=linux64_deb](here)
- Download the Following extensions for VS Code:
    - C/C++
    - Arduino
    - Python
    - GitLens (optional if you're familiar with Git)
    - PlatformIO (still testing, so optional)

### ESP8266/ESP32 Build Environment

To get started, the Arduino IDE is required for library setup and installation. **Despite downloading the IDE, you are free to use whatever IDE or text editor you wish. VS Code, Sublime Text, or vim is fine.** Download the Arduino IDE and follow [https://github.com/esp8266/Arduino/blob/master/README.md](the instructions depicting "Installing with Boards Manager").

Next, follow the instructions [https://github.com/plerup/makeEspArduino](here) in order to setup the makefile environment. Scroll down to **installing**. To make the call to the makefile easier, make an alias by typing the following line in terminal:

```bash
alias espmake="make -f ~/makeEspArduino/makeEspArduino.mk"
```
Again, note that the installed makefile should be in the correct path as the command above.

### Python Build Environment

> Will come in the future.