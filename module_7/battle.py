from ex0 import CreatureFactory, FlameFactory, AquaFactory


def factory_tester(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(f"{base.attack()}")
    print(f"{base.describe()}\n")

    print(f"{evolved.attack()}")
    print(f"{evolved.describe()}\n")


def battle_tester(flame_factory: CreatureFactory, aqua_factory: CreatureFactory) -> None:
    print("Testing Battle")

    flame_base = flame_factory.create_base()
    aqua_base = aqua_factory.create_base()

    print(f"{flame_base.describe()}")
    print("VS")
    print(f"{aqua_base.describe()}")
    print("Fight!")
    print(f"{flame_base.attack()}")
    print(f"{aqua_base.attack()}")


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    factory_tester(flame_factory)
    factory_tester(aqua_factory)

    battle_tester(flame_factory, aqua_factory)
