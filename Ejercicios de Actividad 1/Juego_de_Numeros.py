import random
numero_secreto = random.randint(1, 10)
intento = int(input("Adivina el número entre 1 y 10: "))

if intento == numero_secreto:
    print("Felicidades, acertaste!")
else:
    print("Intenta de nuevo.")
