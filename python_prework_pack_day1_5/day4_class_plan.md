# Clase Día 4 — Programación Orientada a Objetos (Clases) con MUCHO detalle

## Propósito del día
Hasta ahora el alumno resolvió problemas con funciones + listas + dicts.
Hoy damos el salto a un concepto clave del mundo real: **modelar cosas** con *clases*.

**Idea central**:
- Una *clase* es un “molde” (plantilla).
- Un *objeto/instancia* es “una cosa concreta” creada con ese molde.

Ejemplo: `Car` (clase) → mi carro “Toyota Corolla” (objeto).

---

## Objetivos del día
Al final, el alumno puede:
1. Explicar diferencia entre **clase** e **instancia** con un ejemplo.
2. Crear una clase con atributos y métodos.
3. Entender `__init__` como el “constructor” donde se inicializa el estado.
4. Entender `self` como “la instancia actual”.
5. Diseñar métodos con un “contrato”: *input → output* y *reglas*.
6. Hacer métodos que cambian estado (mutables) vs métodos que calculan y devuelven (puros).

---

## Agenda sugerida (100 min)
- 0–10: Activación: “¿por qué no basta con dicts?”
- 10–25: Demo guiada 1 — Clase mínima + `__init__`
- 25–45: Demo guiada 2 — Métodos (lectura vs mutación de estado)
- 45–55: Mini-ejercicio en vivo
- 55–90: Laboratorio: 4 retos graduales (Day4)
- 90–100: Retro + checklist + tarea corta

---

## Activación (5–10 min) — ¿Por qué clases?
Plantea este caso:
> “Tengo 1,000 estudiantes. Cada uno tiene nombre, billetera (billetes), y necesito compararlos por riqueza.”

Con dicts:
- Sí se puede, pero termina en “diccionarios enormes + claves mágicas + bugs”.

Con clases:
- `Student.wealth()` encapsula la lógica.
- `Student.compare(other)` encapsula la comparación.

Mensaje docente:
- “Las clases organizan el código alrededor de *entidades* del dominio.”

---

## Demo guiada 1 — Clase mínima
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name}: woof!"
```

Puntos clave:
- `__init__` corre cada vez que creas un objeto: `Dog("Fido")`
- `self.name` guarda estado en la instancia

---

## Demo guiada 2 — Métodos de lectura vs mutación
Usa un ejemplo simple:
```python
class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1   # muta estado

    def is_even(self):
        return self.value % 2 == 0  # calcula y devuelve
```

**Discusión**:
- ¿Cuándo conviene mutar estado? (cuando modelas una cosa que cambia)
- ¿Cuándo conviene devolver un cálculo? (cuando no quieres efectos colaterales)

---

## Mini-ejercicio (10 min)
Pide que implementen:
- `BankAccount.deposit(amount)` (muta)
- `BankAccount.balance_in_usd(rate)` (calcula)

Luego muestra cómo testear con asserts.

---

## Laboratorio — 4 retos graduales (Day4)
- Reto 1: clase `Car` (estado: engine_started)
- Reto 2: clase `Castle` (métodos que formatean texto)
- Reto 3: clase `Student` (cálculo de riqueza)
- Reto 4: comparación avanzada: ranking por riqueza (ordenamiento + OOP)

**Dinámica recomendada**:
1) Lee el enunciado
2) Diseña atributos (estado)
3) Diseña métodos (comportamiento)
4) Escribe asserts primero (si puedes)
5) Implementa

---

## Errores comunes (y cómo corregirlos)
1) Olvidar `self` en la firma:
   - `def wealth():` ❌ → `def wealth(self):` ✅
2) Usar variables sueltas en vez de atributos:
   - `name = name` ❌ → `self.name = name` ✅
3) Mezclar responsabilidades:
   - Método `wealth()` no debería hacer `print`, solo calcular y retornar.
4) Comparar objetos sin criterio:
   - Para ordenar, usa `sorted(students, key=lambda s: s.wealth(), reverse=True)`

---

## Checklist final
- [ ] ¿La clase tiene un `__init__` claro?
- [ ] ¿Los atributos se nombran bien?
- [ ] ¿Los métodos devuelven lo que prometen?
- [ ] ¿Hay asserts para casos borde?

---

## Tarea (10–20 min)
- Agrega un método `__repr__` a `Car` o `Student` para que el objeto se imprima bonito.
- Agrega 5 asserts extra en Day4.
