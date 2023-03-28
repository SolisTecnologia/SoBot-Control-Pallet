#!/usr/bin/python3
"""
Solis Robot - SoBot

Controle_Pallet.py: Programming example to control the "SoBot" and the lift
with Pallet using the Logitech F710 controller.

Created By   : Vinicius M. Kawakami
Version      : 1.0

Company: Solis Tecnologia
"""

import inputs
import serial

flag_start = 0
flag_BT_RZ = 0
flag_BT_Z = 0

# Find the Logitech F710 controller ID connected to the Raspberry Pi
gamepad = inputs.devices.gamepads[0]
print(gamepad)

# Configure the serial port
usb = serial.Serial('/dev/ttyACM0', 57600, timeout=0, dsrdtr=False)
usb.flush()

# Configure wheel parametres
usb.write(b"WP MT1 WD99,84")
usb.write(b"WP MT2 WD99,54")
usb.write(b"WP DW264,95")

# Set the motion proportional gain
usb.write(b"PG SO2,3 CA3,22 DF6,11 RI-6")

# Configure operating parametres in continuous mode
usb.write(b"MT0 MC MD0 AT800 DT800 V8")

while True:
    
    events = inputs.get_gamepad()   # Checks if there was any control event
    
    for event in events:
        
        # Checks if it is event of type "KEY"
        if event.ev_type == "Key":
            print(f"Evento code: {event.code}")
            print(f"Evento state: {event.state}")

            # Check if the event code is "BTN_START" in state 1
            if event.code == "BTN_START" and event.state == 1:
                print("Botão Start pressionado")
                if flag_start == 0:
                    flag_start = 1
                    usb.write(b"MT0 ME1")               # Enable motors
                    usb.write(b"LT E1 RD0 GR0 BL100")   # Turn on Led Tap

                else:
                    flag_start = 0
                    usb.write(b"MT0 ME0")               # Disable motors
                    usb.write(b"LT E0")                 # Turn off Led Tap

            # Check if the event code is "BTN_SOUTH" in state 1
            if event.code == "BTN_SOUTH" and event.state == 1:
                print("Botão A pressionado")

            # Check if the event code is "BTN_EAST" in state 1
            elif event.code == "BTN_EAST" and event.state == 1:
                print("Botão B pressionado")

            # Check if the event code is "BTN_NORTH" in state 1
            elif event.code == "BTN_NORTH" and event.state == 1:
                print("Botão X pressionado")

            # Check if the event code is "BTN_WEST" in state 1
            elif event.code == "BTN_WEST" and event.state == 1:
                print("Botão Y pressionado")

            # Check if the event code is "BTN_TR" in state 1
            elif event.code == "BTN_TR" and event.state == 1:
                print("Botão RB pressionado")
                # Configure continuous mode with curve on the same axis
                usb.write(b"MT0 MC MD0 AT800 DT800 V8")

            # Check if the event code is "BTN_TL" in state 1
            elif event.code == "BTN_TL" and event.state == 1:
                print("Botão LB pressionado")
                # Configure continuous mode with differential curve
                usb.write(b"MT0 MC MD1 RI100 AT800 DT800 V8")

        # Checks if it is event of type "Absolute"
        if event.ev_type == "Absolute":
            print(f"Evento code: {event.code}")
            print(f"Evento state: {event.state}")

            ### Buttons to control the direction ###
            # Events with the MODE button disabled
            # Check if the event code is "ABS_HAT0X"
            if event.code == "ABS_HAT0X":
                if flag_start:                  # Check if flag_start is enable
                    if event.state == -1:       # Check state (left direction) of the button
                        print("Botão ESQ pressionado")
                        usb.write(b"MT0 ML")

                    elif event.state == 1:      # Check state (right direction) of the button
                        print("Botão DIR pressionado")
                        usb.write(b"MT0 MR")

                    else:
                        usb.write(b"MT0 MP")

            # Check if the event code is "ABS_HAT0Y"
            if event.code == "ABS_HAT0Y":
                if flag_start:                  # Check if flag_start is enable
                    if event.state == -1:       # Check state (front direction) of the button
                        print("Botão FRENTE pressionado")
                        usb.write(b"MT0 MF")

                    elif event.state == 1:      # Check state (back direction) of the button
                        print("Botão TRAS pressionado")
                        usb.write(b"MT0 MB")

                    else:
                        usb.write(b"MT0 MP")
            
            ### Buttons to control the lift ###
            # Check if the event code is "ABS_RZ"
            if event.code == "ABS_RZ":
                if event.state >= 1:            # Check if state is greater than 1 (button pressed)
                    if flag_BT_RZ == 0:
                        flag_BT_RZ = 1
                        print("Botão RZ pressionado")
                        usb.write(b"EL UP")
                elif event.state == 0:
                    print("Botão RZ solto")
                    flag_BT_RZ = 0
                    usb.write(b"EL ST")

            # Check if the event code is "ABS_Z"
            if event.code == "ABS_Z":
                if event.state >= 1:            # Check if state is greater than 1 (button pressed)
                    if flag_BT_Z == 0:
                        flag_BT_Z = 1
                        print("Botão Z pressionado")
                        usb.write(b"EL DN")
                elif event.state == 0:
                    print("Botão Z solto")
                    flag_BT_Z = 0
                    usb.write(b"EL ST")
