from datetime import date, timedelta
from studiengang import Studiengang
from modul import Modul
from kennzahlen_service import KennzahlenService
from dashboard_view import DashboardView

studium = Studiengang("Cyber Security", date(2025, 7, 1),
                      date(2027, 12, 1), 1.9, 180)
sem1 = studium.semester_anlegen(1)

m1 = Modul("Mathematik", 5)
m1.pruefungsleistung_anlegen(date(2025, 9, 1), 2.0)
sem1.modul_zuordnen(m1)

m2 = Modul("Pentesting", 5)
m2.pruefungsleistung_anlegen(date.today() + timedelta(days=5))
sem1.modul_zuordnen(m2)

daten = KennzahlenService().berechnen(studium)
DashboardView().rendern(daten)