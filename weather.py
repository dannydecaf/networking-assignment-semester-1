from flask import Flask, render_template
from sense_hat import SenseHat

app = Flask(__name__)

@app.route('/')

def index():
	sense = SenseHat()

	celcius = round(sense.get_temperature(), 1)
	fahrenheit = round(1.8 * celcius + 32, 1)
	humidity = round(sense.get_humidity(), 1)
	
	pressure = round(sense.get_pressure(), 1)

	coldmusic="https://www.youtube.com/embed/gied8n7LR2g"
	hotmusic="https://www.youtube.com/embed/JB_iylafXiQ"

	return render_template('weather.html', celcius=celcius, fahrenheit=fahrenheit,
	humidity=humidity, pressure=pressure, music_link=hotmusic if celcius > 32 else coldmusic)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
