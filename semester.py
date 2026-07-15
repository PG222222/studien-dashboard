class Semester:
    def __init__(self, nummer: int) -> None:
        self._nummer = nummer
        self._module = []

    def modul_zuordnen(self, modul) -> None:
        self._module.append(modul)

    @property
    def nummer(self) -> int:
        return self._nummer

    @property
    def module(self) -> tuple:
        return tuple(self._module)