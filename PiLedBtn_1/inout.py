import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
while 1:
    if GPIO.input(11):
		GPIO.output(18, False)
    else:
	    GPIO.output(18, True)
        
    if GPIO.input(12):
        GPIO.output(15, False) 
    else: 
        GPIO.output(15, True)
