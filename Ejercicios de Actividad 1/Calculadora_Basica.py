a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == '+':
    print(f"Resultado: {a + b}")
elif operacion == '-':
    print(f"Resultado: {a - b}")
elif operacion == '*':
    print(f"Resultado: {a * b}")
elif operacion == '/':
    print(f"Resultado: {a / b}")
else:
    print("Operación no válida")
