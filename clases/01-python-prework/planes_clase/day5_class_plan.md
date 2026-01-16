# Clase Día 5 — Herencia y diseño OOP (super, override, classmethod) con MUCHO detalle

## Enfoque del día
Ya sabes crear clases. Hoy aprenderás a **reutilizar** código y modelar jerarquías:

- `Building` (base)
  - `House` (subclase)
  - `Castle` (subclase con comportamiento extra)

**Palabras clave**:
- herencia (inheritance)
- `super()` (llamar a la implementación del padre)
- override (sobrescribir un método)
- `@classmethod` (métodos a nivel de clase)

---

## Objetivos del día
Al final, el alumno puede:
1. Explicar qué problema resuelve la herencia (evitar duplicación, DRY).
2. Crear una subclase y heredar atributos/métodos del padre.
3. Sobrescribir un método y llamar a `super()` para no reescribir todo.
4. Entender diferencia entre:
   - instance method (usa `self`)
   - class method (usa `cls`)
5. Diseñar clases con responsabilidades claras.

---

## Agenda sugerida (100 min)
- 0–10: Activación: “duplicación” vs “reutilización”
- 10–25: Demo 1 — Building base class
- 25–45: Demo 2 — Subclases + `super().__init__`
- 45–60: Demo 3 — Override + `super().method()`
- 60–90: Laboratorio (4 retos Day5)
- 90–100: Retro + checklist

---

## Activación: el dolor de duplicar
Haz que el alumno imagine:
- `House` y `Castle` tienen `width`, `length`, `floor_area()`.
- Si duplicas ese método en ambos:
  - ¿Qué pasa si mañana cambia la fórmula?
  - Debes cambiarlo en 2 lugares → bug seguro.

Mensaje:
> “Herencia: un solo lugar para la lógica común.”

---

## Demo 1 — Base class
```python
class Building:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def floor_area(self):
        return self.width * self.length
```

---

## Demo 2 — Subclases
```python
class House(Building):
    pass
```
- Hereda `__init__` y `floor_area` sin escribir nada.

---

## Demo 3 — Override + super()
```python
class Castle(Building):
    def floor_area(self):
        base = super().floor_area()
        return base + 300  # jardín
```

Punto clave:
- `super()` evita copiar/pegar la lógica base.

---

## Classmethod explicado simple
- Instance method: necesitas una *instancia* para llamarlo.
  - `castle.floor_area()`
- Class method: lo llamas desde la clase:
  - `Castle.categories()`

Usos típicos:
- constructores alternativos (factory methods)
- información del “tipo” (categorías, configuración, defaults)

---

## Laboratorio — 4 retos (Day5)
1) Construir jerarquía Building/House/Castle
2) Añadir estado propio en Castle (butler)
3) Override con super (jardín)
4) classmethod categories

---

## Errores comunes
- Olvidar heredar: `class House:` en vez de `class House(Building):`
- No llamar a `super().__init__` cuando la subclase redefine el init
- Confundir `self` y `cls` en classmethod
- Hacer override y no respetar el contrato de retorno

---

## Checklist final
- [ ] ¿La subclase hereda correctamente?
- [ ] ¿No hay duplicación de lógica?
- [ ] ¿Override usa `super()` cuando corresponde?
- [ ] ¿classmethod no usa `self`?

---

## Tarea
- Crea otra subclase `Skyscraper` con pisos y un método `total_area()`.
