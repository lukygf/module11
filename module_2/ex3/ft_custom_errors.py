#!/usr/bin/python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, message="Default plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Default water error"):
        super().__init__(message)


def check_garden_status(sensor_type: str):
    if sensor_type == "plant":
        raise PlantError("¡La planta está seca!")
    elif sensor_type == "water":
        raise WaterError("¡Falta agua en el tanque!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    for item in ["plant", "water"]:
        try:
            check_garden_status(item)

        except GardenError as e:
            print(f"Caught a general garden issue: {e}")
    
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()