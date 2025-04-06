from detection.preprocessor import Preprocessor
from detection.postprocessor import Postprocessor
import json
import cv2

class VisionPipeline:
    def __init__(self, detector, estimator):
        self.detector = detector
        self.estimator = estimator
        self.preprocessor = Preprocessor()
        self.postprocessor = Postprocessor()

    def process_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        frame_idx = 0
        all_detections = []
        frame_positions = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Görüntü temizleme
            frame = self.preprocessor.preprocess(frame)

            # Nesne tespiti
            result = self.detector.detect_frame(frame)
            detections = []
            for box in result.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = box
                detections.append({
                    "frame": frame_idx,
                    "bbox": [x1, y1, x2, y2],
                    "score": float(score),
                    "class_id": int(class_id)
                })

            
            zone_check = self.postprocessor.check_landing_zone(detections)

            
            all_detections.append({
                "frame": frame_idx,
                "detections": detections,
                "zones": zone_check
            })

            frame_idx += 1

        cap.release()

        # Pozisyon tahmini üret (simülasyon)
        position_json = self.estimator.estimate_from_video(video_path)

        return json.dumps(all_detections, indent=2), position_json
