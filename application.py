from json_repository import JsonRepository
from kennzahlen_service import KennzahlenService
from dashboard_view import DashboardView
from menue import Menue
from dashboard_controller import DashboardController


class Application:
    """Startpunkt und Composition Root: erzeugt und verdrahtet Repository,
    Service, View und Menue. Einzige Stelle, die JsonRepository konkret
    kennt - so bleibt der Rest von der Speicherwahl unabhaengig."""

    def start(self) -> None:
        repository = JsonRepository("data/studiengang.json")
        service = KennzahlenService()
        view = DashboardView()
        controller = DashboardController(repository, service, view)
        menue = Menue(repository, controller)
        menue.starten()