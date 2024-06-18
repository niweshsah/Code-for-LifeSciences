import smbus2
import bme280
import time

BME280_I2C_ADDRESS = 0x76


bus = smbus2.SMBus(1)  

calibration_params = bme280.load_calibration_params(bus, BME280_I2C_ADDRESS)

def read_bme280_data():


    data = bme280.sample(bus, BME280_I2C_ADDRESS, calibration_params)
    temperature = data.temperature
    humidity = data.humidity
    pressure = data.pressure
    return temperature, humidity, pressure



while True:
        temperature, humidity, pressure = read_bme280_data()
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Humidity: {humidity:.2f} %")
        print(f"Pressure: {pressure:.2f} hPa")
        time.sleep(1)

