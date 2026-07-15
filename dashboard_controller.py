from repository import Repository
from kennzahlen_service import KennzahlenService
from dashboard_view import DashboardView


class DashboardController:
    def __init__(self, repository: Repository,
                 service: KennzahlenService,
                 view: DashboardView) -> None:
        self._repository = repository
        self._service = service
        self._view = view

    def dashboard_anzeigen(self) -> None:
        studiengang = self._repository.laden()
        daten = self._service.berechnen(studiengang)
        self._view.rendern(daten)