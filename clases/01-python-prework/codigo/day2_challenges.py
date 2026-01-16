# Day 2 — Lists & Loops (listas, for, enumerate, comprehensions)
# Basado en: Day2 slides (Lists and loops).
#
# Cómo usar este archivo:
# 1) Resuelve los retos en orden (1 → 4).
# 2) Ejecuta el archivo: `python day2_challenges.py`
# 3) Si un assert falla, NO lo borres: arréglalo.
#
# Reglas de oro:
# - Usa nombres claros.
# - Prefiere funciones puras (sin print dentro, salvo debug temporal).
# - Agrega docstring + type hints.
# - Un reto = un patrón mental.
#
# ------------------------------------------------------------
# RETO 1 (Warm-up) — Acceso seguro por índice
# ------------------------------------------------------------
# Implementa safe_get(items, index, default=None)
# - Devuelve items[index] si existe
# - Si el índice está fuera de rango, devuelve default
#
# Contexto real:
# - Cuando consumes datos de un CSV/JSON, a veces no llega la posición esperada.
#
# Ejemplos:
# safe_get(["a", "b"], 1) -> "b"
# safe_get(["a", "b"], 5, "N/A") -> "N/A"
# safe_get([], 0, "empty") -> "empty"
#
# Pista:
# - Puedes usar try/except IndexError.
def safe_get(items: list, index: int, default=None):
    """Devuelve el elemento en `index` o `default` si el índice no existe."""
    # TODO: implementa
    pass


# ------------------------------------------------------------
# RETO 2 (Beginner) — Lista numerada con enumerate
# ------------------------------------------------------------
# Implementa numbered_list(names)
# - names: lista de strings
# - Devuelve una lista de strings: ["1 - Ben", "2 - Alex", ...]
#
# Reglas:
# - La numeración comienza en 1 (no en 0).
# - Si la lista está vacía, devuelve [].
#
# Ejemplo:
# numbered_list(["Ben", "Alex"]) -> ["1 - Ben", "2 - Alex"]
#
# Pista:
# - enumerate(names) te da (index, value)
def numbered_list(names: list[str]) -> list[str]:
    """Convierte una lista de nombres en una lista numerada (como en un ranking)."""
    # TODO: implementa
    pass


# ------------------------------------------------------------
# RETO 3 (Intermediate) — FizzBuzz en forma de lista
# ------------------------------------------------------------
# Implementa fizz_buzz_list(n)
# - Devuelve una lista con valores desde 1 hasta n (inclusive)
# - Reglas:
#   - múltiplo de 3  -> "Fizz"
#   - múltiplo de 5  -> "Buzz"
#   - múltiplo de 15 -> "FizzBuzz"
#   - sino -> el número (int)
#
# Casos borde:
# - si n <= 0 -> devuelve []
#
# Ejemplo:
# fizz_buzz_list(5) -> [1, 2, "Fizz", 4, "Buzz"]
def fizz_buzz_list(n: int) -> list:
    """Genera la secuencia FizzBuzz desde 1 hasta n."""
    # TODO: implementa
    pass


# ------------------------------------------------------------
# RETO 4 (Advanced) — List comprehension con if/else (transformación)
# ------------------------------------------------------------
# Implementa stylize_fruits(fruits)
# - fruits: lista de strings
# - Devuelve una nueva lista:
#   - si len(fruit) < 6 -> fruit en MAYÚSCULAS
#   - else              -> fruit en minúsculas
#
# Objetivo didáctico:
# - Practicar list comprehension con if/else.
#
# Restricción:
# - Debe hacerse en UNA sola línea usando list comprehension (sin for tradicional).
#
# Ejemplo (del slide):
# fruits = ["Orange", "Mango", "Banana", "Pineapple", "Kiwi"]
# stylize_fruits(fruits) -> ["orange", "MANGO", "banana", "pineapple", "KIWI"]
def stylize_fruits(fruits: list[str]) -> list[str]:
    """Aplica un estilo según longitud del string, usando list comprehension."""
    # TODO: implementa
    pass


# -------------------------
# Tests rápidos (NO BORRAR)
# -------------------------
if __name__ == "__main__":
    # RETO 1
    assert safe_get(["a", "b"], 1) == "b"
    assert safe_get(["a", "b"], 5, "N/A") == "N/A"
    assert safe_get([], 0, "empty") == "empty"

    # RETO 2
    assert numbered_list(["Ben", "Alex"]) == ["1 - Ben", "2 - Alex"]
    assert numbered_list([]) == []

    # RETO 3
    assert fizz_buzz_list(0) == []
    assert fizz_buzz_list(5) == [1, 2, "Fizz", 4, "Buzz"]
    assert fizz_buzz_list(15)[-1] == "FizzBuzz"

    # RETO 4
    fruits = ["Orange", "Mango", "Banana", "Pineapple", "Kiwi"]
    assert stylize_fruits(fruits) == ["orange", "MANGO", "banana", "pineapple", "KIWI"]

    print("✅ Day 2: todos los asserts pasaron (si implementaste TODOs).")
