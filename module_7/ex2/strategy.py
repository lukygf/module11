from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import Sproutling, Bloomelle, Shiftling, Morphagon, HealCapability, TransformCapability

class InvalidStrategyError(Exception):
    pass

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass
    
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True
    
    def act(self, creature: Creature) -> None:
        print(creature.attack())

class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False
    
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}' for this aggressive strategy")

class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}' for this defensive strategy")

