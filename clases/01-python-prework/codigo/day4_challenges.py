# Day 4 — Classes (OOP) (retos graduales, 4 por día)
#
# Cómo usar:
# - Implementa en orden (1 → 4)
# - Ejecuta: `python day4_challenges.py`
# - NO borres asserts: arregla tu código hasta que pasen.
#
# Meta docente:
# - Aprender a modelar entidades (estado + comportamiento)
# - Entender self, __init__, métodos que mutan vs métodos que calculan

# ------------------------------------------------------------
# RETO 1 (Warm-up) — Clase Car (estado + método mutador)
# ------------------------------------------------------------
# Crea una clase Car con:
# - Atributos:
#   - brand: str
#   - model: str
#   - engine_started: bool (por defecto False)
#
# - Métodos:
#   - start_engine(self) -> None   (cambia engine_started a True)
#   - stop_engine(self) -> None    (cambia engine_started a False)
#   - is_engine_started(self) -> bool (devuelve el estado)
#
# Ejemplo:
# car = Car("Toyota", "Corolla")
# car.is_engine_started() -> False
# car.start_engine()
# car.is_engine_started() -> True
class Car:
    # TODO: implementa
    pass


# ------------------------------------------------------------
# RETO 2 (Beginner) — Clase Castle (métodos de “texto”)
# ------------------------------------------------------------
# Crea una clase Castle con:
# - Atributos: name (str), ruler (str)
#
# - Métodos:
#   - ruler_name(self) -> str
#       retorna: "The ruler is <ruler>"
#   - castle_details(self) -> str
#       retorna: "The castle is called <name> and the ruler is <ruler>"
class Castle:
    # TODO: implementa
    pass


# ------------------------------------------------------------
# RETO 3 (Intermediate) — Clase Student (cálculo de riqueza)
# ------------------------------------------------------------
# Crea una clase Student con:
# - Atributos:
#   - name: str
#   - fives: int  (cantidad de billetes de 5)
#   - tens: int   (cantidad de billetes de 10)
#   - twenties: int (cantidad de billetes de 20)
#
# - Métodos:
#   - wealth(self) -> int
#       total = 5*fives + 10*tens + 20*twenties
#   - compare(self, other: "Student") -> str
#       retorna el nombre del estudiante con más riqueza.
#       si empatan, retorna "Equal"
#
# Ejemplo:
# a = Student("Ana", fives=1, tens=0, twenties=0)  # 5
# b = Student("Beto", fives=0, tens=1, twenties=0) # 10
# a.compare(b) -> "Beto"
class Student:
    # TODO: implementa
    pass


# ------------------------------------------------------------
# RETO 4 (Advanced) — Ranking de riqueza (ordenamiento + OOP)
# ------------------------------------------------------------
# Agrega a Student un método:
#   advanced_compare(self, others: list["Student"]) -> list[str]
#
# Reglas:
# - Construye una lista con [self] + others
# - Ordena por wealth() DESC
# - Si hay empate de wealth, ordena por name ASC
# - Devuelve SOLO los nombres en orden
#
# Ejemplo:
# a (10), b (5), c (10)
# advanced_compare([b,c]) -> ["Ana", "Carla", "Beto"]  # (Ana 10, Carla 10, Beto 5) y tie-break por nombre
#
# Pista:
# - Usa sorted(..., key=..., reverse=...) o una key compuesta.
# - Key compuesta: key=lambda s: (-s.wealth(), s.name)
#   (negativo para ordenar DESC sin reverse)
#
# Nota:
# - No crees una nueva clase; se agrega al Student.
# - En el reto 3 ya tienes wealth(), úsalo.
# (En este archivo no puedes “forzar” al alumno a editar la clase; pero en evaluación sí.)
#
# -------------------------
# Tests rápidos (NO BORRAR)
# -------------------------
if __name__ == "__main__":
    # RETO 1
    car = Car("Toyota", "Corolla")
    assert car.brand == "Toyota"
    assert car.model == "Corolla"
    assert car.is_engine_started() is False
    car.start_engine()
    assert car.is_engine_started() is True
    car.stop_engine()
    assert car.is_engine_started() is False

    # RETO 2
    c = Castle("Winterfell", "Ned Stark")
    assert c.ruler_name() == "The ruler is Ned Stark"
    assert c.castle_details() == "The castle is called Winterfell and the ruler is Ned Stark"

    # RETO 3
    a = Student("Ana", fives=1, tens=0, twenties=0)   # 5
    b = Student("Beto", fives=0, tens=1, twenties=0)  # 10
    e = Student("Ema", fives=1, tens=0, twenties=0)   # 5
    assert a.wealth() == 5
    assert b.wealth() == 10
    assert a.compare(b) == "Beto"
    assert a.compare(e) == "Equal"

    # RETO 4
    # Nota: para que pase, el método advanced_compare debe existir en Student
    assert a.advanced_compare([b, e]) == ["Beto", "Ana", "Ema"]

    print("✅ Day 4: OK (si implementaste TODOs).")
