usuario_correcto = "admin"
password_correcto = "1234"
intentos = 0

while intentos < 3:
    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    if usuario == usuario_correcto and password == password_correcto:
        print(f"Sea Bienvenido, {usuario} :) ")
        break
    else:
        intentos += 1
else:
    print("Acceso bloqueado")
