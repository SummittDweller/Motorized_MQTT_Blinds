My latest wiring for the fine-adjust Raspberry Pi portion of this project uses long sections of CAT5 cable for the 4-wire connection from the DRV8825 to the motor.  Each CAT5 twisted pair of wires (blue + blue/white, green + green/white, brown + brown/white, orange + orange/white) is joined at each end such that each pair carries one of the 4 controller-to-motor signals.  This arrangement calls for short wires (typically Dupont "breadboard" wires) to connect the power supply, DRV8825 motor controler, and the control source (either an ESP8266 or Raspberry Pi 3B+) together.  It seems to work nicely even over long (20' or more) lengths of CAT5 cable.

The 4-wires from the motor are colored:

  - Blue
  - Yellow
  - Orange, and
  - Pink

I use a female CAT5 connector at the motor with corresponding "scheme B" wire colors as indicated below.

| Motor Wire | CAT5 Pair |
| --- | --- |
| Blue | Blue |
| Pink | Brown |
| Yellow | Green |
| Orange | Orange |
