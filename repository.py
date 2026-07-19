from abc import ABC, abstractmethod
from studiengang import Studiengang


class Repository(ABC):
    """Abstrakte Schnittstelle fuer die Datenspeicherung. Legt nur fest,
    DASS geladen und gespeichert werden kann, nicht WIE. So laesst sich
    die konkrete Speicherloesung (z. B. JSON, spaeter Datenbank)
    austauschen, ohne den uebrigen Code zu aendern (Polymorphie)."""
    @abstractmethod
    def laden(self) -> Studiengang:
        """Laedt einen Studiengang aus der Datenquelle."""
        ...

    @abstractmethod
    def speichern(self, studiengang: Studiengang) -> None:
        """Speichert den Studiengang in die Datenquelle."""
        ...