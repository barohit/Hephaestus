from Machines.Machine import Machine

class Glinthawk(Machine):

    def __init__(self):
        super().__init__(name="Glinthawk", height=2.5, weight=15.0, max_width=1.4, max_depth=1, health=100)

    def spit_chillwater(self):
        print("gulp")

    def physical_attack(self):
        print("Swoop")

