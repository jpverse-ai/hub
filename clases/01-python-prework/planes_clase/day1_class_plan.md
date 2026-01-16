# Clase Día 1 — Python 101 (con mucho detalle)

## Objetivos (al final de la clase el alumno puede…)
1. Explicar la diferencia entre `int`, `float`, `str`, `bool` y `None`.
2. Escribir funciones con `def`, parámetros, `return`, docstring y type hints.
3. Transformar strings usando `.strip()`, `.lower()`, `.capitalize()`.
4. Usar condicionales (`if/else`) para decidir entre dos salidas.
5. Aplicar `%` (módulo) para validar divisibilidad.

---

## Agenda sugerida (100 min)
- 0–10: Activación (mini quiz + motivación)
- 10–30: Demo guiada 1: Strings y casting
- 30–45: Demo guiada 2: Condicionales + f-strings
- 45–85: Laboratorio: 4 retos graduales
- 85–100: Revisión + checklist de calidad

---

## Activación (mini quiz)
1) ¿Qué imprime esto?
```python
print(type(3), type(3.0), type("3"))
```
2) ¿Qué devuelve `"  Hola  ".strip().lower()`?
3) ¿Qué significa `num % 2 == 0`?

---

## Demo guiada 1 — Strings y “normalización”
### Idea clave: “limpiar” entradas antes de procesarlas
- `strip()` elimina espacios al inicio y al final.
- `lower()` y `upper()` normalizan mayúsculas/minúsculas.
- `replace()` sustituye fragmentos.
- `split()` separa en lista.

Ejemplo:
```python
raw = "  Scraped_Email@Email.com  "
clean = raw.strip().lower()
print(clean)
```

> Mensaje docente: “Siempre que recibas input humano o scrapeado, normaliza”.

---

## Demo guiada 2 — Funciones + if
### Patrón mental
1) Entradas (inputs)
2) Regla de decisión
3) Salida (output)

Ejemplo:
```python
def is_adult(age: int) -> bool:
    return age >= 18
```

Luego:
```python
def greeting(name: str, age: int) -> str:
    name = name.strip().capitalize()
    if age >= 18:
        return f"Hola {name}, eres mayor de edad"
    return f"Hola {name}, eres menor de edad"
```

---

## Laboratorio (archivo)
- `day1_challenges.py` (alumno)
- `day1_solutions.py` (teacher)

### Qué observar al corregir
- ¿Usa return en lugar de print?
- ¿Los nombres son claros?
- ¿Probó con asserts?
- ¿Manejó formato inválido en la calculadora?

---

## Errores comunes (y cómo explicarlos)
- Confundir `==` con `=`
- Olvidar `return`
- No convertir strings a números (`float("3")`)
- Comparar strings con números sin casting

---

## Tarea (10–15 min)
- Extiende `simple_calculator` para aceptar espacios: `[" 1 ", "+", " 2 "]`.
- Agrega 3 asserts nuevos.
