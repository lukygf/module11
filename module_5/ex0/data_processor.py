#!/usr/bin/python3

from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):

    def __init__(self) -> None:
        self.list = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple:
        tupla = (self.list[0], self.rank)
        self.rank += 1
        del self.list[0]
        return tupla


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
    
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if not isinstance(data, list):
            return False
        for num in data:
            if not isinstance(num, (int, float)):
                return False
        return True
    
    def ingest(self, data: Any) -> None:

        if not self.validate(data):
            raise TypeError("Improper numeric data")

        if isinstance(data, (int, float)):
            self.list.append(str(data))
        
        if isinstance(data, list):
            for num in data:
                self.list.append(str(num))



class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if not isinstance(data, list):
            return False
        for num in data:
            if not isinstance(num, str):
                return False
        return True
    
    def ingest(self, data: Any) -> None:

        if not self.validate(data):
            raise TypeError("Improper text data")

        if isinstance(data, str):
            self.list.append(data)
        
        if isinstance(data, list):
            for value in data:
                self.list.append(value)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    #print("Test invalid ingestion of string 'foo' without prior validation:")
    #numeric.ingest('foo')

    print(f"Processing data: [10, 2, 5, 89, 3]")
    numeric.ingest([10, 2, 5, 89, 3])

    print("Extracting 3 values...")
    print(f"Tupla: {numeric.output()}")
    print(f"Tupla: {numeric.output()}")
    print(f"Tupla: {numeric.output()}")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")

    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 values...")
    print(f"Tupla: {text.output()}")





if __name__ == "__main__":
    main()