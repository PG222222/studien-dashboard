class Modul:
    def __init__(self, titel: str, ects: int) -> None:
        self._titel = titel
        self._ects = ects

    @property
    def titel(self) -> str:
        return self._titel

    @property
    def ects(self) -> int:
        return self._ects