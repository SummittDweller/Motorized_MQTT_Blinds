# Alexa_Only_Blinds Flash Commands for `esptool.py`

Lifted from https://michael-kuehnel.de/iot/2019/07/16/how-to-flash-esp8266-and-esp32-to-use-espruino-firmware-on-mac-os.html

## Erasing the Board
```
/System/Volumes/Data/Users/mark/Library/Python/3.8/bin/esptool.py \
  --port /dev/cu.usbserial-0001  \
  --baud 115200                               \
  erase_flash
```

## Flashing `Alexa_Only_Blinds`
```
cd ~/GitHub/Motorized_MQTT_Blinds/Alexa-Only
/System/Volumes/Data/Users/mark/Library/Python/3.8/bin/esptool.py \
  --port /dev/cu.usbserial-0001  \
  --baud 115200                               \
  write_flash                                 \
  --flash_freq 80m                            \
  --flash_mode qio                            \
  --flash_size 32m                            \
  0x0000 Alexa_Only_Blinds.bin                       
```
