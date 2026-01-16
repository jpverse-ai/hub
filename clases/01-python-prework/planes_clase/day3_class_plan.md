# Clase Día 3 — Diccionarios (dict) con MUCHO detalle

> Basado en: *Day3 slides — Dictionaries* (definición, CRUD, iteración, `get`, dict comprehension).

## Idea central (explicación “profe”)
Una lista es excelente para **secuencias**. Pero cuando hay relación “clave → valor”
(nombre → edad, SKU → precio, país → población), un `dict` es el “mapa” perfecto.

En el slide se muestra el problema de mantener 2 listas paralelas (`students` y `student_ages`)
y luego la solución natural: un diccionario `students_age["Peter"]`.

---

## Objetivos del día
Al final el alumno puede:
1. Definir diccionarios y explicar “keys únicas”
2. Leer valores: `d[key]` vs `d.get(key, default)` y cuándo usar cada uno
3. Crear/actualizar/borrar pares clave-valor (`d[k]=v`, `del d[k]`)
4. Iterar `for key in d`, `d.values()`, `d.items()`
5. Convertir listas a dict usando **dict comprehension** con `zip`

---

## Agenda sugerida (100 min)
- 0–10: Activación: “listas paralelas” → “dict”
- 10–30: Demo guiada 1 — CRUD de diccionario
- 30–45: Demo guiada 2 — Iteración: keys/values/items
- 45–55: Demo guiada 3 — `get()` y defaults
- 55–90: Laboratorio: 4 retos graduales (Day3)
- 90–100: Retro + checklist + mini-tarea

---

## Activación (5–10 min)
Pregunta:
> ¿Qué se rompe si insertas un nuevo alumno en `students` pero te olvidas de insertarlo en `student_ages`?

Respuesta esperada:
- “Se descuadran índices y la edad ya no corresponde”.
- Con dict, no existe ese problema porque “Peter → 24” está “pegado” en la misma estructura.

---

## Demo guiada 1 — CRUD de dict (Create/Read/Update/Delete)
### Create
```python
london = {"country": "England", "population": 8_982_000}
```

### Read
```python
london["country"]         # rápido pero si no existe -> KeyError
london.get("country")     # devuelve valor o None
london.get("pm", "N/A")   # default cuando no existe
```
> Idea clave: en apps reales, `get` es tu seguro anti-crash.

### Update
```python
london["population"] = 8_982_001
```

### Delete
```python
del london["country"]
```

---

## Demo guiada 2 — Iteración
```python
for key in london:
    print(key)

for value in london.values():
    print(value)

for key, value in london.items():
    print(f"{key} -> {value}")
```

---

## Demo guiada 3 — `zip` + dict comprehension
```python
students = ['Peter', 'Mary', 'George', 'Emma']
student_ages = [24, 25, 22, 20]
student_ages_dict = {key: value for key, value in zip(students, student_ages)}
```

---

## Laboratorio (archivo)
- `day3_challenges.py`
- `day3_solutions.py`

Los retos incluyen 2 casos reales del prework: calorie counter y weather forecast.

---

## Errores comunes
- `KeyError` por usar `d[key]` cuando la key no existe → usar `get` o validar con `in`
- Contadores sin default: `counts[word] += 1` rompe si no existe → `counts.get(word, 0) + 1`
- Querer keys+values pero iterar solo keys → usar `.items()`

---

## Mini-tarea (10 min)
- Agrega 5 asserts extra por reto (casos borde).
- Reescribe `count_words` para que ignore `.,!?` al final de palabra (opcional).
