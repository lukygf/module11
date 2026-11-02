from ex1 import HealingCreatureFactory, TransformCreatureFactory


def tester(heal_factory: HealingCreatureFactory(), transform_factory: TransformCreatureFactory()) -> None:
    print("Testing Creature with healing capability")

    print(" Base:")
    heal_base = heal_factory.create_base()
    print(heal_base.describe())
    print(heal_base.attack())
    print(heal_base.heal())

    print(" Evolved:")
    heal_evolved = heal_factory.create_evolved()
    print(heal_evolved.describe())
    print(heal_evolved.attack())
    print(heal_evolved.heal())

    print("\nTesting Creature with transform capability")

    print(" Base:")
    transform_base = transform_factory.create_base()
    print(transform_base.describe())
    print(transform_base.attack())
    print(transform_base.transform())
    print(transform_base.attack())
    print(transform_base.revert())

    print(" Evolved:")
    transform_evolved = transform_factory.create_evolved()
    print(transform_evolved.describe())
    print(transform_evolved.attack())
    print(transform_evolved.transform())
    print(transform_evolved.attack())
    print(transform_evolved.revert())


if __name__ == "__main__":
    tester(HealingCreatureFactory(), TransformCreatureFactory())
