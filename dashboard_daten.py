from dataclasses import dataclass, field
from datetime import date


@dataclass
class AnstehendePruefung:
    modul_titel: str
    datum: date
    tage_bis: int


@dataclass
class DashboardDaten:
    rest_tage: int
    im_plan: bool
    aktueller_notendurchschnitt: float | None
    ziel_notendurchschnitt: float
    erreichte_ects: int
    geplante_ects: int
    aktuelles_semester: int
    anstehende_pruefungen: list = field(default_factory=list)