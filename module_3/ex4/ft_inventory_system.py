#!/usr/bin/python3    

import sys

def inventory_system() -> None:
    print("=== Inventory System Analysis ===")

    inventory = dict()

    for i in range(1, len(sys.argv)):
        partes = sys.argv[i].split(":")

        if len(partes) != 2:
            print(f"Error - invalid parameter '{sys.argv[i]}'")
            continue

        if partes[0] in inventory:
            print(f"Redundant item '{partes[0]}' - discarding")
            continue

        try:
            num = int(partes[1])
            inventory[partes[0]] = num

        except ValueError as error:
            print(f"Quantity error for '{partes[0]}': {error}")
        
    print(f"Got inventory: {inventory}")

    print(f"Items list: {inventory.keys()}")
    
    total = sum(inventory.values())
    print(f"Total quantity of the {len(sys.argv) - 1} items: {total}")

    for key in inventory:
        percentage = (inventory[key] / total) * 100
        print(f"Item {key} represents {percentage:.2f}%")

    """
    valores = list(inventory.values())
    claves = list(inventory.keys())
    mayor = valores[0]
    clave_mayor = claves[0]

    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]
            clave_mayor = claves[i]
    
    print(f"Item most abundant: {clave_mayor} with quantity {mayor}")
    """

    maximo = 0
    clave_maximo = ''

    for key in inventory:
        if inventory[key] > maximo:
            maximo = inventory[key]
            clave_maximo = key
    
    print(f"Item most abundant: {clave_maximo} with quantity {maximo}")

    minimo = maximo
    clave_minimo = ''

    for key in inventory:
        if inventory[key] < minimo:
            minimo = inventory[key]
            clave_minimo = key

    print(f"Item least abundant: {clave_minimo} with quantity {minimo}")

    inventory['magic_item'] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    inventory_system()