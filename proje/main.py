
from detection.detector import Detector
from localization.estimator import Estimator
from pipeline.vision_pipeline import VisionPipeline
import os

model_path = "models/yolov8n.pt"
video_path = "data/test/test_video.mp4"
output_dir = "output"

def main():
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "detections"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "positions"), exist_ok=True)

    detector = Detector(model_path=model_path)
    estimator = Estimator()

    pipeline = VisionPipeline(detector=detector, estimator=estimator)
    detection_json, position_json = pipeline.process_video(video_path)

    with open(os.path.join(output_dir, "detections", "result.json"), "w") as f:
        f.write(detection_json)

    with open(os.path.join(output_dir, "positions", "result.json"), "w") as f:
        f.write(position_json)

    print(" Video işlendi, sonuçlar kaydedildi.")

if __name__ == "__main__":
    main()

