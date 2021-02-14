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

## Alexa only support (no hub required) is HERE


This release uses Amazon Alexa local control and WiFi Manager to configure and control your blinds. No other hub or device (other than a wifi router) is required for this version and there is no MQTT control.

This is a pre-compiled bin file to upload to a NodeMCU using the ESPEasy flashing tool (instructions below).
Install Instructions:

    Download the ESPEasy Flashing tool here: https://github.com/letscontrolit/ESPEasy/releases/
    Extract the zip file from the above link to your computer
    Download the .bin file for this release and place it in the same folder as the ESPEasy flashing tool.
    Plug in your NodeMCU using a USB Cable
    Run FlashESP8266.exe
    Select this bin file (Alexa_Only_Blinds.bin) under the firmware dropdown and press "Flash"

Setup Instructions:

    Connect to the "Blinds Setup" wifi access point that is being broadcast by your NodeMCU
    Enter your WiFi SSID and Password
    Enter the number of rotations required for your blinds to fully open/close (12 Recommended)
    Press save and wire your blinds as shown in the wiring diagram on the main page of this repository.

**If you mess up your settings you can connect a wire between GND and D1 to clear the saved settings on the NodeMCU.
If you have issues with discovery please try the "Blinds_CONFIGURE_Portal_Alexa_Core_2.3.bin" file
