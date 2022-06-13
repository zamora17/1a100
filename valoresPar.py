a: int = int(input('Introduce un número: '))
b: int = int(input('Inroduce otro número: '))
impares: [int] = []


while b <= a:
    b: int = int(input('El segundo número debe ser mayor que el primero. Inroduce otro número: '))

for i in range(a, b+1):
    if(i % 2 != 0):
        impares.append(i)

print(f"Lista de Números impares entre {a} y {b}:")
print(impares)
