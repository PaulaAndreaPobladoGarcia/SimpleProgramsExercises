import math

# Constants
M = 47  # Mass of the egg in grams
p = 1.038  # Density in g/cm³
c = 3.7  # Specific heat capacity in J/g°C
K = 5.4 * math.pow(10, -3)  # Thermal conductivity in W/(m·K)
Tw = 100  # Temperature of the water in °C
Ty = 70   # Desired temperature in °C

# Input: Original temperature of the egg
To = float(input("Enter the original temperature of the egg (in °C): "))

# Calculations
dividing = math.pow(M, 2/3) * (c * math.pow(p, (1/3)))
divisor = (K * math.pow(math.pi, 2)) * math.pow((4 * math.pi) / 3, (2/3))
resultado = dividing / divisor

resultado2 = math.log((0.76 * To - Tw) / (Ty - Tw))

# Time in seconds to reach the maximum temperature
seconds = resultado * resultado2
minutes = round(seconds / 60)

# Output: Display the time in seconds and minutes
print(f"Time to reach the maximum temperature for a soft-boiled egg: {seconds:.2f} seconds ({minutes} minutes)")
