"""Day 3 — SOLUCIONES"""

MENU = {
    "Cheese Burger": 290,
    "Big Mac": 590,
    "McChicken": 430,
    "French Fries": 340,
    "Salad": 100,
    "Coca Cola": 150,
    "Sprite": 140
}
MEALS = {
    "Happy Meal": ["Cheese Burger", "French Fries", "Coca Cola"],
    "Best Of Big Mac": ["Big Mac", "French Fries", "Coca Cola"],
    "Best Of McChicken": ["McChicken", "Salad", "Sprite"]
}

def build_age_dict(names: list[str], ages: list[int]) -> dict[str, int]:
    return {n: a for n, a in zip(names, ages)}

def count_words(sentence: str) -> dict[str, int]:
    counts = {}
    for w in sentence.lower().split():
        counts[w] = counts.get(w, 0) + 1
    return counts

def advanced_calories_counter(orders: list[str]):
    total = 0
    for name in orders:
        if name in MENU:
            total += MENU[name]
        elif name in MEALS:
            for item in MEALS[name]:
                total += MENU[item]
        else:
            return f"{name} not found"
    return total

def is_colorful(num: int) -> bool:
    digits = [int(ch) for ch in str(num)]
    seen = set()
    for i in range(len(digits)):
        product = 1
        for j in range(i, len(digits)):
            product *= digits[j]
            if product in seen:
                return False
            seen.add(product)
    return True

if __name__ == "__main__":
    assert advanced_calories_counter(["Happy Meal"]) == 780
    print("✅ Day 3 SOLUCIONES OK")
