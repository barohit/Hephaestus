from Machines.Machine import Machine


class Behemoth(Machine):

    def __init__(self):
        super().__init__(name="Behemoth", height=3.8, weight=90.0, max_width=2.9, max_depth=5.8, health=325)

    def gravity_pulse(self):
        print("fizz")

    def launch_rock_stream(self):
        print("blast!")

    def physical_attack(self):
        print("Charge!")

