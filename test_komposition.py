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