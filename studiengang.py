from datetime import date
from semester import Semester

class Studiengang:
    def __init__(self, name: str, startdatum: date, zieldatum_abschluss: date,
                 ziel_notendurchschnitt: float, geplante_ects: int) -> None:
        self._name = name
        self._startdatum = startdatum
        self._zieldatum_abschluss = zieldatum_abschluss
        self._ziel_notendurchschnitt = ziel_notendurchschnitt
        self._geplante_ects = geplante_ects
        self._semester = []

    def semester_anlegen(self, nummer: int) -> Semester:
        semester = Semester(nummer)
        self._semester.append(semester)
        return semester    
    
    @property
    def semester(self) -> tuple:
        return tuple(self._semester)