CM_PER_INCH = 2.54 
SQUARE_POWER = 2
SQRT_POWER = 0.5
CM_DECIMAL_PLACES = 2
INCH_DECIMAL_PLACES = 1

width_cm = float(input("Enter width (cm): "))
height_cm = float(input("Enter height (cm): "))

diagonal_cm = (width_cm ** SQUARE_POWER + height_cm ** SQUARE_POWER) ** SQRT_POWER
screen_size_inches = diagonal_cm / CM_PER_INCH

print(f"Diagonal: {diagonal_cm:.{CM_DECIMAL_PLACES}f} cm")
print(f"Screen size: {screen_size_inches:.{INCH_DECIMAL_PLACES}f} inches")
