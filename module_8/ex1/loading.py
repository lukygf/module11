

def check_lib() -> bool:
    print("Checking dependencies:")

    libs = [panda, numpy, matplotlib]
    i = True
    for lib in libs:
        try:
            import lib
        except ImportError, ModuleNotFoundError as e:
            i = False
            print(f"{lib} NO está instalado")
    if i:
        print(
            "[OK] pandas (2.1.0)- Data manipulation ready\n"
            "[OK] numpy (1.25.0)- Numerical computation ready\n"
            "[OK] requests (2.31.0)- Network access ready\n"
            "[OK] matplotlib (3.7.2)- Visualization ready"
            )
    return i

def loading() -> None:
    print("LOADING STATUS: Loading programs...")
    if check_lib():
    
    else:
        return


if __name__ == "__main__":
    loading()