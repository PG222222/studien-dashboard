from enum import Enum, auto


class Pruefungsstatus(Enum):
    """Gueltige Zustaende einer Pruefungsleistung. Als Enum modelliert,
    damit nur diese drei Werte moeglich sind und keine ungueltigen
    Statuswerte entstehen koennen."""
    OFFEN = auto()
    BESTANDEN = auto()
    NICHT_BESTANDEN = auto()