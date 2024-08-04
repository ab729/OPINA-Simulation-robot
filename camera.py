import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        processed_frame = self.process_frame(frame)
        ret, jpeg = cv2.imencode('.jpg', processed_frame)
        if not ret:
            return None
        return jpeg.tobytes()

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                height, width, _ = frame.shape
                if cx < width // 3:
                    self.move_left()
                elif cx > 2 * width // 3:
                    self.move_right()
                else:
                    self.move_forward()
            else:
                self.stop()
        else:
            self.stop()
        return frame

    def move_left(self):
        print("Moving left")

    def move_right(self):
        print("Moving right")

    def move_forward(self):
        print("Moving forward")

    def stop(self):
        print("Stopping")
