import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Básica")  # Título de la ventana
        self.root.geometry("400x500")  # Definir el tamaño de la ventana
        self.root.config(bg="#f5f5f5")  # Establecer un fondo beige suave para la interfaz

        # Variable que almacenará la expresión matemática actual
        self.expresion = ""

        # Llamada a la función que crea todos los elementos visuales (widgets) de la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        """Crea los elementos visuales de la interfaz, como la pantalla y los botones."""
        # Crear la entrada de texto (pantalla) donde se mostrará la expresión y el resultado
        self.resultado = tk.Entry(self.root, font=("Times New Roman", 20), width=15, borderwidth=2, relief="solid", bg="white", fg="black", justify="right")
        self.resultado.grid(row=0, column=0, columnspan=4, pady=20)  # Posicionar la pantalla en la cuadrícula

        # Lista de los botones y su ubicación en la cuadrícula
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Crear cada botón con su texto y ubicación, y asignarles una acción al hacer clic
        for (texto, fila, col) in botones:
            button = tk.Button(self.root, text=texto, font=("Times New Roman", 18), width=5, height=2, bg="#b3e0ff", fg="black", relief="solid", command=lambda t=texto: self.on_click(t))
            button.grid(row=fila, column=col, padx=5, pady=5)  # Posicionar cada botón en su lugar

    def on_click(self, texto):
        """Esta función maneja lo que ocurre cuando se presiona un botón de la calculadora."""
        if texto == "C":
            # Si se presiona "C", limpiamos la pantalla y reiniciamos la expresión
            self.expresion = ""
            self.resultado.delete(0, tk.END)  # Limpiar la pantalla de la calculadora
        elif texto == "=":
            # Si se presiona "=", evaluamos la expresión y mostramos el resultado
            try:
                # Reemplazamos los símbolos de división y multiplicación por sus equivalentes en Python
                self.expresion = self.expresion.replace("÷", "/").replace("×", "*")
                resultado = str(eval(self.expresion))  # Evaluar la expresión matemática
                self.resultado.delete(0, tk.END)  # Limpiar la pantalla antes de mostrar el resultado
                self.resultado.insert(tk.END, resultado)  # Insertar el resultado en la pantalla
                self.expresion = resultado  # Actualizar la expresión para permitir más operaciones
            except Exception as e:
                # Si ocurre un error durante la evaluación, mostramos "Error" en la pantalla
                self.resultado.delete(0, tk.END)
                self.resultado.insert(tk.END, "Error")
                self.expresion = ""  # Reiniciar la expresión en caso de error
        else:
            # Si es otro botón, simplemente agregamos el texto a la expresión
            self.expresion += texto
            self.resultado.delete(0, tk.END)  # Limpiar la pantalla para mostrar la nueva expresión
            self.resultado.insert(tk.END, self.expresion)  # Insertar la nueva expresión

# Crear la ventana principal de la aplicación
root = tk.Tk()
app = Calculadora(root)

# Iniciar el bucle principal de la aplicación, que mantendrá la ventana abierta
root.mainloop()
