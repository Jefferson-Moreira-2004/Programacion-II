import tkinter as tk
from tkinter import messagebox
import random

# Definir el color base y los colores unisex suaves
BACKGROUND_COLOR = "#f0f4f7"
BUTTON_COLOR = "#c1d3e5"
ENTRY_COLOR = "#e3e9f0"

# Estructura de datos para almacenar la información de las cuentas y el historial de transacciones
accounts = {}
transaction_history = {}

# Función para crear cuenta
def crear_cuenta():
    def guardar_cuenta():
        # Validar campos
        nombres = entry_nombres.get()
        apellidos = entry_apellidos.get()
        cedula = entry_cedula.get()
        telefono = entry_telefono.get()
        correo = entry_correo.get()
        codigo_retiro = entry_codigo_retiro.get()
        usuario = entry_usuario.get()
        contrasena = entry_contrasena.get()

        # Validaciones mínimas
        if len(cedula) != 10:
            messagebox.showerror("Error", "La cédula debe tener 10 dígitos.")
            return
        if len(codigo_retiro) != 6:
            messagebox.showerror("Error", "El código de retiro debe tener 6 dígitos.")
            return
        if usuario in accounts:
            messagebox.showerror("Error", "El nombre de usuario ya está registrado.")
            return
        
        # Guardar la cuenta en el diccionario
        accounts[usuario] = {
            "nombres": nombres,
            "apellidos": apellidos,
            "cedula": cedula,
            "telefono": telefono,
            "correo": correo,
            "codigo_retiro": codigo_retiro,
            "contrasena": contrasena,
            "saldo": 1000,  # Saldo inicial
            "numero_cuenta": random.randint(1000000000, 9999999999),
            "tipo_cuenta": "Ahorros"  # Tipo de cuenta por defecto
        }

        # Inicializar el historial de transacciones vacío
        transaction_history[usuario] = []

        # Limpiar y cerrar el formulario
        messagebox.showinfo("Cuenta creada", "La cuenta ha sido creada con éxito.")
        ventana_crear_cuenta.destroy()

    # Ventana para crear cuenta
    ventana_crear_cuenta = tk.Toplevel(root)
    ventana_crear_cuenta.title("Crear Cuenta")
    ventana_crear_cuenta.geometry("400x500")
    ventana_crear_cuenta.config(bg=BACKGROUND_COLOR)

    # Campos de entrada
    tk.Label(ventana_crear_cuenta, text="Nombres", bg=BACKGROUND_COLOR).pack(pady=5)
    entry_nombres = tk.Entry(ventana_crear_cuenta, bg=ENTRY_COLOR)
    entry_nombres.pack(pady=5)

    tk.Label(ventana_crear_cuenta, text="Apellidos", bg=BACKGROUND_COLOR).pack(pady=5)
    entry_apellidos = tk.Entry(ventana_crear_cuenta, bg=ENTRY_COLOR)
    entry_apellidos.pack(pady=5)

    tk.Label(ventana_crear_cuenta, text="Cédula (10 dígitos)", bg=BACKGROUND_COLOR).pack(pady=5)
    entry_cedula = tk.Entry(ventana_crear_cuenta, bg=ENTRY_COLOR)
    entry_cedula.pack(pady=5)

    tk.Label(ventana_crear_cuenta, text="Número de Teléfono", bg=BACKGROUND_COLOR).pack(pady=5)
    entry_telefono = tk.Entry(ventana_crear_cuenta, bg=ENTRY_COLOR)
    entry_telefono.pack(pady=5)

    tk.Label(ventana_crear_cuenta, text="Correo Electrónico", bg=BACKGROUND_COLOR).pack(pady=5)
    entry_correo = tk.Entry(ventana_crear_cuenta, bg=ENTRY_COLOR)
    entry_correo.pack(pady=5)

    tk.Label(ventana_crear_cuenta, text="Código para Retirar Dinero (6 dígitos)", bg=BACKGROUND_COLOR).pack(pady=5)
    entry_codigo_retiro = tk.Entry(ventana_crear_cuenta, bg=ENTRY_COLOR)
    entry_codigo_retiro.pack(pady=5)

    tk.Label(ventana_crear_cuenta, text="Usuario", bg=BACKGROUND_COLOR).pack(pady=5)
    entry_usuario = tk.Entry(ventana_crear_cuenta, bg=ENTRY_COLOR)
    entry_usuario.pack(pady=5)

    tk.Label(ventana_crear_cuenta, text="Contraseña", bg=BACKGROUND_COLOR).pack(pady=5)
    entry_contrasena = tk.Entry(ventana_crear_cuenta, show="*", bg=ENTRY_COLOR)
    entry_contrasena.pack(pady=5)

    # Botón de crear cuenta
    tk.Button(ventana_crear_cuenta, text="Crear Cuenta", command=guardar_cuenta, bg=BUTTON_COLOR).pack(pady=20)

# Función para login
def login():
    def ingresar():
        usuario = entry_usuario.get()
        contrasena = entry_contrasena.get()

        # Validar si los datos son correctos
        if usuario not in accounts or accounts[usuario]["contrasena"] != contrasena:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
        else:
            # Cargar la ventana principal
            ventana_principal(usuario)

    # Ventana de login
    global root
    root = tk.Tk()
    root.title("Banca Móvil - Login")
    root.geometry("400x300")
    root.config(bg=BACKGROUND_COLOR)

    tk.Label(root, text="Usuario", bg=BACKGROUND_COLOR).pack(pady=10)
    entry_usuario = tk.Entry(root, bg=ENTRY_COLOR)
    entry_usuario.pack(pady=5)

    tk.Label(root, text="Contraseña", bg=BACKGROUND_COLOR).pack(pady=10)
    entry_contrasena = tk.Entry(root, show="*", bg=ENTRY_COLOR)
    entry_contrasena.pack(pady=5)

    # Botón para iniciar sesión
    tk.Button(root, text="Ingresar", command=ingresar, bg=BUTTON_COLOR).pack(pady=10)

    # Opción para crear cuenta
    tk.Label(root, text="¿No tienes cuenta?", bg=BACKGROUND_COLOR).pack(pady=5)
    tk.Button(root, text="Crear Cuenta", command=crear_cuenta, bg=BUTTON_COLOR).pack(pady=5)

    root.mainloop()

# Función para la ventana principal después de login
def ventana_principal(usuario):
    def transferir():
        def realizar_transferencia():
            # Obtener datos de la transferencia
            num_cuenta_destino = entry_num_cuenta_destino.get()
            tipo_cuenta = entry_tipo_cuenta.get()
            nombre_destinatario = entry_nombre_destinatario.get()
            apellido_destinatario = entry_apellido_destinatario.get()
            monto = float(entry_monto.get())

            # Validaciones
            if len(num_cuenta_destino) != 10:
                messagebox.showerror("Error", "El número de cuenta de destino debe tener 10 dígitos.")
                return
            if monto <= 0:
                messagebox.showerror("Error", "El monto debe ser mayor que cero.")
                return
            if monto > accounts[usuario]["saldo"]:
                messagebox.showerror("Error", "No tienes suficiente saldo.")
                return

            # Realizar la transferencia
            accounts[usuario]["saldo"] -= monto
            # Asegurarse de que el historial de transacciones esté inicializado
            if usuario not in transaction_history:
                transaction_history[usuario] = []
            transaction_history[usuario].append({
                "tipo": "Transferencia",
                "destino": num_cuenta_destino,
                "nombre": nombre_destinatario,
                "apellido": apellido_destinatario,
                "monto": monto
            })

            messagebox.showinfo("Transferencia", "Transferencia exitosa.")
            ventana_transferencia.destroy()

        # Ventana de transferencia
        ventana_transferencia = tk.Toplevel(ventana)
        ventana_transferencia.title("Realizar Transferencia")
        ventana_transferencia.geometry("400x500")
        ventana_transferencia.config(bg=BACKGROUND_COLOR)

        tk.Label(ventana_transferencia, text="Número de Cuenta Destino", bg=BACKGROUND_COLOR).pack(pady=5)
        entry_num_cuenta_destino = tk.Entry(ventana_transferencia, bg=ENTRY_COLOR)
        entry_num_cuenta_destino.pack(pady=5)

        tk.Label(ventana_transferencia, text="Tipo de Cuenta", bg=BACKGROUND_COLOR).pack(pady=5)
        entry_tipo_cuenta = tk.Entry(ventana_transferencia, bg=ENTRY_COLOR)
        entry_tipo_cuenta.pack(pady=5)

        tk.Label(ventana_transferencia, text="Nombre Destinatario", bg=BACKGROUND_COLOR).pack(pady=5)
        entry_nombre_destinatario = tk.Entry(ventana_transferencia, bg=ENTRY_COLOR)
        entry_nombre_destinatario.pack(pady=5)

        tk.Label(ventana_transferencia, text="Apellido Destinatario", bg=BACKGROUND_COLOR).pack(pady=5)
        entry_apellido_destinatario = tk.Entry(ventana_transferencia, bg=ENTRY_COLOR)
        entry_apellido_destinatario.pack(pady=5)

        tk.Label(ventana_transferencia, text="Monto a Transferir", bg=BACKGROUND_COLOR).pack(pady=5)
        entry_monto = tk.Entry(ventana_transferencia, bg=ENTRY_COLOR)
        entry_monto.pack(pady=5)

        tk.Button(ventana_transferencia, text="Transferir", command=realizar_transferencia, bg=BUTTON_COLOR).pack(pady=20)

    def consultar_saldo():
        saldo = accounts[usuario]["saldo"]
        messagebox.showinfo("Saldo Actual", f"Tu saldo es: ${saldo}")

    def retirar():
        def realizar_retiro():
            codigo_retiro = entry_codigo_retiro.get()
            monto_retiro = float(entry_monto_retiro.get())

            # Validaciones
            if len(codigo_retiro) != 6:
                messagebox.showerror("Error", "El código de retiro debe tener 6 dígitos.")
                return
            if monto_retiro <= 0:
                messagebox.showerror("Error", "El monto debe ser mayor que cero.")
                return
            if monto_retiro > accounts[usuario]["saldo"]:
                messagebox.showerror("Error", "No tienes suficiente saldo.")
                return
            if codigo_retiro != accounts[usuario]["codigo_retiro"]:
                messagebox.showerror("Error", "Código de retiro incorrecto.")
                return

            # Realizar el retiro
            accounts[usuario]["saldo"] -= monto_retiro
            if usuario not in transaction_history:
                transaction_history[usuario] = []
            transaction_history[usuario].append({
                "tipo": "Retiro",
                "monto": monto_retiro
            })

            messagebox.showinfo("Retiro", "Retiro exitoso.")
            ventana_retiro.destroy()

        # Ventana de retiro
        ventana_retiro = tk.Toplevel(ventana)
        ventana_retiro.title("Retirar Dinero")
        ventana_retiro.geometry("400x400")
        ventana_retiro.config(bg=BACKGROUND_COLOR)

        tk.Label(ventana_retiro, text="Código de Retiro (6 dígitos)", bg=BACKGROUND_COLOR).pack(pady=5)
        entry_codigo_retiro = tk.Entry(ventana_retiro, bg=ENTRY_COLOR)
        entry_codigo_retiro.pack(pady=5)

        tk.Label(ventana_retiro, text="Monto a Retirar", bg=BACKGROUND_COLOR).pack(pady=5)
        entry_monto_retiro = tk.Entry(ventana_retiro, bg=ENTRY_COLOR)
        entry_monto_retiro.pack(pady=5)

        tk.Button(ventana_retiro, text="Retirar", command=realizar_retiro, bg=BUTTON_COLOR).pack(pady=20)

    def historial_transacciones():
        # Mostrar el historial de transacciones
        if usuario in transaction_history:
            historial = transaction_history[usuario]
            historial_texto = ""
            for transaccion in historial:
                if transaccion["tipo"] == "Transferencia":
                    historial_texto += f"Transferencia a {transaccion['destino']} de ${transaccion['monto']}\n"
                else:
                    historial_texto += f"Retiro de ${transaccion['monto']}\n"
            messagebox.showinfo("Historial de Transacciones", historial_texto)
        else:
            messagebox.showinfo("Historial de Transacciones", "No hay transacciones aún.")

    # Ventana principal después de login
    ventana = tk.Tk()
    ventana.title("Banca Móvil - Principal")
    ventana.geometry("400x500")
    ventana.config(bg=BACKGROUND_COLOR)

    usuario_data = accounts[usuario]
    nombre_titular = usuario_data["nombres"].split()[0]
    apellidos_titular = usuario_data["apellidos"].split()[0]
    
    tk.Label(ventana, text=f"Bienvenido, {nombre_titular} {apellidos_titular}", bg=BACKGROUND_COLOR).pack(pady=20)

    tk.Label(ventana, text=f"Número de Cuenta: {usuario_data['numero_cuenta']}", bg=BACKGROUND_COLOR).pack(pady=5)
    tk.Label(ventana, text=f"Tipo de Cuenta: {usuario_data['tipo_cuenta']}", bg=BACKGROUND_COLOR).pack(pady=5)

    # Botones interactivos
    tk.Button(ventana, text="Consultar Saldo", command=consultar_saldo, bg=BUTTON_COLOR).pack(pady=10)
    tk.Button(ventana, text="Transferir", command=transferir, bg=BUTTON_COLOR).pack(pady=10)
    tk.Button(ventana, text="Retirar Dinero", command=retirar, bg=BUTTON_COLOR).pack(pady=10)
    tk.Button(ventana, text="Historial de Transacciones", command=historial_transacciones, bg=BUTTON_COLOR).pack(pady=10)

    ventana.mainloop()

# Ejecutar la aplicación
login()
