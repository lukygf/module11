#!/usr/bin/python3    

import random

players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam"
]

def data_alchemist() -> None:
    print("=== Game Data Alchemist ===")

    print(f"Initial list of players: {players}")

    nueva = [nombre.capitalize() for nombre in players]
    print(f"New list with all names capitalized: {nueva}")

    nueva_dos = [nombre for nombre in players if nombre == nombre.capitalize()]
    print(f"New list of capitalized names only: {nueva_dos}")

    
    diccionario = {
        nombre: random.randint(1, 1000)
        for nombre in nueva_dos
    }
    print(f"Score dict: {diccionario}")
    
    total = sum(diccionario.values())
    media = total / len(diccionario)
    print(f"Score average is {media}")

    diccionario_dos = {
        key: diccionario[key]
        for key in diccionario
        if diccionario[key] > media
    }
    print(f"High scores: {diccionario_dos}")

    """
    diccionario = {}
    for nombre in nueva_dos:
        diccionario[nombre] = random.randint(1, 1000)

    print(f"Score dict: {diccionario}")

    total = sum(diccionario.values())
    media = total / len(diccionario)
    print(f"Score average is {media}")

    diccionario_dos = {}

    for key in diccionario:
        if diccionario[key] > media:
            diccionario_dos[key] = diccionario[key]
    
    print(f"High scores: {diccionario_dos}")
    """



if __name__ == "__main__":
    data_alchemist()