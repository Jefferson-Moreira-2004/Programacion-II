import tkinter as tk
from tkinter import messagebox
import random

class AdivinarNumeroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivinar el Número")  # Título de la ventana
        self.root.geometry("600x400")  # Ajustamos el tamaño de la ventana para que se vea bien
        self.root.config(bg="#333333")  # Fondo gris oscuro para un look más moderno

        # Variables del juego
        self.numero_secreto = random.randint(1, 100)  # Número aleatorio entre 1 y 100 que debe adivinar el jugador
        self.intentos_restantes = 10  # El jugador comienza con 10 intentos

        # Fuentes personalizadas para darle estilo al texto
        self.font_principal = ("Comic Sans MS", 16, "bold")
        self.font_secundaria = ("Comic Sans MS", 12, "bold")

        # Etiqueta para mostrar las instrucciones
        self.label_instrucciones = tk.Label(self.root, text="¡Adivina el número entre 1 y 100!", 
                                             font=self.font_principal, fg="white", bg="#333333")
        self.label_instrucciones.pack(pady=20)  # Un poco de espacio alrededor de la etiqueta

        # Etiqueta para mostrar los intentos restantes
        self.label_intentos = tk.Label(self.root, text=f"Tienes {self.intentos_restantes} intentos restantes.", 
                                       font=self.font_secundaria, fg="white", bg="#333333")
        self.label_intentos.pack()

        # Campo de texto para que el jugador ingrese su intento
        self.entry_intento = tk.Entry(self.root, font=("Arial", 18), width=10, justify="center", 
                                      bd=2, relief="solid", fg="black", bg="white")
        self.entry_intento.pack(pady=20)

        # Botón para realizar el intento
        self.boton_adivinar = tk.Button(self.root, text="Adivinar", font=self.font_secundaria, bg="#4CAF50", 
                                        fg="white", command=self.adivinar, relief="flat", height=2, width=12)
        self.boton_adivinar.pack(pady=10)

        # Etiqueta de retroalimentación donde mostraremos los mensajes del juego
        self.label_feedback = tk.Label(self.root, text="", font=self.font_secundaria, fg="white", bg="#333333")
        self.label_feedback.pack(pady=10)

        # Botón de reinicio para empezar un nuevo juego
        self.boton_reiniciar = tk.Button(self.root, text="Vamos de Nuevo?", font=self.font_secundaria, bg="#FFFFFF", 
                                         fg="black", command=self.reiniciar_juego, relief="flat", height=2, width=14)
        self.boton_reiniciar.pack(pady=5)
        self.boton_reiniciar.config(state=tk.DISABLED)  # El botón de reiniciar está deshabilitado al inicio

    def adivinar(self):
        """Esta función se ejecuta cuando el jugador hace clic en "Adivinar"."""
        try:
            intento = int(self.entry_intento.get())  # Tratamos de obtener el número ingresado por el jugador
        except ValueError:
            # Si el jugador no ingresa un número válido, mostramos un mensaje de error
            self.mostrar_feedback("Debes ingresar un número válido.")
            return

        # Verificamos que el número esté dentro del rango permitido (1 a 100)
        if intento < 1 or intento > 100:
            self.mostrar_feedback("Número fuera de rango. Intenta con un número entre 1 y 100.")
            return

        # Comprobamos si el intento es correcto
        if intento == self.numero_secreto:
            self.mostrar_feedback("¡Has adivinado! Tuvistes suerte esta vez ;)")  # Felicitaciones si adivina correctamente
            self.terminar_juego(True)
        elif intento < self.numero_secreto:
            self.mostrar_feedback("Muy bajo, intenta con un número más alto.")  # Si el intento es bajo
        else:
            self.mostrar_feedback("Te has pasado, intenta con un número más bajo.")  # Si el intento es alto

        # Restamos uno a los intentos restantes y actualizamos la etiqueta
        self.intentos_restantes -= 1
        self.label_intentos.config(text=f"Tienes {self.intentos_restantes} intentos restantes. ¡Úsalos sabiamente!")

        # Si no quedan intentos, termina el juego
        if self.intentos_restantes == 0:
            self.mostrar_feedback(f"Te quedaste sin intentos. El número correcto era: {self.numero_secreto}")
            self.terminar_juego(False)

    def mostrar_feedback(self, mensaje):
        """Muestra los mensajes de retroalimentación sobre el juego (si el intento fue correcto, bajo, alto, etc.)"""
        self.label_feedback.config(text=mensaje)

    def terminar_juego(self, ganado):
        """Esta función se ejecuta cuando el juego termina, ya sea por ganar o perder."""
        if ganado:
            # Si el jugador ganó, mostramos un mensaje de felicitaciones
            messagebox.showinfo("¡Ganaste!", "¡Felicidades, la próxima vez no será tan fácil!")
        else:
            # Si el jugador pierde, mostramos el número secreto
            messagebox.showinfo("Perdiste", f"Te has quedado sin intentos. El número era {self.numero_secreto}.")

        # Deshabilitamos los controles de juego (entrada y botón de adivinar)
        self.entry_intento.config(state=tk.DISABLED)
        self.boton_adivinar.config(state=tk.DISABLED)

        # Habilitamos el botón de reiniciar para jugar nuevamente
        self.boton_reiniciar.config(state=tk.NORMAL)

    def reiniciar_juego(self):
        """Reinicia el juego generando un nuevo número secreto y restaurando los intentos."""
        self.numero_secreto = random.randint(1, 100)  # Genera un nuevo número secreto
        self.intentos_restantes = 10  # Restauramos los intentos a 10
        self.label_intentos.config(text=f"Te quedan {self.intentos_restantes} intentos. ¡Échale ganas!")
        self.entry_intento.config(state=tk.NORMAL)  # Habilitamos la entrada para nuevos intentos
        self.entry_intento.delete(0, tk.END)  # Limpiamos el campo de texto
        self.boton_adivinar.config(state=tk.NORMAL)  # Habilitamos el botón de adivinar
        self.label_feedback.config(text="")  # Limpiamos el mensaje de retroalimentación
        self.boton_reiniciar.config(state=tk.DISABLED)  # Deshabilitamos el botón de reiniciar

# Crear la ventana principal
root = tk.Tk()
app = AdivinarNumeroApp(root)

# Iniciar la aplicación
root.mainloop()
