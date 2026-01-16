"""Day 2 — SOLUCIONES (Teacher version)

Temas del día:
- Listas: indexación, modificación, append/remove/pop/del, len, sort
- Bucles: for, range, enumerate
- Transformaciones: list comprehension (con y sin condiciones)

Consejo docente:
- Para cada reto, haz que el alumno diga:
  1) Inputs,
  2) Output,
  3) Reglas,
  4) Casos borde,
  5) Cómo se prueba.

"""

from __future__ import annotations


def safe_get(items: list, index: int, default=None):
    """Acceso seguro a una lista por índice.

    Args:
        items: lista cualquiera
        index: posición a acceder (puede ser negativa también)
        default: valor a retornar si index no existe

    Returns:
        items[index] si existe; si no, default.

    Examples:
        >>> safe_get(["a", "b"], 1)
        'b'
        >>> safe_get(["a", "b"], 5, "N/A")
        'N/A'
    """
    try:
        return items[index]
    except IndexError:
        return default


def numbered_list(names: list[str]) -> list[str]:
    """Devuelve una lista numerada desde 1, usando enumerate.

    Examples:
        >>> numbered_list(["Ben", "Alex"])
        ['1 - Ben', '2 - Alex']
    """
    # Usamos index+1 porque el humano suele contar desde 1.
    return [f"{index + 1} - {name}" for index, name in enumerate(names)]


def fizz_buzz_list(n: int) -> list:
    """Genera FizzBuzz desde 1 hasta n (inclusive) en una lista.

    Reglas:
    - 15: FizzBuzz
    - 3: Fizz
    - 5: Buzz
    - otro: número

    Casos borde:
    - n <= 0 => []

    Examples:
        >>> fizz_buzz_list(5)
        [1, 2, 'Fizz', 4, 'Buzz']
    """
    if n <= 0:
        return []

    out: list = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(i)
    return out


def stylize_fruits(fruits: list[str]) -> list[str]:
    """Transforma frutas con list comprehension + if/else.

    Reglas:
    - len(fruit) < 6 => upper
    - else => lower

    Examples:
        >>> stylize_fruits(["Orange", "Mango", "Banana", "Pineapple", "Kiwi"])
        ['orange', 'MANGO', 'banana', 'pineapple', 'KIWI']
    """
    return [fruit.upper() if len(fruit) < 6 else fruit.lower() for fruit in fruits]


if __name__ == "__main__":
    assert safe_get(["a", "b"], 1) == "b"
    assert safe_get(["a", "b"], 5, "N/A") == "N/A"
    assert safe_get([], 0, "empty") == "empty"
    assert safe_get(["a"], -1) == "a"  # índice negativo válido

    assert numbered_list(["Ben", "Alex"]) == ["1 - Ben", "2 - Alex"]
    assert numbered_list([]) == []

    assert fizz_buzz_list(0) == []
    assert fizz_buzz_list(1) == [1]
    assert fizz_buzz_list(5) == [1, 2, "Fizz", 4, "Buzz"]
    seq = fizz_buzz_list(15)
    assert seq[2] == "Fizz"
    assert seq[4] == "Buzz"
    assert seq[-1] == "FizzBuzz"

    fruits = ["Orange", "Mango", "Banana", "Pineapple", "Kiwi"]
    assert stylize_fruits(fruits) == ["orange", "MANGO", "banana", "pineapple", "KIWI"]

    print("✅ Day 2 SOLUCIONES: OK")
