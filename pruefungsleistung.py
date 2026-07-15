from datetime import date
from pruefungsstatus import Pruefungsstatus


class Pruefungsleistung:
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
        if self._note is None:
            return Pruefungsstatus.OFFEN
        if self._note <= 4.0:
            return Pruefungsstatus.BESTANDEN
        return Pruefungsstatus.NICHT_BESTANDEN