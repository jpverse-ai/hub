"""Day 5 — SOLUCIONES (Teacher version)

Tema:
- Herencia: Building -> House, Castle
- Override con super()
- Estado extra en subclase
- classmethod + class attribute

"""

from __future__ import annotations


class Building:
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    def floor_area(self) -> float:
        return self.width * self.length

    def __repr__(self) -> str:
        return f"Building(width={self.width}, length={self.length})"


class House(Building):
    """Por ahora, no añade nada. Solo hereda."""


class Castle(Building):
    _CATEGORIES = ["MEDIEVAL", "FANTASY", "HISTORICAL"]

    def __init__(self, width: float, length: float):
        super().__init__(width, length)
        self.butler: str | None = None

    def hire_butler(self, name: str) -> None:
        self.butler = name

    def fire_butler(self) -> None:
        self.butler = None

    def has_a_butler(self) -> bool:
        return self.butler is not None and self.butler.strip() != ""

    def floor_area(self) -> float:
        # usamos super para no duplicar la fórmula
        return super().floor_area() + 300

    @classmethod
    def categories(cls) -> list[str]:
        return cls._CATEGORIES


if __name__ == "__main__":
    b = Building(10, 20)
    assert b.floor_area() == 200

    h = House(10, 20)
    assert h.floor_area() == 200

    c = Castle(10, 20)
    assert c.floor_area() == 500

    assert c.has_a_butler() is False
    c.hire_butler("Alfred")
    assert c.has_a_butler() is True
    c.fire_butler()
    assert c.has_a_butler() is False

    assert "MEDIEVAL" in Castle.categories()
    assert isinstance(Castle.categories(), list)

    print("✅ Day 5 SOLUCIONES: OK")
