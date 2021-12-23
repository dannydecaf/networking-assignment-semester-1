from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.clear()

blue = (187, 224, 255)
red = (255, 0, 0)
black = (0, 0, 0)
orange = (255,265,0)
redorange = (255, 69, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
violet = (238, 130, 238)
indigo = (75, 0, 130)
white = (255,250,250)

try:
       while True:
            tempCel = round(sense.get_temperature(), 2)
            tempFahr = round(1.8 * tempCel + 32, 2)
            pressure = round(sense.get_pressure(), 2)
            humidity = round(sense.get_humidity(), 2)
            if tempCel>=30:
              sense.show_message("It's roastin!", text_colour = red, back_colour = black)
            elif tempCel[20] < 30:
              sense.show_message("Warm enough", text_colour = orange, back_colour = redorange)
            elif tempCel[10] < 20:
              sense.show_message("Not too warm, not too cold", text_colour = green, back_colour = yellow)
            elif tempCel[5] < 10:
              sense.show_message("Chilly enough", text_colour = indigo, back_colour = violet)
            else:
              sense.show_message("It's FREEZIN!", text_colour = blue, back_colour = white)
            print()
            print("Temperature in Celcius:",tempCel)
            print()
            print("Temperature in Fahrenheit:",tempFahr)
            print()
            print("Pressure:",pressure)
            print()
            print("Humidity:",humidity)
            print()
            print()
            print()

            time.sleep(1)
except KeyboardInterrupt:
      sense.clear()
