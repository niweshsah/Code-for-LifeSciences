import smbus2
import time

VEML6070_ADDR_LOW = 0x38
VEML6070_ADDR_HIGH = 0x39

VEML6070_CMD_ACK = 0x02  
VEML6070_CMD_ACK_THD = 0x03  

bus = smbus2.SMBus(1)  

def Sensor_start():

    bus.write_byte(VEML6070_ADDR_LOW, VEML6070_CMD_ACK)
    bus.write_byte(VEML6070_ADDR_HIGH, VEML6070_CMD_ACK_THD)
    print("VEML6070 initialized")

def read_uv():

    uv_low = bus.read_byte(VEML6070_ADDR_LOW)
    uv_high = bus.read_byte(VEML6070_ADDR_HIGH)
    uv_value = (uv_high << 8) | uv_low
    return uv_value


Sensor_start()
time.sleep(1)  

while True:
        uv_value = read_uv()
        print("UV Value: ", uv_value)
        time.sleep(1)
