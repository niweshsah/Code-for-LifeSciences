import time
import smbus2
import bh1750 
import serial  

from atlas_i2c import AtlasI2C  


bus = smbus2.SMBus(1)
light_sensor = bh1750.BH1750(bus)

orp_sensor = AtlasI2C()

while True:
    try:
        light_intensity = light_sensor.measure_high_res()
      
        orp_reading = orp_sensor.query("R")

        print(f"Light Intensity: {light_intensity} lux")
        print(f"ORP: {orp_reading} mV")

        time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)
