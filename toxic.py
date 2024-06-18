from gpiozero import MCP3008
import time

adc = MCP3008(channel=0)

def read_sensor():
    try:
        raw = adc.value
        conc = map_to_concentration(raw)
        return conc
    except Exception as e:
        print(f"Error: {e}")
        return None

def map_to_concentration(raw):
    max_raw = 1023
    max_conc = 10.0
    return (raw / max_raw) * max_conc

try:
    while True:
        conc = read_sensor()
        if conc is not None:
            print(f"Concentration: {conc:.2f} mM")
        time.sleep(1)

except KeyboardInterrupt:
    pass


