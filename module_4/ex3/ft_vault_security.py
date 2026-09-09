#!/usr/bin/python3

def secure_archive(
    archivo: str,
    accion: str | int | None = None,
    texto: str | None = None
) -> tuple:

    if accion == "read":
        try:
            with open(archivo) as f:
                contenido = f.read()

            tupla = (True, contenido)
            return tupla

        except Exception as e:
            tupla = (False, str(e))
            return tupla

    elif accion == "write":
        try:
            if texto is None:
                return (False, "No content provided for writing")

            with open(archivo, "w") as f:
                f.write(texto)
            
            tupla = (True, "Content successfully written to file")
            return tupla

        except Exception as e:
            tupla = (False, str(e))
            return tupla

    else:
        return (False, "Invalid action")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    tupla = secure_archive("archivo.txt", "write", "Como va eso")
    print(tupla)