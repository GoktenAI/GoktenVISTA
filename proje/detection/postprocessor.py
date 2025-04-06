# detection/postprocessor.py

class Postprocessor:
    def __init__(self):
        
        pass

    def check_landing_zone(self, detections):
        
        zones = {
            "UAP": {"bbox": None, "suitable": True},
            "UAI": {"bbox": None, "suitable": True}
        }

        for det in detections:
            class_id = det["class_id"]
            bbox = det["bbox"]

            if class_id == 2:  # UAP
                zones["UAP"]["bbox"] = bbox
            elif class_id == 3:  # UAI
                zones["UAI"]["bbox"] = bbox

        for det in detections:
            if det["class_id"] in [0, 1]:  # Taşıt veya İnsan
                for zone_name, zone_info in zones.items():
                    if zone_info["bbox"] is not None:
                        if self._is_inside(det["bbox"], zone_info["bbox"]):
                            zones[zone_name]["suitable"] = False

        return zones

    def _is_inside(self, inner_box, outer_box):
        
        x1, y1, x2, y2 = inner_box
        ox1, oy1, ox2, oy2 = outer_box

        return (x1 >= ox1 and y1 >= oy1 and x2 <= ox2 and y2 <= oy2)
