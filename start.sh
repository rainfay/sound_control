#!/bin/bash
#this script starts pulse audio. then kickes off the script
sleep 70s
/usr/bin/pulseaudio
/usr/bin/python3  /home/pi/sound_control/main.py
