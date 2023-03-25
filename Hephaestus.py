from Machines.Machine import Machine
from Machines.Behemoth import Behemoth
from Machines.Glinthawk import Glinthawk
from Machines.Ravager import Ravager
from Machines.Strider import Strider
from Machines.Thunderjaw import Thunderjaw
from Machines.Watcher import Watcher

class Hephaestus:
    def create_machine(self, machine_class: str) -> Machine:
        if machine_class == "Behemoth":
            return Behemoth()
        elif machine_class == "Glinthawk":
            return Glinthawk()
        elif machine_class == "Ravager":
            return Ravager()
        elif machine_class == "Strider":
            return Strider()
        elif machine_class == "Thunderjaw":
            return Thunderjaw()
        elif machine_class == "Watcher":
            return Watcher()
        else:
            print("This model of Hephaestus cannot create this machine. Please check if this model exists, and if so, please update the operating system and firmware.")


