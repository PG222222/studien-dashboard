from datetime import date
from studiengang import Studiengang
from pruefungsstatus import Pruefungsstatus
from dashboard_daten import DashboardDaten, AnstehendePruefung


class KennzahlenService:
    """Berechnet aus dem Studiengang die fertigen Anzeige-Werte fuers
    Dashboard. Bewusst von den Entity-Klassen und der View getrennt,
    damit die View selbst nichts mehr rechnen muss."""
    def berechnen(self, studiengang: Studiengang) -> DashboardDaten:
        """Ermittelt Resttage, Notenschnitt, ECTS-Fortschritt und die
        Liste der anstehenden Pruefungen und buendelt sie in DashboardDaten."""
        heute = date.today()
        rest_tage = (studiengang.zieldatum_abschluss - heute).days
        im_plan = rest_tage >= 0

        aktuelles_semester = len(studiengang.semester)

        # Nur offene Pruefungen in der Zukunft, sortiert nach Naehe 
        # das ergibt die Liste "Anstehende Pruefungen" auf dem Dashboard.
        anstehende = []
        for semester in studiengang.semester:
            for modul in semester.module:
                for pl in modul.pruefungsleistungen:
                    if pl.status == Pruefungsstatus.OFFEN and pl.datum >= heute:
                        anstehende.append(AnstehendePruefung(
                            modul_titel=modul.titel,
                            datum=pl.datum,
                            tage_bis=(pl.datum - heute).days,
                        ))
        anstehende.sort(key=lambda a: a.tage_bis)

        return DashboardDaten(
            rest_tage=rest_tage,
            im_plan=im_plan,
            aktueller_notendurchschnitt=studiengang.aktueller_notendurchschnitt,
            ziel_notendurchschnitt=studiengang.ziel_notendurchschnitt,
            erreichte_ects=studiengang.erreichte_ects_gesamt,
            geplante_ects=studiengang.geplante_ects,
            aktuelles_semester=aktuelles_semester,
            anstehende_pruefungen=anstehende,
        )