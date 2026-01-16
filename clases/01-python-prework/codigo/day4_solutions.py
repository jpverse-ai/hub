"""Day 4 — SOLUCIONES (Teacher version)

Tema:
- Clases (estado + comportamiento)
- self, __init__
- Métodos que mutan estado vs métodos que calculan
- Ordenamiento de objetos con key

"""

from __future__ import annotations


class Car:
    """Modelo simple de un carro con estado: engine_started."""

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.engine_started = False

    def start_engine(self) -> None:
        self.engine_started = True

    def stop_engine(self) -> None:
        self.engine_started = False

    def is_engine_started(self) -> bool:
        return self.engine_started

    def __repr__(self) -> str:
        status = "started" if self.engine_started else "stopped"
        return f"Car(brand={self.brand!r}, model={self.model!r}, engine={status})"


class Castle:
    """Modelo simple de un castillo con nombre y gobernante."""

    def __init__(self, name: str, ruler: str):
        self.name = name
        self.ruler = ruler

    def ruler_name(self) -> str:
        return f"The ruler is {self.ruler}"

    def castle_details(self) -> str:
        return f"The castle is called {self.name} and the ruler is {self.ruler}"


class Student:
    """Un estudiante con billetes en la billetera."""

    def __init__(self, name: str, fives: int = 0, tens: int = 0, twenties: int = 0):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def wealth(self) -> int:
        return 5 * self.fives + 10 * self.tens + 20 * self.twenties

    def compare(self, other: "Student") -> str:
        my_w = self.wealth()
        other_w = other.wealth()
        if my_w > other_w:
            return self.name
        if other_w > my_w:
            return other.name
        return "Equal"

    def advanced_compare(self, others: list["Student"]) -> list[str]:
        everyone = [self] + list(others)
        ranked = sorted(everyone, key=lambda s: (-s.wealth(), s.name))
        return [s.name for s in ranked]

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, wealth={self.wealth()})"


if __name__ == "__main__":
    car = Car("Toyota", "Corolla")
    assert car.is_engine_started() is False
    car.start_engine()
    assert car.is_engine_started() is True
    car.stop_engine()
    assert car.is_engine_started() is False

    c = Castle("Winterfell", "Ned Stark")
    assert c.ruler_name() == "The ruler is Ned Stark"
    assert c.castle_details() == "The castle is called Winterfell and the ruler is Ned Stark"

    a = Student("Ana", fives=1, tens=0, twenties=0)   # 5
    b = Student("Beto", fives=0, tens=1, twenties=0)  # 10
    e = Student("Ema", fives=1, tens=0, twenties=0)   # 5
    assert a.wealth() == 5
    assert b.wealth() == 10
    assert a.compare(b) == "Beto"
    assert a.compare(e) == "Equal"
    assert a.advanced_compare([b, e]) == ["Beto", "Ana", "Ema"]

    print("✅ Day 4 SOLUCIONES: OK")
