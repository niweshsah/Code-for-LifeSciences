import serial
import time

serial_port = 'abc'
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate, timeout=1)

def read_co2_level():
    try:
        if ser.in_waiting > 0:

            line = ser.readline().decode('utf-8').strip()
            co2_ppm = float(line.split(' ')[1])  
            return co2_ppm
        
    except serial.SerialException as e:
        print(f"Serial Exception: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return None

try:
    while True:
        co2_level = read_co2_level()
        if co2_level is not None:
            print(f"CO2 Level: {co2_level} ppm")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("\nProgram terminated by user")
finally:
    ser.close()
    print("Serial connection closed")
