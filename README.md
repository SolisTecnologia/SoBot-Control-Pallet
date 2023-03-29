# Solis Robot - SoBot
![](https://github.com/SolisTecnologia/SoBot-Control-Pallet/blob/main/png/SoBotPallet.png)

# Introduction

AMR (autonomous mobile robotics) platform equipped with a camera system, ultrasonic and photoelectric sensors, works with a high rate of precision and repeatability of its movements, as it uses stepper motors in its movement and navigation, the SoBot also can be termed as a research and development interface, as it facilitates the practical experimentation of algorithms from the simplest to the most complex level.

This product was developed 100% by Solis Tecnologia, and has a lot of technology employing cutting-edge concepts, such as:

The motors can be controlled simultaneously or individually.
The user can select different accessories to implement to the robot.
Several programming languages can be used to connect via API.

# Components

* Main structure in aluminum
* Removable fairing with magnetic attachment points
* Element handling system with pallet
* Robot Control Driver
* Raspberry Pi 4B board <img align="center" height="30" width="40" src="https://github.com/devicons/devicon/blob/master/icons/raspberrypi/raspberrypi-original.svg">
* 2x NEMA-23 Stepper Motors
* 2x 12V/5A battery
* Wireless Gamepad F710  <img align="center" height="40" width="40" src="https://github.com/SolisTecnologia/SoBot-Control-Pallet/blob/main/png/control.png">

# Programming Example
## Control Pallet - [Control_Pallet.py](https://github.com/SolisTecnologia/SoBot-Control-Pallet/blob/main/Controle_Pallet.py)
Programming example to control the "SoBot" and the lift with Pallet using the Logitech F710 controller.  
  
The Elevator is control with R2 button to up and L2 button to down.  
The moviments direction are control with directions buttons.  

### Programming Language

* Python  <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">

### Required Libraries

~~~python
import inputs
import serial
~~~

The ''inputs'' library is used to capture user input from gamepad.  
The ''serial'' library for serial/usb Raspberry connection with the robot controller driver.  

### Code Description

Commands used to configure wheel parameters and motion proportional gain, as follows:

~~~python
# Configure wheel parametres
usb.write(b"WP MT1 WD99,84")
usb.write(b"WP MT2 WD99,54")
usb.write(b"WP DW264,95")
# Set the motion proportional gain
usb.write(b"PG SO2,3 CA3,22 DF6,11 RI-6")
~~~

The commands used in this example to control SoBot are continuous movement commands, as follows:

~~~python
usb.write(b"MT0 MC MD0 AT800 DT800 V8")         # Configure continuous mode with curve on the same axis
usb.write(b"MT0 MC MD1 RI100 AT800 DT800 V8")   # Configure continuous mode with differential curve
usb.write(b"MT0 ME1")               # Enable continuous movement
usb.write(b"MT0 ME0")               # Disable continuous movement
usb.write(b"MT0 ML")                # Move left
usb.write(b"MT0 MR")                # Move right
usb.write(b"MT0 MB")                # Move backward
usb.write(b"MT0 MF")                # Move Forward
usb.write(b"MT0 MP")                # Pause movement
~~~

To control the elevator module, the following commands are used:

~~~python
usb.write(b"EL DN")	    # Move elevator down
usb.write(b"EL UP")	    # Move elevator up
usb.write(b"EL ST")	    # Pause the elevator
~~~

Commands are also used to control the lighting of the LED tape as follows:

~~~python
usb.write(b"LT E1 RD0 GR0 BL100")   # Turn on Led Tap
usb.write(b"LT E0")                 # Turn off Led Tap
~~~
For more information about the commands used, check the Robot Commands Reference Guide.

### Flowchart

![](https://github.com/SolisTecnologia/SoBot-Control-Pallet/blob/main/png/Flowchart_Control_Pallet.png)

# Reference Link
[SolisTecnologia website](https://solistecnologia.com/produtos/robotsingle)

# Please Contact Us


If you have any problem when using our robot after checking this tutorial, please contact us.

### Phone:
+55 1143040786

### Technical support email: 
contato@solistecnologia.com.br

![](https://github.com/SolisTecnologia/SoBot-Simple-Route/blob/master/png/logo.png)
