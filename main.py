#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
 
#classes
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
Sensor = ColorSensor(Port.S1)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

robot.settings(Speeding, 20, 30, 40)
 
#variable
Speeding = -200
TurnTimer = 10
Turn = True
 
Presseding = False


#Rood obstakel omver rijden
if Sensor.color() == Color.RED:
    robot.drive(200)
else:
    robot.drive(100)


# Groene Knop gebruiken
if Sensor.color() == Color.GREEN:
    robot.stop()
)


#zwarte lijn volgen
while True:
if Sensor.color() == Color.BLACK:
        robot.drive(Speeding, 0)
elif Sensor.color() != Color.BLACK:

if Turn == False:
       TurnTimer - 1
       left_motor.run(Speeding)

if TurnTimer == 0:
    Turn = False
    TurnTimer + 10
else:
    Turn = False
 

if TurnTimer == 0:
    Turn = True
    TurnTimer + 10
elif Turn == True:
    TurnTimer - 1




