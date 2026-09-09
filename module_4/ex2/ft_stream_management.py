#!/usr/bin/python3

import sys

def ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    
    print("=== Cyber Archives Recovery & Preservation ===")

    print(f"Accessing file '{sys.argv[1]}'")

    try:
        f = open(sys.argv[1])

        contenido = f.read()
        
        print("---")
        print(contenido)
        print("---")

        f.close()

        print(f"File '{sys.argv[1]}' closed.")
        
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        return

    print("\nTransform data:")

    nuevo_contenido = contenido.replace("\n", "#\n")
    nuevo_contenido = nuevo_contenido + "#"

    print("---")
    print(nuevo_contenido)
    print("---")

    print("Enter new file name (or empty): ", end="", flush=True)
    decision = sys.stdin.readline()
    decision = decision.rstrip("\n")

    if decision:
        print(f"Saving data to '{decision}'")
        try:
            archivo = open(decision, "w")

            archivo.write(nuevo_contenido)

            archivo.close()

            print(f"Data saved in file '{decision}'.")

        except Exception as e:
            sys.stderr.write(f"[STDERR] Error opening file '{decision}': {e}\n")
            print("Data not saved.")

    else:
        print("Not saving data.")

            
    
if __name__ == "__main__":
    ancient_text()
