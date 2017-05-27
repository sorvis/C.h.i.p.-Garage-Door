from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'
@app.route('/forwardon')
def forwardon():
import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(40, GPIO.OUT) ## Setup GPIO Pin 40 to OUT
GPIO.output(40,True) ## Turn on GPIO pin 40
@app.route('/forwardoff')
def forwardoff
import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(40, GPIO.OUT) ## Setup GPIO Pin 40 to OUT
GPIO.output(40,false) ## Turn off GPIO pin 40

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
