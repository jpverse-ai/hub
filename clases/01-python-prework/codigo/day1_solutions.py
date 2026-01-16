"""Day 1 — SOLUCIONES (Teacher version)

Temas del día:
- Tipos básicos: int, float, str, bool, None
- Operaciones: +, -, *, /, %, //, **
- Strings: strip, lower, upper, replace, split, join
- Casting: int(), float(), str()
- Funciones: def, return, docstrings, type hints
- Condicionales: if / elif / else, operadores lógicos

Consejo docente:
- Haz que el alumno *verbalice*:
  1) Qué entra (inputs),
  2) Qué sale (output),
  3) Reglas (restricciones),
  4) Casos borde (edge cases),
  5) Cómo lo pruebo (asserts).
"""

from __future__ import annotations


def clean_email(raw: str) -> str:
    """Normaliza un email: elimina espacios a los extremos y lo pasa a minúsculas.

    Args:
        raw: texto con posibles espacios y mayúsculas.

    Returns:
        Email normalizado.

    Examples:
        >>> clean_email("  Scraped_Email@Email.com  ")
        'scraped_email@email.com'
    """
    return raw.strip().lower()


def greeting(name: str, age: int) -> str:
    """Construye un saludo con validación de mayoría de edad.

    Reglas:
    - Capitalizar el nombre.
    - Si age >= 18 => mayor de edad, sino menor.

    Examples:
        >>> greeting("jhon", 18)
        'Hola Jhon, eres mayor de edad'
    """
    nice_name = name.strip().capitalize()
    if age >= 18:
        return f"Hola {nice_name}, eres mayor de edad"
    return f"Hola {nice_name}, eres menor de edad"


def check_divisibility(num: int, a: int, b: int) -> bool:
    """Retorna True si num es divisible por a y por b.

    Nota:
    - "Divisible" significa: num % a == 0

    Examples:
        >>> check_divisibility(12, 3, 4)
        True
    """
    return (num % a == 0) and (num % b == 0)


def simple_calculator(tokens: list[str]):
    """Calculadora simple con validación de formato y operador.

    Args:
        tokens: [operando1, operador, operando2]

    Returns:
        - número (int si la operación termina en entero exacto) o float para /
        - o mensajes de error especificados

    Errores:
        - Formato inválido: longitud distinta de 3
        - Operador inválido: no está en + - * / %

    Observación:
        Se convierten operandos a float.
        Para + - * % devolvemos int si el resultado es entero exacto.

    Examples:
        >>> simple_calculator(['1', '+', '1'])
        2
        >>> simple_calculator(['3', '/', '2'])
        1.5
    """
    if len(tokens) != 3:
        return "Please enter valid format: [Operand, Operator, Operand]"

    left_s, op, right_s = tokens
    if op not in {"+", "-", "*", "/", "%"}:
        return "Please enter a valid operator [ +, -, /, *, % ]"

    left = float(left_s)
    right = float(right_s)

    if op == "+":
        res = left + right
    elif op == "-":
        res = left - right
    elif op == "*":
        res = left * right
    elif op == "/":
        # división real
        return left / right
    else:  # %
        res = left % right

    # Si res es entero exacto (ej: 2.0), lo devolvemos como int para el estilo del reto.
    return int(res) if res.is_integer() else res


if __name__ == "__main__":
    # Tests del enunciado
    assert clean_email("  Scraped_Email@Email.com  ") == "scraped_email@email.com"

    assert greeting("jhon", 18) == "Hola Jhon, eres mayor de edad"
    assert greeting("ana", 17) == "Hola Ana, eres menor de edad"
    assert greeting("  MARIA  ", 18) == "Hola Maria, eres mayor de edad"

    assert check_divisibility(12, 3, 4) is True
    assert check_divisibility(12, 5, 3) is False

    assert simple_calculator(["1", "+", "1"]) == 2
    assert simple_calculator(["3", "/", "2"]) == 1.5
    assert simple_calculator(["1", "?", "1"]) == "Please enter a valid operator [ +, -, /, *, % ]"
    assert simple_calculator(["1", "+"]) == "Please enter valid format: [Operand, Operator, Operand]"

    # Tests extra (casos borde)
    assert simple_calculator(["2.5", "*", "2"]) == 5
    assert simple_calculator(["5", "%", "2"]) == 1
    assert simple_calculator(["5", "-", "2"]) == 3

    print("✅ Day 1 SOLUCIONES: OK")
