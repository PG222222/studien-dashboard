from datetime import date
from pruefungsstatus import Pruefungsstatus


class Pruefungsleistung:
    """Einzelne Pruefungsleistung. Die Note ist optional (None, solange
    nicht bewertet); der Status wird daraus abgeleitet, nicht gespeichert."""
    def __init__(self, datum: date, note: float | None = None) -> None:
        self._datum = datum
        self._note = note

    @property
    def note(self) -> float | None:
        return self._note

    @property
    def datum(self) -> date:
        return self._datum

    @property
    def status(self) -> Pruefungsstatus:
        """Berechnet den Status aus der Note statt ihn zu speichern.
        Keine Note -> OFFEN, Note <= 4.0 -> BESTANDEN, sonst NICHT_BESTANDEN.
        So koennen Note und Status nie widerspruechlich sein."""
        if self._note is None:
            return Pruefungsstatus.OFFEN
        if self._note <= 4.0:
            return Pruefungsstatus.BESTANDEN
        return Pruefungsstatus.NICHT_BESTANDEN