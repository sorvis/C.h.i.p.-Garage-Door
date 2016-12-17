#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET
import CHIP_IO.GPIO as GPIO
import time

tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/garage', 'garage_status',
    '/garage/toggle', 'garage_toggle'
)

app = web.application(urls, globals())

class garage_status:
    def GET(self):
        return "<html><body><h1>Garage Status: Unknown</h1></body></html>"

class garage_toggle:
    def GET(self):
        GPIO.cleanup()
        GPIO.setup("XIO-P0", GPIO.OUT)

        print "Toggling the door...."
        GPIO.output("XIO-P0", GPIO.HIGH)
        time.sleep(.5)
        GPIO.output("XIO-P0", GPIO.LOW)
        GPIO.cleanup()
        return "<html><body>Door was toggled!</body></html>"


if __name__ == "__main__":
    app.run()