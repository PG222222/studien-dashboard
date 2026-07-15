from datetime import date
from studiengang import Studiengang
from modul import Modul
from json_repository import JsonRepository

# Kleinen Studiengang aufbauen
studium = Studiengang("Cyber Security", date(2025, 7, 1),
                      date(2027, 12, 1), 1.9, 180)

sem1 = studium.semester_anlegen(1)
m1 = Modul("Mathematik", 5)
m1.pruefungsleistung_anlegen(date(2025, 9, 1), 2.0)
sem1.modul_zuordnen(m1)

# Speichern
repo = JsonRepository("data/studiengang.json")
repo.speichern(studium)

print("Gespeichert nach data/studiengang.json")

# Wieder laden und pruefen
geladen = repo.laden()

print("--- Laden-Test ---")
print("Name:", geladen.name)
print("Erreichte ECTS gesamt:", geladen.erreichte_ects_gesamt)
print("Notendurchschnitt:", geladen.aktueller_notendurchschnitt)
print("Anzahl Semester:", len(geladen.semester))