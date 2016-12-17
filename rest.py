#!/usr/bin/env python
from string import Template
import time
import web
import CHIP_IO.GPIO as GPIO
import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

urls = (
    '/garage', 'garage_status',
    '/garage/toggle', 'garage_toggle'
)

app = web.application(urls, globals())

class garage_status:
    def GET(self):
        with open('garage.html') as html_file:
            lines = html_file.readlines()
            html_template = ''.join(lines)
            template = Template(html_template)
            html = template.substitute(server_ip=get_ip_address())
            return html

class garage_toggle:
    def GET(self):
        try:
            GPIO.cleanup()
            GPIO.setup("XIO-P0", GPIO.OUT)

            print "Toggling the door...."
            GPIO.output("XIO-P0", GPIO.HIGH)
            time.sleep(.5)
            GPIO.output("XIO-P0", GPIO.LOW)
            GPIO.cleanup()
            return "<html><body>Door was toggled!</body></html>"
        except:
            return "Error calling GPIO pin"


if __name__ == "__main__":
    app.run()