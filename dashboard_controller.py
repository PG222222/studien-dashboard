from repository import Repository
from kennzahlen_service import KennzahlenService
from dashboard_view import DashboardView


class DashboardController:
    """Steuert den Ablauf: laedt den Studiengang ueber das Repository,
    laesst den Service rechnen und die View anzeigen. Kennt nur die
    abstrakte Repository-Schnittstelle, nicht die konkrete Speicherklasse."""
    def __init__(self, repository: Repository,
                 service: KennzahlenService,
                 view: DashboardView) -> None:
        self._repository = repository
        self._service = service
        self._view = view

    def dashboard_anzeigen(self) -> None:
        """Fuehrt den Ablauf einmal aus: laden, berechnen, anzeigen."""
        studiengang = self._repository.laden()
        daten = self._service.berechnen(studiengang)
        self._view.rendern(daten)