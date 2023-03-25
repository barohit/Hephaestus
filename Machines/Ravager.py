from Machines.Machine import Machine


class Ravager(Machine):

    def __init__(self):
        super().__init__(name="Ravager", height=2.0, weight=25.0, max_width=1.2, max_depth=3.5, health=150)

    def shoot_ravager_cannon(self):
        print("do do do do do do")

    def physical_attack(self):
        print("Swipe")

