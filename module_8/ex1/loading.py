
def check_lib() -> bool:
    print("\nChecking dependencies:")

    i = True
    try:
        import pandas
        print(f"[OK] pandas {pandas.__version__}- Data manipulation ready")
    except (ImportError, ModuleNotFoundError):
            i = False
            print(f"pandas NO está instalado\n")

    try:
        import numpy
        print(f"[OK] numpy {numpy.__version__}- Numerical computation ready")
    except (ImportError, ModuleNotFoundError):
            i = False
            print(f"numpy NO está instalado\n")

    try:
        import matplotlib
        print(f"[OK] matplotlib {matplotlib.__version__}- Visualization ready\n")
    except (ImportError, ModuleNotFoundError):
            i = False
            print(f"matplotlib NO está instalado\n")

    return i


def loading() -> None:
    print("\nLOADING STATUS: Loading programs...")
    if check_lib():
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd

        print("Analyzing Matrix data...\nProcessing 1000 data points...")

        datos_numpy = np.random.normal(0, 1, 1000)

        df = pd.DataFrame(datos_numpy, columns=["Matrix_Signal"])
        df["Moving_Average"] = df["Matrix_Signal"].rolling(window=20).mean()

        print("Generating visualization...")
        plt.figure(figsize=(10, 5))
        plt.plot(df["Matrix_Signal"], label="Signal", alpha=0.6)
        plt.plot(df["Moving_Average"], label="Moving Average", color="red")
        plt.title("Matrix Data Analysis")
        plt.legend()

        plt.savefig("matrix_analysis.png")
        plt.close()

        print("Analysis complete!\nResults saved to: matrix_analysis.png")
    else:
        print("Pip Intallation:\n pip install -r requirements.txt\n")
        print("Poetry Intallation:\n poetry install\n poetry run python loading.py")



if __name__ == "__main__":
    loading()
