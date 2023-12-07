from flask import Flask,render_template,Response
from camera import VideoCamera

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'b'Context-Type:image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



