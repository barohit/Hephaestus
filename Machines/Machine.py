
class Machine:

    def __init__(self, name: str, health: float, height: float, max_width: float, max_depth: float, weight: float):
        self.name = name
        self.health = health
        self.height = height
        self.max_width = max_width
        self.max_depth = max_depth
        self.weight = weight

    def physical_attack(self):
        pass
