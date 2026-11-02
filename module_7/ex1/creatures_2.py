from .capabilities import HealCapability, TransformCapability
from ex0 import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return ("Sproutling uses Vine Whip!")

    def heal(self) -> str:
        return ("Sprouting heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return ("Bloomelle uses Petal Dance")

    def heal(self) -> str:
        return ("Blomelle heals itself and others for a large amount")


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return ("Shiftling performs a boosted strike!")
        else:
            return ("Shiftling attacks normally.")

    def transform(self) -> str:
        if not self.transformed:
            self.transformed = not self.transformed
            return ("Shiftling shifts into a sharper form!")
        else:
            return ("Shiftling is already transformed")

    def revert(self) -> str:
        if self.transformed:
            self.transformed = not self.transformed
            return ("Shiftling returns to normal.")
        else:
            return ("Shiftling is already normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return ("Morphagon unleashes a devastating morph strike!")
        else:
            return ("Morphagon attacks normally.")

    def transform(self) -> str:
        if not self.transformed:
            self.transformed = not self.transformed
            return ("Morphagon morphs into a dragonic battle form!")
        else:
            return ("Morphagon is already transformed")

    def revert(self) -> str:
        if self.transformed:
            self.transformed = not self.transformed
            return ("Morphagon stabilizes its form.")
        else:
            return ("Morphagon is already normal.")
