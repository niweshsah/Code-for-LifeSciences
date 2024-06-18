import serial
import time

serial_port = '/dev/ttyUSB0' 
ser = serial.Serial(serial_port, baud_rate, timeout=1)


def read_geiger_counter():
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            return line
    except serial.SerialException as e:
        print("Serial Exception")
    except Exception as e:
        print(f"Error: {e}")
    return None


while True:
        radiation_data = read_geiger_counter()
        if radiation_data:
            print(f"Radiation Level: {radiation_data}")
        time.sleep(1)



