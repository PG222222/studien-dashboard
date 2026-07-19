class Semester:
    """Verwaltet zugeordnete Module per Assoziation. Anders als beim
    Studiengang werden Module hier NICHT erzeugt, sondern von aussen
    entgegengenommen - dadurch kann dasselbe Modul mehreren Semestern
    zugeordnet sein (z. B. bei einer Wiederholung)."""
    def __init__(self, nummer: int) -> None:
        self._nummer = nummer
        self._module = []

    def modul_zuordnen(self, modul) -> None:
        """Nimmt ein bestehendes Modul entgegen (Assoziation).

        Bewusster Gegensatz zu semester_anlegen im Studiengang: Da hier
        kein neues Modul erzeugt wird, bleibt die Objektidentitaet
        erhalten und ein Modul kann in mehreren Semestern liegen.
        """
        self._module.append(modul)

    @property
    def nummer(self) -> int:
        return self._nummer

    @property
    def module(self) -> tuple:
        # Tupel schuetzt die interne Liste vor Veraenderung von aussen
        return tuple(self._module)
    
    @property
    def erreichte_ects(self) -> int:
        """Summe der ECTS - nur bestandene Module zaehlen (abgeleitet)."""
        return sum(m.ects for m in self._module if m.bestanden)