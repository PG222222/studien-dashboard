from rich.console import Console, Group
from rich.panel import Panel
from rich.columns import Columns
from dashboard_daten import DashboardDaten


class DashboardView:
    """Stellt die DashboardDaten mit rich in der Konsole dar. Enthaelt
    nur Darstellungslogik, keine Berechnung."""
    def __init__(self) -> None:
        self._console = Console()

    def rendern(self, daten: DashboardDaten) -> None:
        inhalt = Group(
            self._obere_reihe(daten),
            self._fortschritt(daten),
            self._anstehende(daten),
        )
        rahmen = Panel(
            inhalt,
            title="[bold]Mein Studien-Dashboard[/bold]",
            subtitle="B.Sc. Cyber Security",
            width=100,
            padding=(1, 2),
        )
        self._console.print(rahmen)

    def _obere_reihe(self, daten: DashboardDaten) -> Columns:
        # Ziel 1: Abschluss
        plan_text = "im Plan" if daten.im_plan else "im Verzug"
        plan_farbe = "green" if daten.im_plan else "red"
        ziel1 = Panel(
            f"noch [bold]{daten.rest_tage}[/bold] Tage\n[{plan_farbe}]{plan_text}[/{plan_farbe}]",
            title="Ziel 1: Abschluss",
        )

        # Ziel 2: Notenschnitt
        if daten.aktueller_notendurchschnitt is None:
            schnitt_text = "noch keine Note"
            schnitt_farbe = "white"
        else:
            im_ziel = daten.aktueller_notendurchschnitt <= daten.ziel_notendurchschnitt
            schnitt_farbe = "green" if im_ziel else "red"
            schnitt_text = f"[{schnitt_farbe}]{daten.aktueller_notendurchschnitt:.1f}[/{schnitt_farbe}] / Ziel ≤ {daten.ziel_notendurchschnitt}"
        ziel2 = Panel(schnitt_text, title="Ziel 2: Notenschnitt")

        # Ziel 3: ECTS
        prozent = round(daten.erreichte_ects / daten.geplante_ects * 100)
        ziel3 = Panel(
            f"[bold]{daten.erreichte_ects}[/bold] / {daten.geplante_ects}\n{prozent} % geschafft",
            title="Ziel 3: ECTS",
        )

        return Columns([ziel1, ziel2, ziel3], equal=True, expand=True, width=28)
    
    def _fortschritt(self, daten: DashboardDaten) -> Panel:
        prozent = daten.erreichte_ects / daten.geplante_ects
        breite = 90
        gefuellt = round(prozent * breite)
        balken = "█" * gefuellt + "░" * (breite - gefuellt)
        text = (
            f"ECTS-Fortschritt{' ' * 60}{daten.erreichte_ects} von {daten.geplante_ects} ECTS\n"
            f"{balken}  {round(prozent * 100)} %\n"
            f"[dim]{f'{daten.aktuelles_semester}. Semester'.center(breite)}[/dim]"
        )
        return Panel(text)
    
    def _anstehende(self, daten: DashboardDaten) -> Panel:
        if not daten.anstehende_pruefungen:
            return Panel("Keine anstehenden Pruefungen", title="Anstehende Pruefungen")
        zeilen = []
        for a in daten.anstehende_pruefungen:
            farbe = "red" if a.tage_bis <= 7 else "white"
            zeilen.append(
                f"{a.modul_titel:<30} [{farbe}]in {a.tage_bis} Tagen[/{farbe}]"
            )
        return Panel("\n".join(zeilen), title="Anstehende Pruefungen")