#!/usr/bin/python3

class Plant:
    name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

        print(f"Plant created: {self.name}: {self._height:.1f}cm, {self._age} days old\n")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if value > 0:
            self._height = value
            print(f"Height updated: {self._height:.1f}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, value: int) -> None:
        if value > 0:
            self._age = value
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> None:
        print(f"\nCurrent state: {self.name}: {self._height:.1f}cm, {self._age} days old")

    def age(self) -> None:
        self._age = self._age + 1

    def grow(self) -> None:
        self.height = self.height + 0.8


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15, 10)

    rose.set_age(15)
    rose.show()


if __name__ == "__main__":
    main()
