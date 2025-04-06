import json
import random

class Estimator:
    def __init__(self):
       
        pass

    def estimate_from_video(self, video_path):
        """
        Örnek olarak videodan alınan pozisyonları rastgele üretir.
        İleride optical flow tabanlı hesaplamaya çevrilebilir.
        """
        positions = []

        for frame_num in range(30):  
            x = round(random.uniform(0, 10), 2)
            y = round(random.uniform(0, 10), 2)
            z = round(random.uniform(0, 5), 2)

            positions.append({
                "frame": frame_num,
                "position": {"x": x, "y": y, "z": z}
            })

        return json.dumps(positions, indent=2)
