from repository import Repository
from dashboard_controller import DashboardController


class Menue:
    """Einfache Konsolen-Menuefuehrung. Erlaubt Anzeigen des Dashboards,
    Eintragen von Noten und Hinzufuegen von Modulen und speichert
    Aenderungen ueber das Repository."""

    def __init__(self, repository: Repository,
                 controller: DashboardController) -> None:
        self._repository = repository
        self._controller = controller
        self._studiengang = repository.laden()

    def starten(self) -> None:
        while True:
            print("\n--- Studien-Dashboard ---")
            print("[1] Dashboard anzeigen")
            print("[2] Note eintragen")
            print("[3] Modul hinzufuegen")
            print("[0] Beenden")
            auswahl = input("Auswahl: ").strip()

            if auswahl == "1":
                self._dashboard_zeigen()
            elif auswahl == "2":
                self._note_eintragen()
            elif auswahl == "3":
                self._modul_hinzufuegen()
            elif auswahl == "0":
                print("Programm beendet.")
                break
            else:
                print("Ungueltige Auswahl.")

    def _dashboard_zeigen(self) -> None:
        self._controller.dashboard_anzeigen()

    def _note_eintragen(self) -> None:
        # Alle Module mit Nummer auflisten, damit der Nutzer eins waehlen kann
        module = self._alle_module()
        if not module:
            print("Keine Module vorhanden.")
            return

        print("\nWelches Modul?")
        for i, modul in enumerate(module, start=1):
            print(f"  [{i}] {modul.titel}")

        wahl = input("Modul-Nummer: ").strip()
        if not wahl.isdigit() or not (1 <= int(wahl) <= len(module)):
            print("Ungueltige Modul-Nummer.")
            return
        modul = module[int(wahl) - 1]

        note_text = input("Note (z. B. 1.7): ").strip().replace(",", ".")
        try:
            note = float(note_text)
        except ValueError:
            print("Das ist keine gueltige Note.")
            return

        # Neue Pruefungsleistung ueber die Factory-Methode des Moduls anlegen
        from datetime import date
        modul.pruefungsleistung_anlegen(date.today(), note)
        self._repository.speichern(self._studiengang)
        print(f"Note {note} fuer '{modul.titel}' gespeichert.")

    def _alle_module(self) -> list:
        module = []
        for semester in self._studiengang.semester:
            for modul in semester.module:
                module.append(modul)
        return module

    def _modul_hinzufuegen(self) -> None:
        semester_liste = list(self._studiengang.semester)
        if not semester_liste:
            print("Kein Semester vorhanden.")
            return

        print("\nZu welchem Semester?")
        for i, semester in enumerate(semester_liste, start=1):
            print(f"  [{i}] {semester.nummer}. Semester")

        wahl = input("Semester-Nummer: ").strip()
        if not wahl.isdigit() or not (1 <= int(wahl) <= len(semester_liste)):
            print("Ungueltige Semester-Nummer.")
            return
        semester = semester_liste[int(wahl) - 1]

        titel = input("Modultitel: ").strip()
        if not titel:
            print("Titel darf nicht leer sein.")
            return

        ects_text = input("ECTS: ").strip()
        if not ects_text.isdigit():
            print("ECTS muss eine ganze Zahl sein.")
            return
        ects = int(ects_text)

        # Modul erzeugen und dem Semester zuordnen (Assoziation)
        from modul import Modul
        modul = Modul(titel, ects)
        semester.modul_zuordnen(modul)
        self._repository.speichern(self._studiengang)
        print(f"Modul '{titel}' ({ects} ECTS) hinzugefuegt.")    