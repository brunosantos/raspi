import RPi.GPIO as GPIO
import time
# blinking function
def blink(pin):
    # set up GPIO output channel
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)
        return
GPIO.cleanup() 
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# blink GPIO17 50 times
for i in range(0,50):
    blink(15)
    blink(16)
    blink(18)
GPIO.cleanup() 