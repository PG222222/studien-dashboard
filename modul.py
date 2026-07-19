from pruefungsleistung import Pruefungsleistung
from pruefungsstatus import Pruefungsstatus
from datetime import date


class Modul:
    """Verwaltet seine Pruefungsleistungen per Komposition - sie werden
    hier erzeugt und existieren nicht unabhaengig vom Modul."""
    def __init__(self, titel: str, ects: int) -> None:
        self._titel = titel
        self._ects = ects
        self._pruefungsleistungen = []

    def pruefungsleistung_anlegen(self, datum: date,
                                  note: float | None = None) -> Pruefungsleistung:
        """Erzeugt eine Pruefungsleistung im Modul (Factory-Methode,
        Komposition - analog zu semester_anlegen im Studiengang)."""
        pl = Pruefungsleistung(datum, note)
        self._pruefungsleistungen.append(pl)
        return pl

    @property
    def titel(self) -> str:
        return self._titel

    @property
    def ects(self) -> int:
        return self._ects

    @property
    def pruefungsleistungen(self) -> tuple:
        return tuple(self._pruefungsleistungen)

    @property
    def bestanden(self) -> bool:
        """Abgeleitet: True, sobald mindestens eine Leistung bestanden ist."""
        return any(
            pl.status == Pruefungsstatus.BESTANDEN
            for pl in self._pruefungsleistungen
        )