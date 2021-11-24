#!/bin/bash
/usr/bin/parec -d  alsa_input.usb-Burr-Brown_from_TI_USB_Audio_CODEC-00.analog-stereo  | /usr/bin/pacat  -d alsa_output.usb-Razer_Razer_Kraken_Kitty_Edition_00000000-00.analog-stereo  --latency-msec 1 &
