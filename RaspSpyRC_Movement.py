#RaspSpy RC, A PI Controlled RC Spy Car
#Made By David Warren
#For the use of UI Mode, Run RaspSpyRC_UI but don't delete this script (RaspSpyRC_UI uses this script for movement
#Command Line Mode Not Made Yet

import RPi.GPIO as GPIO 
import time 
from datetime import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
backServo = GPIO.PWM(12,50)
backServo.start(0)
backServo.ChangeDutyCycle(7)
timenow = str(datetime.now())
f = open("Log.txt", "a") 
f.write('\n \n' + timenow)
    
#def Movement(): 
    #direction = input("Enter Direction (Left = L, Right = R, Forward = F, Stop = S, None = N)\n")
    #raw_sec = input("Enter The Time Of Movment In Sec I.E. 5, Press Enter For 0\n") or '0' 
    #sec = int(raw_sec)  




#print("Welcome To RaspSpy RC By: David Warren \nWhen Asked To Input Direction Put L, R, F, S, Or W (L = Left, R = Right, F = Forward, S = Stop, (This Stops the Script) W = Wait) \nThen Input Time Of Movement In Sec I.E. 5 \nAll Inputs Will Be Saved In Log.TXT")
#time.sleep(1)
#print("Connecting......")
#time.sleep(3) 
#print("Connected") 
#time.sleep(2)
#input("Press Enter To Start RaspSpy....")
#CLM()
def Left(raw_sec):
    sec = int(raw_sec)
    direction = 'Left' 
    f.write('\n' + direction)
    f.write(' For ' + raw_sec +' Seconds') 
    GPIO.output(16, GPIO.HIGH)
    backServo.ChangeDutyCycle(12)
    time.sleep(sec)
    GPIO.output(16, GPIO.LOW)
    backServo.ChangeDutyCycle(7)
    print("Done")
    GPIO.cleanup
    
def Right(raw_sec):
    sec = int(raw_sec)
    direction = 'Right'
    f.write('\n' + direction)
    f.write(' For ' + raw_sec + ' Seconds') 
    GPIO.output(18, GPIO.HIGH)
    backServo.ChangeDutyCycle(2)
    time.sleep(sec)
    GPIO.output(18, GPIO.LOW)
    backServo.ChangeDutyCycle(7)
    print("Done")
    GPIO.cleanup
    
def Forward(raw_sec):
    sec = int(raw_sec)
    direction = 'Forward'
    print(raw_sec)
    f.write('\n' + direction) 
    f.write(' For ' + raw_sec + ' Seconds') 
    GPIO.output(16, GPIO.HIGH) 
    GPIO.output(18, GPIO.HIGH) 
    time.sleep(sec) 
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    print("Done")
    GPIO.cleanup

def Wait(raw_sec):
    sec = int(raw_sec)
    direction = 'Wait' 
    f.write('\n' + direction) 
    f.write(' For ' + raw_sec + ' Seconds')
    time.sleep(sec)
    print("Done")
def Stop(raw_sec):
    sec = int(raw_sec)
    time.sleep(sec)
    f.write('\nClosed') 
    f.write('\n' + timenow) 
    f.close() 
    exit()
     


    

