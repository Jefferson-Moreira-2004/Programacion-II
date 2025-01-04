import tkinter as tk
import random

class JuegoPiedraPapelTijera:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")  # Título de la ventana
        self.root.geometry("600x400")  # Tamaño de la ventana para que se vea bien
        self.root.config(bg="#e0e0e0")  # Fondo gris claro para darle un toque moderno

        # Inicializamos las variables de puntuación
        self.puntuacion_jugador = 0
        self.puntuacion_pc = 0

        # Llamamos a la función para crear los elementos de la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        """Creación de los elementos visuales de la interfaz: etiquetas, botones y resultados."""
        # Título principal de la ventana
        self.titulo = tk.Label(self.root, text="Piedra, Papel o Tijera?", font=("Times New Roman", 24, "bold"), bg="#e0e0e0", fg="#333333")
        self.titulo.grid(row=0, column=1, pady=20)  # Centrado en la ventana con un poco de espacio

        # Sección de la interfaz donde se muestran las elecciones del jugador y la computadora
        self.jugador_label = tk.Label(self.root, text="Jugador:", font=("Arial", 14), bg="#e0e0e0", fg="#333333")
        self.jugador_label.grid(row=1, column=0, padx=20, sticky="e")  # Etiqueta de "Jugador", alineada a la derecha
        
        self.pc_label = tk.Label(self.root, text="PC:", font=("Arial", 14), bg="#e0e0e0", fg="#333333")
        self.pc_label.grid(row=2, column=0, padx=20, sticky="e")  # Etiqueta de "PC", alineada a la derecha
        
        # Mostramos las elecciones del jugador y la PC (por ahora vacías)
        self.eleccion_jugador = tk.Label(self.root, text="-", font=("Arial", 14), bg="#e0e0e0", fg="#333333")
        self.eleccion_jugador.grid(row=1, column=1, padx=20)

        self.eleccion_pc = tk.Label(self.root, text="-", font=("Arial", 14), bg="#e0e0e0", fg="#333333")
        self.eleccion_pc.grid(row=2, column=1, padx=20)

        # Botones para que el jugador elija entre Piedra, Papel o Tijera
        self.boton_piedra = tk.Button(self.root, text="Piedra", width=15, height=2, font=("Times New Roman", 15), command=lambda: self.jugar("Piedra"), bg="#66bb6a", fg="white", relief="solid")
        self.boton_piedra.grid(row=1, column=2, pady=10)

        self.boton_papel = tk.Button(self.root, text="Papel", width=15, height=2, font=("Times New Roman", 15), command=lambda: self.jugar("Papel"), bg="#42a5f5", fg="white", relief="solid")
        self.boton_papel.grid(row=2, column=2, pady=10)

        self.boton_tijera = tk.Button(self.root, text="Tijera", width=15, height=2, font=("Times New Roman", 15), command=lambda: self.jugar("Tijera"), bg="#ab47bc", fg="white", relief="solid")
        self.boton_tijera.grid(row=3, column=2, pady=10)

        # Sección para mostrar el resultado del juego (victoria, derrota o empate)
        self.resultado = tk.Label(self.root, text="EMPEZAMOS :)", font=("Times New Roman", 20), bg="#42a5f5", fg="white")
        self.resultado.grid(row=4, column=0, columnspan=3, pady=20)

        # Puntuaciones del jugador y la computadora
        self.puntuacion_label = tk.Label(self.root, text="Puntuaciones (°o°)", font=("Arial", 18), bg="#e0e0e0", fg="#333333")
        self.puntuacion_label.grid(row=5, column=0, columnspan=3, pady=10)

        self.puntuacion_jugador_label = tk.Label(self.root, text="Jugador: 0", font=("Arial", 16), bg="#e0e0e0", fg="#333333")
        self.puntuacion_jugador_label.grid(row=6, column=0, padx=20, sticky="e")

        self.puntuacion_pc_label = tk.Label(self.root, text="PC: 0", font=("Arial", 16), bg="#e0e0e0", fg="#333333")
        self.puntuacion_pc_label.grid(row=6, column=1, padx=20)

    def jugar(self, eleccion_jugador):
        """Lógica principal del juego. Se ejecuta cuando el jugador elige Piedra, Papel o Tijera."""
        # La computadora elige aleatoriamente entre Piedra, Papel y Tijera
        opciones = ["Piedra", "Papel", "Tijera"]
        eleccion_pc = random.choice(opciones)

        # Actualizamos las etiquetas con las elecciones del jugador y de la PC
        self.eleccion_jugador.config(text=eleccion_jugador)
        self.eleccion_pc.config(text=eleccion_pc)

        # Determinamos el resultado del juego
        resultado = self.determinar_resultado(eleccion_jugador, eleccion_pc)

        # Actualizamos el mensaje con el resultado
        self.resultado.config(text=resultado, bg="#42a5f5", fg="white")

        # Actualizamos las puntuaciones dependiendo del resultado
        if resultado == "¡Ganaste!":
            self.puntuacion_jugador += 1
        elif resultado == "¡Perdiste!":
            self.puntuacion_pc += 1

        # Mostramos las puntuaciones actualizadas en la interfaz
        self.puntuacion_jugador_label.config(text=f"Jugador: {self.puntuacion_jugador}")
        self.puntuacion_pc_label.config(text=f"PC: {self.puntuacion_pc}")

    def determinar_resultado(self, jugador, pc):
        """Determina el resultado del juego según las reglas básicas: Piedra vence a Tijera, Tijera vence a Papel, y Papel vence a Piedra."""
        if jugador == pc:
            return "Empate!"
        elif (jugador == "Piedra" and pc == "Tijera") or (jugador == "Tijera" and pc == "Papel") or (jugador == "Papel" and pc == "Piedra"):
            return "¡Ganaste!"
        else:
            return "¡Perdiste!"

# Crear la ventana principal de la aplicación
root = tk.Tk()
app = JuegoPiedraPapelTijera(root)

# Iniciar la aplicación y mostrar la ventana
root.mainloop()
