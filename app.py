from flask import Flask, render_template, Response
# from camera_stream import gen_frames
from input_handler import handle_input
from flask_socketio import SocketIO, emit
# from camera_switch import switch_camera
import serial
from flask_socketio import send, emit
# from serial_reader import latitude, longitude
import threading, time

app = Flask(__name__)
app.debug=True
socketio = SocketIO(app)

latitude = None
longitude = None

# Serial reader function to be run in a separate thread
def serial_reader():
    global latitude, longitude
    with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
        while True:
            # Read from serial port
            data = ser.readline().decode('utf-8').strip()

            # Check if the line contains latitude and longitude values
            # if 'Latitude: ' in data or 'Latitude:' in data:
            #     latitude = float(data.split('Latitude:')[2])
            # if 'Longitude: ' in data or 'Longitude: ' in data:
            #     print("longtude condition entered")
            #     longitude = float(data.split('Longitude:')[-1])
            values = data.split(",")
            latitude = float(values[0].split(":")[1])
            longitude = float(values[1].split(":")[1])
            print("Latitude:", latitude)
            print("Longitude:", longitude)

            print("latitude=")
            print(latitude)
            print("longitude=")
            print(longitude)
            # Wait for one second before reading again
            time.sleep(10)

# Start the serial reader thread when the app starts
serial_thread = threading.Thread(target=serial_reader)
serial_thread.start()


# @app.route('/video_feed')
# def video_feed():
    # return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/control', methods=['POST'])
def control():
    message = handle_input()
    print(message)
    return message


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/switch_camera', methods=['POST','GET'])
def switchcamera():
    print("switch camera route accessed")
    # Call the function to switch cameras
    switch_camera()
    return "switch camera route finished running"
# code for displaying latitude and longitude 
@app.route('/latitude')
def get_latitude():
    global latitude
    return str(latitude)

# endpoint to get the longitude value
@app.route('/longitude')
def get_longitude():
    global longitude
    return str(longitude)


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


def send_frame(frame):
    emit('frame', frame)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
