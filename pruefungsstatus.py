from enum import Enum, auto


class Pruefungsstatus(Enum):
    OFFEN = auto()
    BESTANDEN = auto()
    NICHT_BESTANDEN = auto()