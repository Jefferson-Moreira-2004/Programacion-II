notas = []
while True:
    nota = float(input("Introduce una calificación (-1 para terminar): "))
    if nota == -1:
        break
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
