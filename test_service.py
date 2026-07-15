from datetime import date, timedelta
from studiengang import Studiengang
from modul import Modul
from kennzahlen_service import KennzahlenService

# Studiengang mit einer anstehenden Pruefung in der Zukunft
studium = Studiengang("Cyber Security", date(2025, 7, 1),
                      date(2027, 12, 1), 1.9, 180)

sem1 = studium.semester_anlegen(1)

m1 = Modul("Mathematik", 5)
m1.pruefungsleistung_anlegen(date(2025, 9, 1), 2.0)   # schon bewertet
sem1.modul_zuordnen(m1)

m2 = Modul("Pentesting", 5)
# anstehende Pruefung: heute + 5 Tage, noch keine Note
m2.pruefungsleistung_anlegen(date.today() + timedelta(days=5))
sem1.modul_zuordnen(m2)

# Service laufen lassen
service = KennzahlenService()
daten = service.berechnen(studium)

print("--- Service-Test ---")
print("Resttage bis Abschluss:", daten.rest_tage)
print("Im Plan:", daten.im_plan)
print("Notendurchschnitt:", daten.aktueller_notendurchschnitt)
print("ECTS:", daten.erreichte_ects, "von", daten.geplante_ects)
print("Aktuelles Semester:", daten.aktuelles_semester)
print("Anstehende Pruefungen:")
for a in daten.anstehende_pruefungen:
    print("  ", a.modul_titel, "in", a.tage_bis, "Tagen")