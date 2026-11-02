from abc import ABC, abstractmethod


class HealCapability(ABC):

    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):

    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass
