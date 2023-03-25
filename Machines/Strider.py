from Machines.Machine import Machine


class Strider(Machine):

    def __init__(self):
        super().__init__(name="Strider", height=2.3, weight=20.0, max_width=0.8, max_depth=3.2, health=100)

    def run(self):
        print("neeeeeiigh")

    def physical_attack(self):
        print("Charge and kick!")

