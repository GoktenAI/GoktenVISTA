from ultralytics import YOLO
import cv2
import json

class Detector:
    def __init__(self, model_path="models/yolo.pt"):
        self.model = YOLO(model_path)

    def detect_frame(self, frame):
        results = self.model.predict(source=frame, conf=0.4, verbose=False)
        return results[0]

    def detect_from_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        detections = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            result = self.detect_frame(frame)
            for box in result.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = box
                detections.append({
                    "bbox": [x1, y1, x2, y2],
                    "score": float(score),
                    "class_id": int(class_id),
                })

        cap.release()
        return json.dumps(detections, indent=2)
