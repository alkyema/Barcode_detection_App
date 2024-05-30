from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import threading
import time


app = Flask(__name__)

# Global variables
is_detection_running = False
qr_code_count = 0
count = 0

def detect_barcodes(camera):
    global is_detection_running

    model_barcode = YOLO(r"D:\Coding\python\code\project\Bar_Code_detection\main hackaton\barcode detection s.pt")

    while is_detection_running:
        success, frame = camera.read()
        cv2.resize(frame,(720,720),0,0)
        if not success:
            break

        results_barcode = model_barcode.track(frame, persist=True)

        if len(results_barcode) > 0 and results_barcode[0].boxes is not None:
            barcode_count = len(results_barcode[0].boxes)
        else:
            barcode_count = 0

        total_count = qr_code_count + barcode_count

        cv2.putText(frame, f"Total Count: {total_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        annotated_frame_barcode = results_barcode[0].plot()
        

        ret, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()

        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

def generate(camera):
    global is_detection_running
    while is_detection_running:
        yield next(detect_barcodes(camera))

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/start_detection')
def start_detection():
    global is_detection_running
    if not is_detection_running:
        is_detection_running = True
        camera = cv2.VideoCapture(0)
        return Response(detect_barcodes(camera), mimetype='multipart/x-mixed-replace; boundary=frame')
    return 'Barcode detection is already running.'

@app.route('/stop_detection')
def stop_detection():
    global is_detection_running
    is_detection_running = False
    time.sleep(2) 
    return 'Barcode detection stopped.'

if __name__ == '__main__':
    app.run(debug=True) 