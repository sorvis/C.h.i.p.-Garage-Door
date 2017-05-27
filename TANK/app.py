from flask import Flask, render_template
import RPi.GPIO as GPIO ## Import GPIO library


app = Flask(__name__)
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'
@app.route('/forwardon')
def forwardon():
    GPIO.setup(40, GPIO.OUT) ## Setup GPIO Pin 40 to OUT
    GPIO.output(40,True) ## Turn on GPIO pin 40
@app.route('/forwardoff')
def forwardoff
    GPIO.setup(40, GPIO.OUT) ## Setup GPIO Pin 40 to OUT
    GPIO.output(40,false) ## Turn off GPIO pin 40

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
