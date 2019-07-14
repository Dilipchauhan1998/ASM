import RPi.GPIO as GPIO
import time
import picamera
import os

# Servo Motor 1 - p
op1 = 7

# Servo Motor 2 - q
op2 = 11

# Slider
op3 = 35
op4 = 36
op5 = 38
op6 = 37

# Stamp
op7 = 31
op8 = 33

# Y-Axis
op9 = 29
op10 = 32

# IR Sensor
op11 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(op3,GPIO.OUT)
GPIO.setup(op4,GPIO.OUT)
GPIO.setup(op5,GPIO.OUT)
GPIO.setup(op6,GPIO.OUT)
GPIO.setup(op7,GPIO.OUT)
GPIO.setup(op8,GPIO.OUT)
GPIO.setup(op9,GPIO.OUT)
GPIO.setup(op10,GPIO.OUT)
GPIO.setup(op11,GPIO.IN)


GPIO.output(op7,False)
GPIO.output(op8,False)
GPIO.output(op9,False)
GPIO.output(op10,False)
GPIO.setmode(GPIO.BOARD)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(op1,GPIO.OUT)
GPIO.setup(op2,GPIO.OUT)

p = GPIO.PWM(op1,50)
q = GPIO.PWM(op2,50)
ir = GPIO.input(op11)

##################################

# p = 80 53 56
# q = 6 7.5 7

##################################


def highLow(high, low):
	GPIO.output(high,True)
	GPIO.output(low,False)

def allFalse(A,B):
	GPIO.output(A,False)
	GPIO.output(B,False)

def servoStart():
	p.start(5)
	q.start(5)

def startP():
	p.start(5)

def startQ():
	q.start(5)

def stopP():
	p.stop()

def stopQ():
	q.stop()

def servoStop():
	p.stop()
	q.stop()

def servoReset():
	theta1 = 90
	duty2 = 6
	duty1 = float(theta1)/18 + 2
	p.ChangeDutyCycle(duty1)
	q.ChangeDutyCycle(duty2)
	time.sleep(0.5)


def totalDown():
	theta1 = 53
	duty2 = 7.5
	duty1 = float(theta1)/18 + 2
	p.ChangeDutyCycle(duty1)
	q.ChangeDutyCycle(duty2)
	time.sleep(0.5)

def up1():
	theta1 = 65
	duty2 = 7
	duty1 = float(theta1)/18 + 2
	p.ChangeDutyCycle(duty1)
	q.ChangeDutyCycle(duty2)
	time.sleep(1.8)

def sliderOut():
	highLow(op3,op4)
	highLow(op5,op6)
	time.sleep(0.97)
	allFalse(op3,op4)
	allFalse(op5,op6)

def sliderIn():
	highLow(op4,op3)
	highLow(op6,op5)
	time.sleep(0.97)
	allFalse(op3,op4)
	time.sleep(0.02)
	allFalse(op5,op6)	

##################################

# STAMP

def stamp():
	for j in range (0,1):
		for i in range (0,1):
			GPIO.output(op8,True)
			GPIO.output(op7,False)
			time.sleep(0.3)		#	down
		GPIO.output(op8,False)
		GPIO.output(op7,False)
		# time.sleep(0.2)
		for i in range (0,4):
			GPIO.output(op8,True)
			GPIO.output(op7,False)
			time.sleep(0.01)
			GPIO.output(op8,False)
			GPIO.output(op7,False)
			# time.sleep(0.2)

		GPIO.output(op8,False)
		GPIO.output(op7,False)
		time.sleep(0.2)


		for i in range (0,1):
			GPIO.output(op7,True)
			GPIO.output(op8,False)
			time.sleep(0.01)
			GPIO.output(op7,False)
			GPIO.output(op8,False)
			# time.sleep(0.2)
		GPIO.output(op7,False)
		GPIO.output(op8,False)
		# time.sleep(0.2)
		for i in range (0,1):
			GPIO.output(op7,True)
			GPIO.output(op8,False)
			time.sleep(0.33)		#	up
		GPIO.output(op7,False)
		GPIO.output(op8,False)
		time.sleep(0.2)

	GPIO.output(op7,False)
	GPIO.output(op8,False)
	GPIO.output(op9,False)
	GPIO.output(op10,False)

def YMoveBack():
	GPIO.output(op10,True)
	GPIO.output(op9,False)
	time.sleep(0.5)
	GPIO.output(op9,False)
	GPIO.output(op10,False)

def YMoveFront():
	GPIO.output(op9,True)
	GPIO.output(op10,False)
	time.sleep(0.55)
	GPIO.output(op9,False)
	GPIO.output(op10,False)

def YSliderBack():
	GPIO.output(op10,True)
	GPIO.output(op9,False)


	highLow(op4,op3)
	highLow(op6,op5)
	time.sleep(0.93)
	# time.sleep(1)
	GPIO.output(op9,False)
	GPIO.output(op10,False)
	time.sleep(0.2)
	
	allFalse(op3,op4)
	time.sleep(0.02)
	allFalse(op5,op6)

def YSliderFront():
	GPIO.output(op10,False)
	GPIO.output(op9,True)


	highLow(op3,op4)
	highLow(op5,op6)
	time.sleep(0.93)
	# time.sleep(1)
	GPIO.output(op9,False)
	GPIO.output(op10,False)
	time.sleep(0.2)
	
	allFalse(op3,op4)
	allFalse(op5,op6)
##################################

# CODE STARTS HERE:

##################################

# sliderOut()
# sliderIn()
# YMoveFront()
# YMoveBack()
# servoStart()
# servoReset()
# stamp()
# YSliderBack()
# YSliderFront()



print("Is the stamp at extreme position? 1->Yes, 0->No ")
extreme = int(input())
print("Enter the number of pages: ")
pages = int(input())
servoStart()
camera = picamera.PiCamera()
for j in range (0,pages):
	print "Stamping page "+str(j+1)+"..."
	stamp()
	print "Page "+str(j+1)+" stamped..."
	servoReset()
	if(extreme==1):
		YSliderBack()
	else:
		sliderIn()
	if(j>0):
		save = str(j)+".jpg"
		camera.capture(save)
		print "Page " + str(j) + " saved..."
	time.sleep(0.2)
	totalDown()
	up1()
	if(extreme==1):
		YSliderFront()
	else:
		sliderOut()
	time.sleep(0.3)
	servoReset()
	time.sleep(0.5)
if(extreme==1):
	YSliderBack()
else:
	sliderIn()
save = str(pages)+".jpg"
camera.capture(save)
print "Page " + str(pages) + " saved!"
time.sleep(0.2)
if(extreme==1):
	YSliderFront()
else:
	sliderOut()
servoReset()
servoStop()

print ("Converting to PDF...")
arr = []
for i in range (1,pages+1):
	arr.append(str(i)+".jpg")
os.system("convert "+' '.join(arr)+' op.pdf')
print ("PDF saved as op.pdf ...")

# ir = GPIO.input(op11)
# while 1:
# 	if(GPIO.input(op11)==True):
# 		print("1")
# 	else:
# 		print("0")
# 	time.sleep(0.5)

GPIO.cleanup()
