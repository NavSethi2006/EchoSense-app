#THIS FILE IS FOR HARDWARE AND SERVER


#########################
### AUTHOR @Amir-Nafissi
#########################

import RPi.GPIO as GPIO
import time
import os
import socket
import threading

#networking stuff by @NavSethi2006
#####################################
height = None

def thread_func():
  while True: 
    height = c.recv(1042).decode()
    height = height - (height / 2)
    print(height)

thread = threading.Thread(target=thread_func)

s = socket.socket()        
print ("Socket successfully created")
 
port = 8080               

height = None

s.bind(("", port))        
print ("socket binded to %s" %(port))
 
s.listen(5)    
print ("socket is listening")           
c, addr = s.accept() 
#####################################

#pins for back ultrasonic sensor
TRIG_1=21
ECHO_1=20

#pins for front ultrasonic sensor
TRIG_2=23
ECHO_2=24

GPIO.setmode(GPIO.BCM)

thread.start()

while True:

	#---------#back sensor distance measurement---------
	#print("distance measurement in progress")
	GPIO.setup(TRIG_1,GPIO.OUT)
	GPIO.setup(ECHO_1,GPIO.IN)
	GPIO.output(TRIG_1,False)
	#print("waiting for sensor to settle")
	time.sleep(0.2)
	GPIO.output(TRIG_1,True)
	time.sleep(0.00001) #wait for 10 micro second
	GPIO.output(TRIG_1,False)
	while GPIO.input(ECHO_1)==0: #wait till echo is LOW
		pulse_start=time.time()
	while GPIO.input(ECHO_1)==1: #wait till echo is HIGH
		pulse_end=time.time()
	#calculating distance
	pulse_duration=pulse_end-pulse_start
	distance_1=pulse_duration*17150
	distance_1=round(distance_1,2)
	print("distance_1:",distance_1,"cm")
	if distance_1 <= height:
		os.system("mpg123 beep_sound.mp3")
		os.system("mpg123 above_sound.mp3")
	time.sleep(0) #can be changed


	#---------#front sensor distance measurement---------
	#print("distance measurement in progress")
	GPIO.setup(TRIG_2,GPIO.OUT)
	GPIO.setup(ECHO_2,GPIO.IN)
	GPIO.output(TRIG_2,False)
	#print("waiting for sensor to settle")
	time.sleep(0.2)
	GPIO.output(TRIG_2,True)
	time.sleep(0.00001) #wait for 10 micro second
	GPIO.output(TRIG_2,False)
	while GPIO.input(ECHO_2)==0: #wait till echo is LOW
		pulse_start=time.time()
	while GPIO.input(ECHO_2)==1: #wait till echo is HIGH
		pulse_end=time.time()
	#calculating distance
	pulse_duration=pulse_end-pulse_start
	distance_2=pulse_duration*17150
	distance_2=round(distance_2,2)
	print("distance_2:",distance_2,"cm")
	if distance_2 <= 100:
		if distance_2 <= 40:
			if distance_2 <= 10:
				os.system("mpg123 below_sound_plus_beeping_2.mp3")
			os.system("mpg123 below_sound_plus_beeping_1.mp3")
		os.system("mpg123 beeping_faster.mp3")

		
	time.sleep(0) #can be changed


