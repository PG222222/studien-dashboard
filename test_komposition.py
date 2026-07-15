from datetime import date
from studiengang import Studiengang

sg = Studiengang("Cyber Security", date(2025, 7, 1),
                 date(2027, 12, 1), 1.9, 180)

s1 = sg.semester_anlegen(1)
s2 = sg.semester_anlegen(2)

print("Semester angelegt:", s1, s2)

print("Anzahl Semester:", len(sg.semester))

# Versuch, von außen etwas anzuhängen:
try:
        sg.semester.append("Schummel-Semester")
        print("Anhaengen von aussen hat geklappt - schlecht!")
except AttributeError:
        print("Anhaengen von aussen wurde verhindert - gut!")

print("Anzahl danach:", len(sg.semester))

from modul import Modul

# Assoziation: dasselbe Modul in zwei Semestern
oop = Modul("OOP mit Python", 5)
s1.modul_zuordnen(oop)
s2.modul_zuordnen(oop)

print("Gleiches Objekt in beiden Semestern:",
      s1.module[0] is oop and s2.module[0] is oop)

from pruefungsleistung import Pruefungsleistung
from datetime import date

print("--- Pruefungsstatus-Test ---")
p_offen = Pruefungsleistung(date(2026, 8, 1))            # keine Note
p_gut = Pruefungsleistung(date(2026, 3, 1), 1.7)         # bestanden
p_schlecht = Pruefungsleistung(date(2026, 3, 1), 4.7)    # nicht bestanden

print("Ohne Note:", p_offen.status)
print("Note 1.7:", p_gut.status)
print("Note 4.7:", p_schlecht.status)

print("--- Modul bestanden-Test ---")
mathe = Modul("Statistik", 5)
print("Vor Pruefung bestanden?", mathe.bestanden)   # False erwartet

mathe.pruefungsleistung_anlegen(date(2026, 2, 1), 2.3)
print("Nach Note 2.3 bestanden?", mathe.bestanden)   # True erwartet

print("--- Gesamtmodell-Test ---")
studium = Studiengang("Cyber Security", date(2025, 7, 1),
                      date(2027, 12, 1), 1.9, 180)

sem1 = studium.semester_anlegen(1)

m1 = Modul("Mathematik", 5)
m1.pruefungsleistung_anlegen(date(2025, 9, 1), 2.0)
sem1.modul_zuordnen(m1)

m2 = Modul("Programmierung", 5)
m2.pruefungsleistung_anlegen(date(2025, 10, 1), 1.0)
sem1.modul_zuordnen(m2)

print("Erreichte ECTS gesamt:", studium.erreichte_ects_gesamt)
print("Notendurchschnitt:", studium.aktueller_notendurchschnitt)