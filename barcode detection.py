from ultralytics import YOLO
import cv2
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

video = cv2.VideoCapture(0)
model = YOLO(r"C:\Users\satwi\Downloads\robotics\yolov8n.pt")
detection = 0

while video.isOpened():
    ret, frame = video.read()
    if ret:
        frame = cv2.resize(frame, (640, 640), 0, 0)
        results = model.track(source=frame, conf=0.35, persist=True)

        img = results[0].plot()
        cv2.imshow("frame", img)
        print(detection)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()

print("Object detection prediction completed.")
