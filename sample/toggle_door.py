import CHIP_IO.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setup("XIO-P0", GPIO.OUT)

print "Toggling the door...."
GPIO.output("XIO-P0", GPIO.HIGH)
time.sleep(1)
GPIO.output("XIO-P0", GPIO.LOW)
GPIO.cleanup()
