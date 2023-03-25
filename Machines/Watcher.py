from Machines.Machine import Machine

class Watcher(Machine):

    def __init__(self):
        super().__init__(name="Watcher", height=2.0, weight=12.2, max_width=0.3, max_depth=1.3, health=50)

    def shoot_eye_flash(self):
        print("flash")

    def physical_attack(self):
        print("Tail Swipe!")

