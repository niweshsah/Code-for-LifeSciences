import time
import board
import busio

import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1015(i2c)

channel = AnalogIn(ads, ADS.P0)


def read_moisture_level():
    try:
        raw_value = channel.value
        
        moisture_percent = (raw_value / 65535) * 100 
        
        return moisture_percent
        
    except Exception as e:
        print(f"Error: {e}")
        return None

while True:
        moisture_level = read_moisture_level()
        if moisture_level is not None:
            print(f"Soil Moisture Level: {moisture_level:.2f}%")
        
        time.sleep(1)

