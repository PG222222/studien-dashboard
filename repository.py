from abc import ABC, abstractmethod
from studiengang import Studiengang


class Repository(ABC):
    @abstractmethod
    def laden(self) -> Studiengang:
        ...

    @abstractmethod
    def speichern(self, studiengang: Studiengang) -> None:
        ...