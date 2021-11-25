# SPDX-FileCopyrightText: 2021 faye archip
# SPDX-License-Identifier: MIT

"""Simple test for keypad on I2C RGB character LCD Shield or Pi Plate kits"""
import time
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import socket
import subprocess
import sys

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2
eqflag = 0
escape = 0
# Initialise I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
#kill running sound bridges 
subprocess.run(["killall","pacat"])
# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.clear()
#ips=socket.gethostbyname(socket.gethostname())
lcd.message = "AUDIO BRIDGE \n ANALOG TO CAT"

#print(ips)

lcd.color = [100, 0, 0]
while True:
    if lcd.left_button:
      #  print("Left!")
        lcd.message = "Turn on =^_^=\nWith EQ"
        subprocess.run("./EQon.sh")
        subprocess.run("./neko.sh")

    elif lcd.up_button:
       # print("Up!")
        lcd.clear()
        lcd.message = "EQon"
        subprocess.run("./EQon.sh")

    elif lcd.down_button:
       # print("Down!")
        lcd.clear()
        lcd.message = "EQoff"
        subprocess.run("./EQoff.sh")

    elif lcd.right_button:
      #  print("Right!")
        lcd.clear()
        lcd.message = "Turn off =^_^="
        subprocess.run(["killall","pacat"])

    elif lcd.select_button:
        lcd.clear()
        lcd.message = "House lights"
        subprocess.run("./houselight.sh")
"""
        lcd.message = "House lights"
        if eqflag == 1:
            lcd.clear()
            lcd.message = "ON, Press DWN to\nTurn off "
            escape = 0
            while escape == 0:
                if lcd.select_button:
                    escape = 1
                    lcd.message ="EXIT"
                    lcd.clear()
                elif lcd.down_button:
                    escape = 1
                    eqflag = 0
                    #poke the xair here
                    lcd.message = "TURNING OFF EQ"
                    time.sleep(.5)
                    lcd.clear()
                time.sleep(0.5)

        if eqflag == 0:
            lcd.clear()
            lcd.message = "OFF, Press UP\n to Turn ON "
            escape = 0
            while escape == 0:
                if lcd.select_button:
                    escape = 1
                    lcd.message ="EXIT"
                    lcd.clear()
                elif lcd.up_button:
                    escape = 1
                    eqflag = 1
                    #xair poke
                    lcd.message = "TURNING ON EQ"
                    lcd.clear()
            time.sleep(0.5) */

"""


time.sleep(0.5)
#        lcd.clear()
def lights(switch):
    #this function will call shell scripts to trigger the lighing controler Lightfactory 
    #0 switch to lightinng mode on controler
    #1 House lights 
    #2 Blue
    #3 Red
    #4 Show
    #5 Fay Look
    #6 Panic
    if switch == 1: #house lights
        #do house lights 
    if switch == 2: # Blue
        #do blue
    if switch == 3:
        #do red
    if switch == 4:
        #do show
    if switch == 5:
        #do fay's look
    if switch == 6:
        #do panic
    if switch == 0:
        #do control function 
