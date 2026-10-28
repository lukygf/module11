from .light_validator import validate_ingredients

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str):
    ing = validate_ingredients(ingredients, light_spell_allowed_ingredients())
    if ing:
        print(f"Spell recorded: {spell_name} ({ingredients} - VALID)")
    else:
        print(f"Spell rejected: {spell_name} ({ingredients} - INVALID)")