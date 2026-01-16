# Day 1 — Python 101 (Tipos, strings, números, variables, funciones y if)
# Referencia: "Python 101" slides (Day1) y objetivos de prework.
#
# Cómo usar este archivo:
# 1) Resuelve cada reto en orden (1 → 4).
# 2) No avances al siguiente hasta que puedas explicar tu solución.
# 3) Ejecuta este archivo y prueba tus funciones con los ejemplos.
#
# Reglas:
# - Escribe código claro (nombres descriptivos).
# - Agrega docstring y tests simples con assert.
# - Evita "hardcodear": usa parámetros.
#
# ------------------------------------------------------------
# RETO 1 (Warm-up) — Limpieza y transformación de strings
# ------------------------------------------------------------
# Crea una función clean_email(raw) que:
# - reciba un string con espacios extra
# - devuelva el email en minúsculas y sin espacios en extremos
#
# Ejemplos:
# clean_email("  Scraped_Email@Email.com  ") -> "scraped_email@email.com"
#
# Pistas:
# - .strip(), .lower()
def clean_email(raw: str) -> str:
    # TODO: implementa
    pass

# ------------------------------------------------------------
# RETO 2 (Beginner) — Interpolación y validación simple
# ------------------------------------------------------------
# Crea una función greeting(name, age) que:
# - name: str
# - age: int
# - devuelva:
#   - "Hola <Name>, eres mayor de edad" si age >= 18
#   - "Hola <Name>, eres menor de edad" si age < 18
#
# Reglas:
# - capitaliza el nombre (primera letra en mayúscula)
#
# Ejemplos:
# greeting("jhon", 18) -> "Hola Jhon, eres mayor de edad"
def greeting(name: str, age: int) -> str:
    # TODO: implementa
    pass

# ------------------------------------------------------------
# RETO 3 (Intermediate) — Módulo (divisibilidad)
# ------------------------------------------------------------
# Escribe check_divisibility(num, a, b) que retorne True si:
# - num es divisible por a
# - y también divisible por b
# Caso contrario False.
#
# Restricción: num, a, b son enteros positivos
#
# Ejemplos:
# check_divisibility(12, 3, 4) -> True
# check_divisibility(12, 5, 3) -> False
def check_divisibility(num: int, a: int, b: int) -> bool:
    # TODO: implementa (usa %)
    pass

# ------------------------------------------------------------
# RETO 4 (Advanced) — Mini-calculadora con validación de formato
# ------------------------------------------------------------
# Crea simple_calculator(tokens) donde tokens es una lista de strings:
#   [operando1, operador, operando2]
# Reglas:
# - Si el formato NO es exactamente longitud 3, devuelve:
#   "Please enter valid format: [Operand, Operator, Operand]"
# - Operadores válidos: +, -, *, /, %
# - Si el operador es inválido:
#   "Please enter a valid operator [ +, -, /, *, % ]"
# - Los operandos SIEMPRE serán numéricos (int o float en string),
#   no necesitas validar eso, solo convertir con float().
# - Para / devuelve float (división real).
#
# Ejemplos:
# simple_calculator(['1', '+', '1']) -> 2
# simple_calculator(['3', '/', '2']) -> 1.5
def simple_calculator(tokens: list[str]):
    # TODO: implementa
    pass


# -------------------------
# Tests rápidos (edítalos)
# -------------------------
if __name__ == "__main__":
    # RETO 1
    assert clean_email("  Scraped_Email@Email.com  ") == "scraped_email@email.com"

    # RETO 2
    assert greeting("jhon", 18) == "Hola Jhon, eres mayor de edad"
    assert greeting("ana", 17) == "Hola Ana, eres menor de edad"

    # RETO 3
    assert check_divisibility(12, 3, 4) is True
    assert check_divisibility(12, 5, 3) is False

    # RETO 4
    assert simple_calculator(["1", "+", "1"]) == 2
    assert simple_calculator(["3", "/", "2"]) == 1.5
    assert simple_calculator(["1", "?", "1"]) == "Please enter a valid operator [ +, -, /, *, % ]"
    assert simple_calculator(["1", "+"]) == "Please enter valid format: [Operand, Operator, Operand]"

    print("✅ Day 1: todos los asserts pasaron (si implementaste TODOs).")
