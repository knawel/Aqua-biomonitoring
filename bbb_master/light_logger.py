import Adafruit_BBIO.GPIO as GPIO
import time
i = 30
P = "P8_10"
print GPIO

GPIO.setup(P, GPIO.OUT)

for j in range(i):
	GPIO.output(P, GPIO.HIGH)
	time.sleep(0.4)
	GPIO.output(P, GPIO.LOW)
	time.sleep(0.4)
GPIO.cleanup()
