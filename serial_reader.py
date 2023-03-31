import threading
import serial
import time
time.sleep(1)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Replace '/dev/ttyUSB0' with the appropriate serial port on your system
latitude = None
longitude = None
def read_serial():
 while True:
    # time.sleep(10)
    # Read from serial port
    data = ser.readline().decode('utf-8').strip()

    # Check if the line contains latitude and longitude values
    if 'Lat:' in data:
        latitude = float(data.split('Lat: ')[-1])
    elif 'Long:' in data:
        longitude = float(data.split('Long: ')[-1])
    # print("Latitude=")
    # print(latitude)
    # print("longitude=")
    # print(longitude)
    # Wait for one second before reading again
    time.sleep(10)
 