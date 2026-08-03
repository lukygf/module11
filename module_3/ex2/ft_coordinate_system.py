#!/usr/bin/python3

import math

def get_player_pos() -> tuple:

    lista = []

    while True:
        i = 0
        pos = input("Enter new coordinates as floats in format 'x,y,z':")

        partes = pos.split(",")

        if len(partes) != 3:
            i = 1
        else:
            for j in range(0, 3):
                try:
                    num = float(partes[j])
                    lista.append(num)
                except ValueError:
                    i = 1

        if i == 0:
            tupla = tuple(lista)
            break
        else:
            print("Invalid syntax")
    
    return tupla

def coordinate_system() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")

    first = get_player_pos()

    print(f"Got a first tuple: {first}")
    
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")

    print(f"Distance to center: {math.sqrt(first[0]**2 + first[1]**2 + first[2]**2)}")

    print("Get a second set of coordinates")

    second = get_player_pos()

    print(f"Distance between the 2 sets of coordinates: {math.sqrt((second[0]-first[0])**2 + (second[1]-first[1])**2 + (second[2]-first[2])**2)}")


if __name__ == "__main__":
    coordinate_system()