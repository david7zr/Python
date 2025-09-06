def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32

def run_temperature_converter() -> None:
    while True:
        try:
            c = float(input("Enter temperature in Celsius: "))
            break
        except ValueError:
            print("Invalid input! Enter a number.")
    print(f"{c}°C is {celsius_to_fahrenheit(c)}°F")

if __name__ == "__main__":
    run_temperature_converter()