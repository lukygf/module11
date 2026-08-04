#!/usr/bin/python3

import sys

def ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

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
        print(f"Error opening file '{sys.argv[1]}': {e}")
    


    
if __name__ == "__main__":
    ancient_text()