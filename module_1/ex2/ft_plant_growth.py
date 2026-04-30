#!/usr/bin/python3

class Plant:
    name: str
    height: float
    _age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def age(self) -> None:
        self._age = self._age + 1

    def grow(self) -> None:
        self.height = self.height + 0.8


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose._age = 30
    rose.show()

    initial_height: float = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")

        rose.age()
        rose.grow()
        rose.show()

    total_growth: float = rose.height - initial_height
    print(f"Growth this week: {total_growth:.1f}cm")


if __name__ == "__main__":
    main()
