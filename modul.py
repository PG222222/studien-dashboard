class Modul:
    def __init__(self, titel: str, ects: int) -> None:
        self._titel = titel
        self._ects = ects

    @property
    def titel(self) -> str:
        return self._titel

    @property
    def ects(self) -> int:
        return self._ects
    
from pruefungsleistung import Pruefungsleistung
from pruefungsstatus import Pruefungsstatus
from datetime import date


class Modul:
    def __init__(self, titel: str, ects: int) -> None:
        self._titel = titel
        self._ects = ects
        self._pruefungsleistungen = []

    def pruefungsleistung_anlegen(self, datum: date,
                                  note: float | None = None) -> Pruefungsleistung:
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
        return any(
            pl.status == Pruefungsstatus.BESTANDEN
            for pl in self._pruefungsleistungen
        )