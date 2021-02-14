# Alexa ONLY Control... the GOOD Stuff

  - Lifted from https://github.com/thehookup/Motorized_MQTT_Blinds/releases/tag/Alexa_No_Hub

## Alexa Only with WiFi Manager

@thehookup thehookup released this on Apr 11, 2019 · 10 commits to master since this release

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

  Assets 4
  Alexa_Only_Blinds.bin
  408 KB
  Blinds_CONFIGURE_Portal_Alexa_Core_2.3.bin
  358 KB
  Source code (zip)
  Source code (tar.gz) 
