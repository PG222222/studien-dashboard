from dataclasses import dataclass, field
from datetime import date


@dataclass
class AnstehendePruefung:
    """Anzeigeobjekt fuer eine anstehende Pruefung (bereits mit Modultitel
    und Tagen bis zum Termin, fertig zur Darstellung)."""
    modul_titel: str
    datum: date
    tage_bis: int


@dataclass
class DashboardDaten:
    """Reines Transportobjekt vom Service zur View. Enthaelt nur fertig
    berechnete Werte und rechnet selbst nichts."""
    rest_tage: int
    im_plan: bool
    aktueller_notendurchschnitt: float | None
    ziel_notendurchschnitt: float
    erreichte_ects: int
    geplante_ects: int
    aktuelles_semester: int
    anstehende_pruefungen: list = field(default_factory=list)