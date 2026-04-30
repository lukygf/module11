#!/usr/bin/python3

class Plant:
    name: str
    height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

        print(f"Created: {self.name}: {self.height:.1f}cm, {self._age} days old")

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

def main() -> None:
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)


if __name__ == "__main__":
    main()
