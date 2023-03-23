from flask import Flask, render_template, Response
from camera_stream import gen_frames
from input_handler import handle_input


app = Flask(__name__)


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/control', methods=['POST'])
def control():
    message = handle_input()
    print(message)
    return message


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
