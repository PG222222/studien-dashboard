from datetime import date
from semester import Semester

class Studiengang:
    """Oberstes Entity-Objekt. Verwaltet seine Semester per Komposition:
    Semester werden ausschliesslich hier erzeugt und existieren nicht
    unabhaengig vom Studiengang."""
    def __init__(self, name: str, startdatum: date, zieldatum_abschluss: date,
                 ziel_notendurchschnitt: float, geplante_ects: int) -> None:
        self._name = name
        self._startdatum = startdatum
        self._zieldatum_abschluss = zieldatum_abschluss
        self._ziel_notendurchschnitt = ziel_notendurchschnitt
        self._geplante_ects = geplante_ects
        self._semester = []

    def semester_anlegen(self, nummer: int) -> Semester:
        """Erzeugt ein neues Semester und nimmt es in die interne Liste auf.

        Bewusst als Factory-Methode umgesetzt: Da der Studiengang das
        Semester selbst erzeugt, kann von aussen kein Semester
        eingehaengt werden. Das setzt die Komposition im Code durch.
        """
        semester = Semester(nummer)
        self._semester.append(semester)
        return semester    
    
    @property
    def semester(self) -> tuple:
        # Tupel statt Liste: schuetzt die interne Struktur vor
        # Veraenderung von aussen (kein append moeglich)
        return tuple(self._semester)
    
    @property
    def erreichte_ects_gesamt(self) -> int:
        """Summe der erreichten ECTS ueber alle Semester (abgeleitet)."""
        return sum(s.erreichte_ects for s in self._semester)

    @property
    def aktueller_notendurchschnitt(self) -> float | None:
        """Nach ECTS gewichteter Durchschnitt aller benoteten Leistungen.
        Gibt None zurueck, solange keine Note vorliegt."""
        noten = []
        gewichte = []
        for semester in self._semester:
            for modul in semester.module:
                for pl in modul.pruefungsleistungen:
                    if pl.note is not None:
                        noten.append(pl.note * modul.ects)
                        gewichte.append(modul.ects)
        if not gewichte:
            return None
        return sum(noten) / sum(gewichte)
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def startdatum(self) -> date:
        return self._startdatum

    @property
    def zieldatum_abschluss(self) -> date:
        return self._zieldatum_abschluss

    @property
    def ziel_notendurchschnitt(self) -> float:
        return self._ziel_notendurchschnitt

    @property
    def geplante_ects(self) -> int:
        return self._geplante_ects