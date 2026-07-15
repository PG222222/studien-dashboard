import json
from datetime import date
from repository import Repository
from studiengang import Studiengang
from modul import Modul


class JsonRepository(Repository):
    def __init__(self, pfad: str) -> None:
        self._pfad = pfad

    def speichern(self, studiengang: Studiengang) -> None:
        daten = {
            "name": studiengang.name,
            "startdatum": studiengang.startdatum.isoformat(),
            "zieldatum_abschluss": studiengang.zieldatum_abschluss.isoformat(),
            "ziel_notendurchschnitt": studiengang.ziel_notendurchschnitt,
            "geplante_ects": studiengang.geplante_ects,
            "semester": [
                {
                    "nummer": s.nummer,
                    "module": [
                        {
                            "titel": m.titel,
                            "ects": m.ects,
                            "pruefungsleistungen": [
                                {
                                    "datum": pl.datum.isoformat(),
                                    "note": pl.note,
                                }
                                for pl in m.pruefungsleistungen
                            ],
                        }
                        for m in s.module
                    ],
                }
                for s in studiengang.semester
            ],
        }
        with open(self._pfad, "w", encoding="utf-8") as f:
            json.dump(daten, f, indent=2, ensure_ascii=False)

    def laden(self) -> Studiengang:
        with open(self._pfad, "r", encoding="utf-8") as f:
            daten = json.load(f)

        studiengang = Studiengang(
            daten["name"],
            date.fromisoformat(daten["startdatum"]),
            date.fromisoformat(daten["zieldatum_abschluss"]),
            daten["ziel_notendurchschnitt"],
            daten["geplante_ects"],
        )

        for s_daten in daten["semester"]:
            semester = studiengang.semester_anlegen(s_daten["nummer"])
            for m_daten in s_daten["module"]:
                modul = Modul(m_daten["titel"], m_daten["ects"])
                semester.modul_zuordnen(modul)
                for pl_daten in m_daten["pruefungsleistungen"]:
                    modul.pruefungsleistung_anlegen(
                        date.fromisoformat(pl_daten["datum"]),
                        pl_daten["note"],
                    )

        return studiengang