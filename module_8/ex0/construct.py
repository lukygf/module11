import sys
import os
import site


def construct() -> None:
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print(
            "WARNING: You're in the global environment!\n"
            "The machines can see everything you install.\n"
            )
        print(
            "To enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            r"matrix_env\Scripts\activate # On Windows"
            )
        print("\nThen run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print(
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system."
            )

        site_packages_list = site.getsitepackages()
        if site_packages_list:
            site_packages_path = site_packages_list[0]
        else:
            site_packages_path = "N/A"

        print(f"Package installation path:\n{site_packages_path}")


if __name__ == "__main__":
    construct()