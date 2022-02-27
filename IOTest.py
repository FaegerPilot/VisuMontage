#Script to test all I/O's

import time
import board
import neopixel

from subprocess import check_call

from gpiozero import Button, LED, RotaryEncoder

# Pins and Objects
greenStatus = LED(25)
redStatus = LED(26)

LeftEncoder = RotaryEncoder(23,24)
RightEncoder = RotaryEncoder(5,6)

LeftSwitch = Button(22,False,)
RightSwitch = Button(4,False,)

MpSwitch = Button(27,False, hold_time=5)

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 60

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def shutdown():
    check_call(['sudo','poweroff'])

def UpdatePixel(wait):
    pixel[LeftEncoder.steps] = (0,255,0)
    pixel[RightEncoder.steps] = (255,0,0)

while True:
    greenStatus.source = LeftSwitch
    redStatus.source = RightSwitch
    
    LeftEncoder.when_rotated = UpdatePixel
    RightEncoddder.when_rotated = UpdatePixel

    MpSwitch.when_held = shutdown
    
    time.sleep(0.01)
    