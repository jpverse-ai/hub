# Day 5 — Inheritance & Advanced OOP (4 retos graduales)
#
# Ejecuta: `python day5_challenges.py`
# Reglas:
# - Implementa en orden
# - NO borres asserts

# ------------------------------------------------------------
# RETO 1 (Warm-up) — Base class Building
# ------------------------------------------------------------
# Crea una clase Building con:
# - atributos: width (int/float), length (int/float)
# - método: floor_area(self) -> int/float  (width * length)
#
# Luego crea 2 subclases:
# - House(Building)
# - Castle(Building)
#
# Nota: por ahora heredan todo (no añadas nada extra aún).
class Building:
    # TODO
    pass

class House(Building):
    # TODO (por ahora puede estar vacía)
    pass

class Castle(Building):
    # TODO (por ahora puede estar vacía)
    pass


# ------------------------------------------------------------
# RETO 2 (Beginner) — Estado extra en Castle: butler
# ------------------------------------------------------------
# Actualiza Castle para que tenga:
# - atributo butler (str | None), por defecto None
# - método has_a_butler(self) -> bool
#     True si butler no es None y no es string vacío
#
# Extra (opcional, recomendado):
# - método hire_butler(self, name: str) -> None  (asigna butler)
# - método fire_butler(self) -> None             (vuelve a None)

# ------------------------------------------------------------
# RETO 3 (Intermediate) — Override + super(): jardín del castillo
# ------------------------------------------------------------
# Sobrescribe floor_area en Castle:
# - Debe devolver super().floor_area() + 300
#   (interpretamos +300 como “jardín / terreno extra”)
#
# Restricción:
# - Debes usar super(), no copies la fórmula width*length.

# ------------------------------------------------------------
# RETO 4 (Advanced) — @classmethod categories
# ------------------------------------------------------------
# Agrega a Castle:
# - atributo de clase (class attribute) _CATEGORIES (lista de strings)
#   ejemplo: ["MEDIEVAL", "FANTASY", "HISTORICAL"]
#
# - método de clase:
#   @classmethod
#   def categories(cls) -> list[str]:
#       return cls._CATEGORIES
#
# Nota:
# - Se llama así: Castle.categories()
# - No requiere instancia.

# -------------------------
# Tests rápidos (NO BORRAR)
# -------------------------
if __name__ == "__main__":
    b = Building(10, 20)
    assert b.floor_area() == 200

    h = House(10, 20)
    assert h.floor_area() == 200

    c = Castle(10, 20)
    # después del reto 3 debe ser 200 + 300 = 500
    assert c.floor_area() == 500

    # reto 2
    assert c.has_a_butler() is False
    c.hire_butler("Alfred")
    assert c.has_a_butler() is True
    c.fire_butler()
    assert c.has_a_butler() is False

    # reto 4
    assert isinstance(Castle.categories(), list)
    assert "MEDIEVAL" in Castle.categories()

    print("✅ Day 5: OK (si implementaste TODOs).")
