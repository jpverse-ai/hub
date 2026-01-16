# Day 3 — Dictionaries (dict, items/values, get, dict comprehensions)
# Basado en: Day3 slides (Dictionaries) y prework (calorie counter / weather forecast).
#
# Cómo usar este archivo:
# 1) Implementa las funciones en orden (1 → 4).
# 2) Ejecuta: `python day3_challenges.py`
# 3) Si un assert falla, corrige tu código (no borres asserts).
#
# ------------------------------------------------------------
# RETO 1 (Warm-up) — Listas a dict con zip + dict comprehension
# ------------------------------------------------------------
# Implementa build_age_dict(names, ages)
# - names y ages tienen la misma longitud
# - Devuelve: {name: age}
#
# Ejemplo (similar al slide):
# build_age_dict(["Peter","Mary"], [24,25]) -> {"Peter": 24, "Mary": 25}
def build_age_dict(names: list[str], ages: list[int]) -> dict[str, int]:
    """Construye un diccionario {nombre: edad} usando zip."""
    # TODO: implementa
    pass


# ------------------------------------------------------------
# RETO 2 (Beginner) — Contador de palabras (patrón contador)
# ------------------------------------------------------------
# Implementa count_words(sentence)
# - sentence: str
# - devuelve un dict con conteo de cada palabra
# - normaliza a minúsculas
#
# Reglas:
# - Separa por espacios (split)
# - Para mantenerlo simple, no eliminamos puntuación interna.
#
# Ejemplo:
# count_words("Hola hola mundo") -> {"hola": 2, "mundo": 1}
def count_words(sentence: str) -> dict[str, int]:
    """Cuenta palabras (case-insensitive)."""
    # TODO: implementa (usa dict.get para defaults)
    pass


# ------------------------------------------------------------
# RETO 3 (Intermediate) — Calorie Counter (dict + validación)
# ------------------------------------------------------------
# Menú base (del prework de calorie counter):
MENU: dict[str, int] = {
    "Cheese Burger": 290,
    "Big Mac": 590,
    "McChicken": 430,
    "French Fries": 340,
    "Salad": 100,
    "Coca Cola": 160,
    "Sprite": 170,
}

# Implementa calories_counter(orders)
# - orders: lista de strings (platos)
# - devuelve el total (int) de calorías
#
# Regla de validación:
# - Si un item NO está en MENU -> devuelve "<item> not found"
#
# Ejemplo:
# calories_counter(["Big Mac", "Salad"]) -> 690
# calories_counter(["Pizza"]) -> "Pizza not found"
def calories_counter(orders: list[str]) -> int | str:
    """Suma calorías de items individuales. Si no existe un item, retorna '<item> not found'."""
    # TODO: implementa (usa MENU.get)
    pass


# ------------------------------------------------------------
# RETO 4 (Advanced) — Weather forecast (navegar dict grande)
# ------------------------------------------------------------
# Inspiración: prework de OpenWeatherMap forecast.
# - El response tiene una key 'city' con el nombre
# - Y una key 'list' con pronósticos cada 3 horas.
# - Debemos devolver el pronóstico de MAÑANA a las 06:00:00
#
# Formato de retorno (según el prework):
# "The weather in <city> tomorrow is <forecast>"
#
# Tips:
# - Usa datetime para construir la fecha de mañana como 'YYYY-MM-DD'
# - Recorre response['list'] y busca el elemento cuyo 'dt_txt' contenga:
#   f"{tomorrow} 06:00:00"
# - El forecast está en: item['weather'][0]['description']
# - Usa get() para evitar KeyError y un return defensivo si no encuentras.
def weather_forecast(response: dict) -> str:
    """Retorna el pronóstico de mañana a las 06:00am, en formato texto."""
    # TODO: implementa
    pass


# -------------------------
# Tests rápidos (NO BORRAR)
# -------------------------
if __name__ == "__main__":
    # RETO 1
    assert build_age_dict(["Peter", "Mary"], [24, 25]) == {"Peter": 24, "Mary": 25}
    assert build_age_dict([], []) == {}

    # RETO 2
    assert count_words("Hola hola mundo") == {"hola": 2, "mundo": 1}
    assert count_words("") == {}

    # RETO 3
    assert calories_counter(["Big Mac", "Salad"]) == 690
    assert calories_counter(["Pizza"]) == "Pizza not found"

    # RETO 4 (test dinámico: construimos un response para mañana)
    from datetime import date, timedelta
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    fake_response = {
        "city": {"name": "Lima"},
        "list": [
            {"dt_txt": f"{tomorrow} 03:00:00", "weather": [{"description": "cloudy"}]},
            {"dt_txt": f"{tomorrow} 06:00:00", "weather": [{"description": "light rain"}]},
            {"dt_txt": f"{tomorrow} 09:00:00", "weather": [{"description": "sunny"}]},
        ],
    }
    assert weather_forecast(fake_response) == "The weather in Lima tomorrow is light rain"

    print("✅ Day 3: todos los asserts pasaron (si implementaste TODOs).")
