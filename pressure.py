import time
from smbus2 import SMBus
from bmp180 import BMP180

bus = SMBus(1)
sensor = BMP180(bus)

while True:
    try:
        pressure = sensor.pressure
        print(f"Pressure: {pressure:.2f} hPa")
        time.sleep(1)

    except Exception as e:
        print("Error")
        time.sleep(1)
