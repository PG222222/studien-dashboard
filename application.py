from json_repository import JsonRepository
from kennzahlen_service import KennzahlenService
from dashboard_view import DashboardView
from dashboard_controller import DashboardController


class Application:
    def start(self) -> None:
        repository = JsonRepository("data/studiengang.json")
        service = KennzahlenService()
        view = DashboardView()
        controller = DashboardController(repository, service, view)
        controller.dashboard_anzeigen()