# boot.py
# This file is executed on every boot (including wake-boot from deepsleep)

# Functions related to the ESP8266 - https://docs.micropython.org/en/latest/pyboard/library/esp.html
import esp
# Frame buffer manipulation - https://docs.micropython.org/en/latest/pyboard/library/framebuf.html
import framebuf
# Functions related to the hardware - https://docs.micropython.org/en/latest/pyboard/library/machine.html
import machine
# Network configuration - https://docs.micropython.org/en/latest/pyboard/library/network.html
import network
# Time related functions - https://docs.micropython.org/en/v1.5/pyboard/library/time.html
import time
# uasyncio
import modules.uasyncio as uasyncio
# pkg_resource
import modules.pkg_resources as pkg_resources

# WebREPL functions - https://micropython.org/webrepl/
# WebREPL client for MicroPython - https://github.com/micropython/webrepl
import webrepl

# Adafruit LCD screen
import modules.ssd1306 as ssd1306

# redirect vendor O/S debugging messages to UART(0)
esp.osdebug(0)
# start the REPL server on ws://XXX.XXX.XXX.XXX:8266/
webrepl.start()
