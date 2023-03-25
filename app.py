from flask import Flask, render_template, Response
# from camera_stream import gen_frames
from input_handler import handle_input
from flask_socketio import SocketIO, emit
from camera_switch import switch_camera

app = Flask(__name__)
app.debug=True
socketio = SocketIO(app)


@app.route('/video_feed')
def video_feed():
    # return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    #return an empty response for debugging
    return ""


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


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


def send_frame(frame):
    emit('frame', frame)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
