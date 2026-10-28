from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str, val_ing: list) -> bool:
    ing = ingredients.split()
    for i in ing:
        if i in val_ing:
            return True
    return False