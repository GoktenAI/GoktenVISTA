import math

class TrajectoryAnalyzer:
    def __init__(self):
        self.positions = []

    def add_position(self, x, y, z):
        self.positions.append((x, y, z))

    def calculate_displacement(self):
        
        if len(self.positions) < 2:
            return 0.0

        x1, y1, z1 = self.positions[0]
        x2, y2, z2 = self.positions[-1]

        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1

        return round(math.sqrt(dx**2 + dy**2 + dz**2), 2)

    def get_path_length(self):
        
        total = 0.0
        for i in range(1, len(self.positions)):
            x1, y1, z1 = self.positions[i-1]
            x2, y2, z2 = self.positions[i]

            dx = x2 - x1
            dy = y2 - y1
            dz = z2 - z1

            dist = math.sqrt(dx**2 + dy**2 + dz**2)
            total += dist

        return round(total, 2)
