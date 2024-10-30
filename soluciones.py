import math
radio = float(input("Ingrese el radio: "))
perimetro = 2 * math.pi * radio
area = math.pi * (radio ** 2)
print(f"Perímetro: {perimetro:.1f}")
print(f"Área: {area:.1f}")