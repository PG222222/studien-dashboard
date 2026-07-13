from datetime import date


class Studiengang:
    def __init__(self, name: str, startdatum: date, zieldatum_abschluss: date,
                 ziel_notendurchschnitt: float, geplante_ects: int) -> None:
        self._name = name
        self._startdatum = startdatum