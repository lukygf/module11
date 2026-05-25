#!/usr/bin/python3

class Plant:
    # Clase anidada para estadísticas 
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0
            self.shade_calls: int = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._stats = self._Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        """Comprueba si la edad es mayor a 365 días."""
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        """Crea una planta con valores por defecto."""
        return cls("Unknown plant", 0.0, 0)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        self._stats.show_calls += 1  # Incrementa contador [cite: 210]
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def age(self) -> None:
        self._stats.age_calls += 1  # Incrementa contador [cite: 210]
        self._age += 1

    def grow(self) -> None:
        self._stats.grow_calls += 1  # Incrementa contador [cite: 210]
        self._height += 0.8


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds_count: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42  # Genera semillas al florecer 

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds_count}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk

    def produce_shade(self) -> None:
        self._stats.shade_calls += 1  # Incrementa contador específico [cite: 211]
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self._height:.1f}cm "
              f"long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


def display_stats(plant: Plant) -> None:
    """Función única para mostrar estadísticas de cualquier planta."""
    print(f"[statistics for {plant.name}]")
    s = plant._stats
    print(f"Stats: {s.grow_calls} grow, {s.age_calls} age, {s.show_calls} show")
    if isinstance(plant, Tree):
        print(f"{s.shade_calls} shade")


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    # Flower y stats [cite: 215]
    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)

    # Tree y stats de sombra [cite: 216]
    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5.0)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)

    # Clase Seed [cite: 217]
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    # Planta Anónima [cite: 218]
    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_stats(anon)


if __name__ == "__main__":
    main()
