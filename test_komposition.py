from datetime import date
from studiengang import Studiengang

sg = Studiengang("Cyber Security", date(2025, 7, 1),
                 date(2027, 12, 1), 1.9, 180)

s1 = sg.semester_anlegen(1)
s2 = sg.semester_anlegen(2)

print("Semester angelegt:", s1, s2)

print("Anzahl Semester:", len(sg.semester))

# Versuch, von außen etwas anzuhängen:
sg.semester.append("Schummel-Semester")

print("Anzahl danach:", len(sg.semester))