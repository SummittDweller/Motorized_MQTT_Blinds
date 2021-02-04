# Motorized_MQTT_Blinds


This repository is to accompany my Motorized_MQTT_Blinds video:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/1O_1gUFumQM/0.jpg)](https://www.youtube.com/watch?v=1O_1gUFumQM)

## Parts List
Stepper Motors: https://amzn.to/2D5rVsF

Stepper Drivers: https://amzn.to/2OZqW1W

NodeMCU: https://amzn.to/2I89xDF

12V Power Supply: https://amzn.to/2G2ZJrf

Buck Converter: https://amzn.to/2UsQ7jA

## 3D Printing

Download the correct STL file for your style of tilt rod

## Wiring Schematic

![alt text](https://github.com/thehookup/Motorized_MQTT_Blinds/blob/master/Schematic.jpg?raw=true)

**Dont forget to cut the center trace on the stepper motor as shown in the youtube video**

## File setup

Fill out the entire USER CONFIGURATION section of the code.

You should leave "STEPS_TO_CLOSE" at 12 to start with.  It can be adjusted for your specific blinds

## Home Assistant YAML

Replace "BlindsMCU" with your MQTT_CLIENT_ID if you changed it in the file setup

```yaml
cover:
  - platform: mqtt
    name: "Motorized Blinds"
    command_topic: "BlindsMCU/blindsCommand"
    set_position_topic: "BlindsMCU/positionCommand"
    position_topic: "BlindsMCU/positionState"
    state_topic: "BlindsMCU/positionState"
    retain: true
    payload_open: "OPEN"
    payload_close: "CLOSE"
    payload_stop: "STOP"
    position_open: 0
    position_closed: 12
  ```

## Recommended Tools

Ender3 3d Printer: https://amzn.to/2GcznnZ

Dupont Crimper and Connector Set: https://amzn.to/2X1Oeap

## Alexa only support available in the releases tab of this repo!

# Additional Resources

##  MQTT Server Creation
https://www.google.com/search?client=firefox-b-1-d&q=mqtt+server
https://www.home-assistant.io/docs/mqtt/broker/
https://learn.adafruit.com/set-up-home-assistant-with-a-raspberry-pi/raspberry-pi-server-setup
https://learn.adafruit.com/set-up-home-assistant-with-a-raspberry-pi/mqtt-setup

## Home Assistant Configuration
http://homeassistant.local:8123   -- My Home Assistant, an RPI B+ located in my office closet
https://www.home-assistant.io/getting-started/onboarding/

### NodeMCU (Arduino) Info
**Attention!** Make sure you are using a micro-USB cable that supports _*data*_ as well as power!

Note that there are comm port issues with Big Sur that impact Arduino.  For more info see:
https://github.com/esp8266/Arduino/issues/7763 and the fix in https://forum.arduino.cc/index.php?topic=702144.0.

#### Now for the Resources
https://www.open-homeautomation.com/2016/06/10/program-an-esp8266-from-arduino-on-macos/
https://en.wikipedia.org/wiki/NodeMCU
https://www.instructables.com/How-to-Program-NodeMCU-on-Arduino-IDE/
https://github.com/nodemcu/nodemcu-firmware
https://medium.com/@bass.pj/nodemcu-esp8266-getting-started-with-arduino-on-macos-1cdc61565496
https://electrosome.com/esp8266-arduino-programming-led-blink/    -- LED blink test

From the Amazon.com product description...

Product description:
ESP8266 is a highly integrated chip designed for the needs of a new connected world. It offers a complete and self-contained Wi-Fi networking solution, allowing it to either host the application or to offload all Wi-Fi networking functions from another application processor.

Instruction & Steps of How to Use:

1. Download the Arduino IDE, the latest version.
2. Install the IDE
3. Set up your Arduino IDE as: Go to File->Preferences and copy the URL below to get the ESP board manager extensions: http://arduino.esp8266.com/stable/package_esp8266com_index.json Placing the http:// before the URL lets the Arduino IDE use it...otherwise it gives you a protocol error.
4. Go to Tools > Board > Board Manager> Type "esp8266" and download the Community esp8266 and install.
5. Set up your chip as:
Tools -> Board -> NodeMCU 1.0 (ESP-12E Module)
Tools -> Flash Size -> 4M (3M SPIFFS)
Tools -> CPU Frequency -> 80 Mhz
Tools -> Upload Speed -> 921600
Tools-->Port--> (whatever it is)
6. Download and run the 32 bit flasher exe at Github(Search for nodemcu/nodemcu-flasher/tree/master/ at Github) github.com/nodemcu/nodemcu-flasher/tree/master/Win32/Release Or download and run the 64 bit flasher exe at: github.com/nodemcu/nodemcu-flasher/tree/master/Win64/Release
7. In Arduino IDE, look for the old fashioned Blink program. Load, compile and upload.
8. Go to FILE> EXAMPLES> ESP8266> BLINK, it will start blinking.

### Control via Arduino Uno
https://www.makerguides.com/28byj-48-stepper-motor-arduino-tutorial/
https://www.seeedstudio.com/blog/2019/03/04/driving-a-28byj-48-stepper-motor-with-a-uln2003-driver-board-and-arduino/
https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/

### Control via Raspberry Pi
https://www.aranacorp.com/en/control-a-stepper-with-raspberrypi/
http://www.scraptopower.co.uk/Raspberry-Pi/how-to-connect-stepper-motors-a-raspberry-pi
https://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/
https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/

### Projects Using 28BYJ-48 w/ Supplied Drivers
https://www.youtube.com/watch?v=avrdDZD7qEQ
https://create.arduino.cc/projecthub/debanshudas23/getting-started-with-stepper-motor-28byj-48-3de8c9
https://www.instructables.com/Arduino-28BJY-48-Stepper-Motor-Simple-and-Improved/
https://www.makerguides.com/28byj-48-stepper-motor-arduino-tutorial/
https://www.hackster.io/BEASTIDREES62/driving-28byj-48-stepper-motor-control-with-joystick-544122
https://hackaday.io/projects?tag=28ByJ-48
https://www.seeedstudio.com/blog/2019/03/04/driving-a-28byj-48-stepper-motor-with-a-uln2003-driver-board-and-arduino/
