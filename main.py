# SPDX-FileCopyrightText: 2021 faye archip
# SPDX-License-Identifier: MIT

"""Simple test for keypad on I2C RGB character LCD Shield or Pi Plate kits"""
import time
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import socket

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2
eqflag = 0
escape = 0
# Initialise I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.clear()
#ips=socket.gethostbyname(socket.gethostname())
lcd.message = "AUDIO BRIDGE \n ANALOG TO CAT"

#print(ips)

lcd.color = [100, 0, 0]
while True:
    if lcd.left_button:
        print("Left!")
        lcd.message = "Left!"

    elif lcd.up_button:
        print("Up!")
        lcd.message = "Up!"

    elif lcd.down_button:
        print("Down!")
        lcd.message = "Down!"

    elif lcd.right_button:
        print("Right!")
        lcd.message = "Right!"

    elif lcd.select_button:
        lcd.message = "Xair18 EQ"
        if eqflag == 1:
            lcd.message = "ON, Press DWN to Turn off "
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
                    time.sleep(1)
                    lcd.clear()
                time.sleep(0.5)

        if eqflag == 0:
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
            time.sleep(0.5)


        time.sleep(0.5)
#        lcd.clear()
