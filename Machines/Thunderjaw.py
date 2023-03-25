from Machines.Machine import Machine


class Thunderjaw(Machine):

    def __init__(self):
        super().__init__(name="Thunderjaw", height=10.0, weight=125.0, max_width=2.5, max_depth=6.7, health=450)

    def shoot_jaw_cannon(self):
        print("do do do do do do do do do do do ")

    def physical_attack(self):
        print("Tail Swipe")

    def launch_disc_laser(self):
        print("beeeeeeaaaaaaam")

