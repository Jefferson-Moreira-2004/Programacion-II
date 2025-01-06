mes = input("Introduce el mes de nacimiento: ").lower()
dia = int(input("Introduce el día de nacimiento: "))

if (mes == "julio" and dia >= 23) or (mes == "agosto" and dia <= 22):
    print("Tu signo es Leo")
# Agregar los otros signos zodiacales según el día y mes.
