#!/bin/bash
#this script starts pulse audio. then kickes off the script
sleep 30s
/usr/bin/pulseaudio --start
/usr/bin/python3  /home/pi/sound_control/main.py
