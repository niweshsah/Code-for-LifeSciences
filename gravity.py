import smbus2
import time

DEVICE_ADDRESS = 0x53
POWER_CTL = 0x2D  
DATA_FORMAT = 0x31  
DATAX0 = 0x32 
ACCEL_SCALE = 0.004  

bus = smbus2.SMBus(1) 

def twos_complement(val, bits):

    if val & (1 << (bits - 1)):
        val = val - (1 << bits)
    return val

def read_gravity_acceleration():
    try:
        bus.write_byte_data(DEVICE_ADDRESS, POWER_CTL, 0x08)
        
        data_z0 = bus.read_i2c_block_data(DEVICE_ADDRESS, DATAX0 + 4, 2) 
        
        z_raw = twos_complement(data_z0[0] + (data_z0[1] << 8), 16)
        z_g = z_raw * ACCEL_SCALE
        
        return z_g
    
    except Exception as e:
        print("Error")
        return None

try:
    while True:
        gravity_acceleration = read_gravity_acceleration()
        if gravity_acceleration is not None:
            print(f"Acceleration due to Gravity (g): {gravity_acceleration:.2f}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram terminated by user")
finally:
    bus.write_byte_data(DEVICE_ADDRESS, POWER_CTL, 0x00)
    print("Measurement disabled")
