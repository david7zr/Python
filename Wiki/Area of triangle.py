def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == "__main__":
    base = float(input("Base of triangle: "))
    height = float(input("Height of triangle: "))
    area = triangle_area(base, height)
    print(f"Area of triangle: {area:.2f}")
