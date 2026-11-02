from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, InvalidStrategyError

def tournament(opponents: list[tuple]) -> None:
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            factory_1, strategy_1 = opponents[i]
            factory_2, strategy_2 = opponents[j]

            creature_1 = factory_1.create_base()
            creature_2 = factory_2.create_base()

            print("\n* Battle *")
            print(creature_1.describe())
            print(" VS")
            print(creature_2.describe())
            print(" Now fight!")            
            try:
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    opponents_1 = [(flame_factory, normal_strategy), (heal_factory, defensive_strategy)]
    print(f"{len(opponents_1)} opponents involved")
    tournament(opponents_1)

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    opponents_2 = [(flame_factory, aggressive_strategy), (heal_factory, defensive_strategy)]
    print(f"{len(opponents_2)} opponents involved")
    tournament(opponents_2)

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    opponents_3 = [(aqua_factory, normal_strategy), (heal_factory, defensive_strategy), (transform_factory, aggressive_strategy)]
    print(f"{len(opponents_3)} opponents involved")
    tournament(opponents_3)
