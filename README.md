# WeMos ESP-WROOM-32

![alt text](https://bitbucket.org/johanels/micropython-wemos-esp32/raw/77df2291d4584294f77e2a3015ac02abe2635310/images/wemos-esp32_com_oled-pinout.png)


## Requirements:
Python 2.7 ( https://www.python.org/ )

CP210x USB to UART Bridge VCP Drivers ( https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers )

MicroPython ( https://micropython.org/ ) and firmware download ( http://micropython.org/download#esp32 )

Python PIP ( https://packaging.python.org/tutorials/installing-packages/ )

Atom IDE ( https://atom.io/ )

Pymakr Atom Package ( https://atom.io/packages/pymakr )

Flash MicroPython using MacOS and Python:
```bash
ls /dev/tty*
pip install esptool
python -m esptool --port /dev/tty.SLAB_USBtoUART erase_flash
python -m esptool --port /dev/tty.SLAB_USBtoUART write_flash --flash_mode dio --flash_size=detect 0x1000 esp32-20180511-v1.9.4.bin
```

Flash MicroPython using Windows and Python:
```cmd
python -m ensurepip --default-pip
python -m pip install --upgrade pip setuptools wheel
"c:\Program Files (x86)\Python\Scripts\pip.exe" install esptool
python -m esptool --port COM3 erase_flash
python -m esptool --port COM3 write_flash --flash_mode dio --flash_size=detect 0x1000 esp32-20180511-v1.9.4.bin
```

## Project folder layout
 * build -> local build folder for files transferred to ESP32
 * images -> images
 * lib -> local libraries folder for submodules
 * tests -> testing and tooling
 * .gitignore
 * .gitmodules
 * README.md
 * boot.py
 * main.py
 * makefile
 * pymakr.conf

## WebREPL
REPL ( Read Evaluate Print Loop ) is available in the ATOM IDE over USB or over the WiFi connection using http://micropython.org/webrepl/ ( GIT source https://github.com/micropython/webrepl ).For access over WiFi you have to configure the WebREPL server over USB
```Python
import webrepl.setup
```

## GIT add submodules
Add any submodules into the lib folder which is excluded from GIT version control.
```bash
git submodule add {GIT URL} lib/{NAME}
```
Download any submodules after project clone
```bash
git submodule update --init --recursive
```
Update any submodules from remote
```bash
git submodule update --recursive --remote
```

## makefile usage
The makefile takes care of including submodules into the files delivered onto the device. The files in the build folder is what is loaded onto the device when pressing the "Upload" button in the IDE. Currently the makefile is only build for MacOS.
