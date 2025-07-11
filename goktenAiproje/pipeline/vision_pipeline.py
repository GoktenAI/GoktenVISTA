from detection.preprocessor import Preprocessor
from detection.postprocessor import Postprocessor
import json
import cv2
import os
import glob

class VisionPipeline:
    def __init__(self, detector, estimator):
        self.detector = detector
        self.estimator = estimator
        self.preprocessor = Preprocessor()
        self.postprocessor = Postprocessor()

    def process_frames(self, frame_dir, initial_positions):
        """
        - frame_dir: .jpg frame'lerin bulunduğu klasör
        - initial_positions: frame_idx -> pozisyon (x, y, z), sadece health=1 olanlar
        """
        frame_paths = sorted(glob.glob(os.path.join(frame_dir, "*.jpg")))
        result_json = []

        prev_frame = None
        prev_position = {"x": 0.0, "y": 0.0, "z": 0.0}

        for frame_path in frame_paths:
            frame_name = os.path.basename(frame_path)
            frame_idx = int(frame_name.replace("frame_", "").replace(".jpg", ""))

            frame = cv2.imread(frame_path)
            if frame is None:
                continue

            # Görüntü ön işleme
            frame = self.preprocessor.preprocess(frame)

            # YOLO nesne tespiti + sadeleştirme
            result = self.detector.detect_frame(frame)
            detections = self.detector.extract_detections(result)

            # Postprocessor: UAP/UAI için landing_status güncelle
            detections = self.postprocessor.check_landing_zone(detections)

            # Pozisyon kestirimi (Görev 2)
            if frame_idx in initial_positions:
                # GPS sağlıklı frame'ler
                position = initial_positions[frame_idx]
                prev_position = position
            else:
                if prev_frame is None:
                    # İlk frame ama pozisyon verisi yoksa, sıfırla
                    position = {"x": 0.0, "y": 0.0, "z": 0.0}
                else:
                    # Görüntüye dayalı pozisyon kestirimi (senin estimator'a bağlı)
                    position = self.estimator.estimate_from_pair(prev_frame, frame, prev_position)
                    prev_position = position

            prev_frame = frame.copy()

            # JSON çıktısı (Şartnameye %100 uygun)
            frame_result = {
                "id": frame_idx,
                "user": "http://localhost/users/4/",
                "frame": f"http://localhost/frames/{frame_idx:06d}/",
                "detected_objects": [
                    {
                        "cls": det["cls"],
                        "landing_status": str(det.get("landing_status", "-1")),
                        "top_left_x": det["top_left_x"],
                        "top_left_y": det["top_left_y"],
                        "bottom_right_x": det["bottom_right_x"],
                        "bottom_right_y": det["bottom_right_y"]
                    }
                    for det in detections
                ],
                "detected_translations": [
                    {
                        "translation_x": position["x"],
                        "translation_y": position["y"],
                        "translation_z": position["z"]
                    }
                ]
            }

            result_json.append(frame_result)

        return json.dumps(result_json, indent=2)
