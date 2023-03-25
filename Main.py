from Hephaestus import Hephaestus


def main():
    main_cauldrom = Hephaestus()
    local_ravager = main_cauldrom.create_machine("Ravager")
    local_thunderjaw = main_cauldrom.create_machine("Thunderjaw")
    local_ravager.physical_attack()
    local_thunderjaw.shoot_jaw_cannon()


main()
