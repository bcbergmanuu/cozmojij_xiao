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


print("ku")

states = [True, True]

# loop forever
while True:


    if not d0.value: 
        if states[0] == False:
            states[0] = True
            kbd.send(Keycode.A)
    if d0.value:
        if states[0] == True:
            states[0] = False
            kbd.send(Keycode.A)

    if not d1.value:        
        if states[1] == False:
            states[1] = True
            kbd.send(Keycode.B)
    if d1.value:
        if states[1] == True:
            states[1] = False
            kbd.send(Keycode.B)
           

    

    