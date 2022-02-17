import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid

import busio
uart = busio.UART(board.TX, board.RX, baudrate=9600)

# configure device as keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# define buttons
d0 = DigitalInOut(board.D0)
d0.direction = Direction.INPUT
d0.pull = Pull.UP

d1 = DigitalInOut(board.D1)
d1.direction = Direction.INPUT
d1.pull = Pull.UP

d2 = DigitalInOut(board.D2)
d2.direction = Direction.INPUT
d2.pull = Pull.UP

d3 = DigitalInOut(board.D3)
d3.direction = Direction.INPUT
d3.pull = Pull.UP

d4 = DigitalInOut(board.D4)
d4.direction = Direction.INPUT
d4.pull = Pull.UP


# loop forever
while True:

    if not d0.value:       
            kbd.send(Keycode.C)
    if not d1.value:       
            kbd.send(Keycode.D)
    if not d2.value:       
            kbd.send(Keycode.E)
    if not d3.value:       
            kbd.send(Keycode.F)
    if not d4.value:       
            kbd.send(Keycode.G)
    
 

   