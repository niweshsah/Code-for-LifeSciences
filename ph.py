import time
from smbus2 import SMBus

I2C_ADDRESS = 99
I2C_BUS = 1

bus = SMBus(I2C_BUS)

def read_ph_sensor():
    try:
        bus.write_byte(I2C_ADDRESS, 0x52)  
        time.sleep(1.5) 

        data = bus.read_i2c_block_data(I2C_ADDRESS, 0, 31)

        result = ''.join([chr(i) for i in data])
        return result.strip()
    
    except Exception as e:
        print("Error ")
        return None

while True:
    try:
        reading = read_ph_sensor()
        if reading:
            pH_level = float(reading) 
            if  pH_level > 12.5:
                print("Very basic environment")
            elif pH_level < 0 :
                print("Very acidic environment")
            else:
                print(f"pH Level: {pH_level}")
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)
