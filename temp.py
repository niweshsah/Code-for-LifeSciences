import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

MIN_TEMP = - 15.0
MAX_TEMP = 122.0  

while True:
    try:
        temperature = sensor.get_temperature()
        
        print(f"Temperature: {temperature:.2f}°C")
        
        if temperature < MIN_TEMP:
            print("Warning")
        elif temperature > MAX_TEMP:
            print("Warning")
        
    except Exception as e:
        print("Error ")
    
    time.sleep(1)
