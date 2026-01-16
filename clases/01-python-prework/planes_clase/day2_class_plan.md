# Clase Día 2 — Listas y Bucles (con MUCHO detalle)

> Basado en: *Day2 slides — Lists and loops* (listas, `for`, `range`, `enumerate`, list comprehensions).

## Objetivos (al final de la clase el alumno puede…)
1. Crear y modificar listas usando `append`, asignación por índice, `remove`, `pop`, `del` y `len()`.
2. Explicar por qué “los índices empiezan en 0” y usar índices negativos.
3. Recorrer listas con `for` y entender `range(n)` como “0..n-1”.
4. Recorrer lista con índice usando `enumerate`, y construir strings como `"1 - Ben"`.
5. Transformar listas con **list comprehensions**, incluyendo la variante con condición `if/else`.

---

## Agenda sugerida (100 min)
- 0–10: Activación (quiz corto + repaso Day1)
- 10–25: Demo guiada 1 — Crear/editar listas (CRUD básico)
- 25–45: Demo guiada 2 — Bucles: `for`, `range`, `enumerate`
- 45–60: Mini-ejercicio en vivo (del profe → alumnos)
- 60–90: Laboratorio: 4 retos graduales (Day2)
- 90–100: Retro + checklist + “qué estudiar hoy”

> Consejo docente: si es un prework, tu meta es que el alumno practique *patrones* (no que memorice).

---

## Activación (mini quiz)
1) ¿Qué pasa aquí y por qué?
```python
beatles = ["john", "ringo", "seb"]
print(beatles[2])
beatles[2] = "george"
print(beatles)
```
2) ¿Qué imprime?
```python
for num in range(5):
    print(num)
```
3) ¿Qué diferencia hay entre `remove`, `pop` y `del`?

---

## Demo guiada 1 — “CRUD” de lista (Create/Read/Update/Delete)
### 1) Crear y leer
```python
staff = ["Ben", "Alex", "Lucien"]
print(staff[0])     # "Ben"
print(staff[-1])    # último elemento
```
**Idea clave**: índice fuera de rango → `IndexError`.

### 2) Actualizar
```python
staff[1] = "Alexa"
```

### 3) Agregar
```python
staff.append("Arthur")
```

### 4) Borrar (tres formas)
- `remove("Arthur")`: borra por valor (solo primera ocurrencia)
- `pop(0)`: borra por índice **y devuelve** el elemento
- `del staff[0]`: borra por índice (no devuelve)

> Mensaje docente: “cuando no sabes si el índice existe, diseña una función segura”.

---

## Demo guiada 2 — Bucles: `for`, `range`, `enumerate`
### Recorrer un rango
`range(5)` produce 0,1,2,3,4
```python
for i in range(5):
    print(i)
```

### Recorrer una lista
```python
for name in staff:
    print(name)
```

### Recorrer con índice (enumerate)
```python
for index, name in enumerate(staff):
    print(f"{index + 1} - {name}")
```

---

## Mini-ejercicio en vivo (10–15 min)
**Objetivo**: construir un “listado numerado” y detectar errores comunes.
- Pide al alumno que intente hacerlo primero con un contador manual:
  ```python
  i = 1
  for name in staff:
      print(f"{i} - {name}")
      i += 1
  ```
- Luego muéstrale `enumerate` y explica por qué es más limpio.

Errores comunes:
- Olvidar `i += 1`
- Empezar desde 0 cuando el enunciado quiere desde 1

---

## Laboratorio (archivo)
- `day2_challenges.py` (alumno)
- `day2_solutions.py` (teacher)

### Rutina de corrección (checklist)
1. ¿La función devuelve (return) lo pedido?
2. ¿Maneja casos borde? (lista vacía, n=0, índice inválido)
3. ¿Tiene docstring y type hints?
4. ¿Hay asserts suficientes?

---

## Extensiones (si terminan rápido)
- Haz que `fizz_buzz_list` acepte un `start` (por defecto 1).
- En `chunk_list`, valida que `size > 0` y lanza `ValueError` si no.

---

## Tarea (10–20 min)
- Repite los 4 retos sin mirar el código, solo con el enunciado.
- Agrega 5 asserts nuevos (casos borde).
