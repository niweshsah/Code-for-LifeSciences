import smbus2
import time


HMC5883L_I2C_ADDR = 0x1E

CONFIG_A_REG = 0x00
CONFIG_B_REG = 0x01
MODE_REG = 0x02
DATA_REG_BEGIN = 0x03

bus = smbus2.SMBus(1) 

def hmc5883l_init():
   
    bus.write_byte_data(HMC5883L_I2C_ADDR, CONFIG_A_REG, 0x70)  
    bus.write_byte_data(HMC5883L_I2C_ADDR, CONFIG_B_REG, 0xA0)  
    bus.write_byte_data(HMC5883L_I2C_ADDR, MODE_REG, 0x00)      
    print("initialized")

def hmc5883l_read_data():
    data = bus.read_i2c_block_data(HMC5883L_I2C_ADDR, DATA_REG_BEGIN, 6)
    
    x = data[0] << 8 | data[1]
    z = data[2] << 8 | data[3]
    y = data[4] << 8 | data[5]
    
    if x > 32767:
        x -= 65536
    if y > 32767:
        y -= 65536
    if z > 32767:
        z -= 65536
    
    return x, y, z


hmc5883l_init()
time.sleep(1) 

while True:
        x, y, z = hmc5883l_read_data()
        print(f"X: {x}, Y: {y}, Z: {z}")
        time.sleep(1)


