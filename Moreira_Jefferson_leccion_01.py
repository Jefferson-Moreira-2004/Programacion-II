import tkinter as tk
from tkinter import messagebox

# Clase Alumno: Representa a un alumno con sus atributos y métodos para calcular su calificación
class Alumno:
    def __init__(self, dni, apellidos, nombre, nota):
        # Inicializa los atributos del alumno: DNI, apellidos, nombre y nota
        self.dni = dni
        self.apellidos = apellidos
        self.nombre = nombre
        self.nota = nota
        self.calificacion = self.calcular_calificacion()  # Calcula la calificación automáticamente

    def calcular_calificacion(self):
        """Calcula la calificación de un alumno en función de su nota."""
        # Dependiendo de la nota, asignamos la calificación correspondiente
        if self.nota < 5:
            return 'SS'  # Suspenso
        elif 5 <= self.nota < 7:
            return 'AP'  # Aprobado
        elif 7 <= self.nota < 9:
            return 'NT'  # Notable
        else:
            return 'SB'  # Sobresaliente

    def __str__(self):
        """Devuelve la representación en texto del alumno para ser mostrada en la interfaz."""
        # Formato: DNI | APELLIDOS, NOMBRE | NOTA | CALIFICACIÓN
        return f"{self.dni:<10} {self.apellidos:<20}, {self.nombre:<20} {self.nota:<5} {self.calificacion}"

# Clase GestorAlumnos: Maneja las operaciones sobre los alumnos, como agregar, eliminar o modificar
class GestorAlumnos:
    def __init__(self):
        # Inicializamos un diccionario vacío para almacenar los alumnos, donde la clave es el DNI
        self.alumnos = {}

    def agregar_alumno(self, dni, apellidos, nombre, nota):
        """Agrega un nuevo alumno al sistema asegurándose de que no haya duplicados por DNI."""
        if dni in self.alumnos:
            return "El alumno con este DNI ya existe."  # Si el DNI ya está en uso, no se puede agregar
        alumno = Alumno(dni, apellidos, nombre, nota)  # Creamos un objeto Alumno
        self.alumnos[dni] = alumno  # Almacenamos al alumno en el diccionario usando su DNI como clave
        return f"Alumno {nombre} {apellidos} añadido con éxito."  # Mensaje de confirmación

    def eliminar_alumno(self, dni):
        """Elimina un alumno del sistema usando su DNI como referencia."""
        if dni in self.alumnos:
            del self.alumnos[dni]  # Elimina al alumno si el DNI existe
            return f"Alumno con DNI {dni} eliminado."  # Mensaje de confirmación
        return "No se encontró un alumno con ese DNI."  # Si el DNI no existe, mostramos un mensaje de error

    def modificar_nota(self, dni, nueva_nota):
        """Permite modificar la nota de un alumno especificado por su DNI."""
        if dni in self.alumnos:
            self.alumnos[dni].nota = nueva_nota  # Actualizamos la nota del alumno
            self.alumnos[dni].calificacion = self.alumnos[dni].calcular_calificacion()  # Recalculamos la calificación
            return f"Nota de {self.alumnos[dni].nombre} {self.alumnos[dni].apellidos} actualizada."
        return "Alumno no encontrado."  # Si no encontramos el alumno con ese DNI, mostramos un mensaje de error

    def obtener_alumnos(self):
        """Devuelve una lista con los alumnos registrados en formato texto."""
        return [str(alumno) for alumno in self.alumnos.values()]  # Genera una lista de cadenas con la información de los alumnos

# Clase Interfaz: Gestiona la parte gráfica de la aplicación usando Tkinter
class Interfaz:
    def __init__(self, root):
        self.root = root  # La ventana principal de la interfaz gráfica
        self.root.title("Gestión de Alumnos")  # Título de la ventana

        # Inicializamos el gestor de alumnos, que maneja las operaciones sobre los estudiantes
        self.gestor = GestorAlumnos()

        # Etiquetas para los campos de entrada de información (DNI, apellidos, etc.)
        self.lbl_dni = tk.Label(root, text="DNI:")
        self.lbl_dni.grid(row=0, column=0)
        self.lbl_apellidos = tk.Label(root, text="Apellidos:")
        self.lbl_apellidos.grid(row=1, column=0)
        self.lbl_nombre = tk.Label(root, text="Nombre:")
        self.lbl_nombre.grid(row=2, column=0)
        self.lbl_nota = tk.Label(root, text="Nota:")
        self.lbl_nota.grid(row=3, column=0)

        # Entradas de texto para capturar los datos del alumno
        self.entry_dni = tk.Entry(root)
        self.entry_dni.grid(row=0, column=1)
        self.entry_apellidos = tk.Entry(root)
        self.entry_apellidos.grid(row=1, column=1)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=2, column=1)
        self.entry_nota = tk.Entry(root)
        self.entry_nota.grid(row=3, column=1)

        # Lista donde se mostrarán los alumnos que haigan agregado.
        self.listbox_alumnos = tk.Listbox(root, width=80, height=10, selectmode=tk.SINGLE)
        self.listbox_alumnos.grid(row=4, column=0, columnspan=2, pady=10)
        self.listbox_alumnos.grid_forget()  # Ocultamos la lista al inicio

        # Botones que ejecutan las acciones correspondientes, osea botones interactivos
        self.btn_agregar = tk.Button(root, text="Agregar Alumno", command=self.agregar_alumno)
        self.btn_agregar.grid(row=5, column=0, pady=5)

        self.btn_eliminar = tk.Button(root, text="Eliminar Alumno", command=self.eliminar_alumno)
        self.btn_eliminar.grid(row=5, column=1, pady=5)

        self.btn_modificar = tk.Button(root, text="Modificar Nota", command=self.modificar_nota)
        self.btn_modificar.grid(row=6, column=0, pady=5)

        self.btn_mostrar = tk.Button(root, text="Mostrar Alumnos", command=self.mostrar_alumnos)
        self.btn_mostrar.grid(row=6, column=1, pady=5)

    def limpiar_campos(self):
        """Limpiar los campos de entrada de texto después de agregar un alumno."""
        self.entry_dni.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)

    def agregar_alumno(self):
        """Agrega un nuevo alumno con los datos introducidos en los campos de texto."""
        dni = self.entry_dni.get().strip()  # Recoge el DNI del alumno desde la entrada de texto y elimina espacios extra
        apellidos = self.entry_apellidos.get().strip()  # Recoge los apellidos del alumno
        nombre = self.entry_nombre.get().strip()  # Recoge el nombre del alumno
        try:
            # Intenta convertir la nota a un número flotante
            nota = float(self.entry_nota.get().strip())
        except ValueError:
            messagebox.showerror("Error", "La nota debe ser un número.")  # Si no es un número, mostramos un error
            return

        if 0 <= nota <= 10:
            # Si la nota está en el rango válido (0-10), se agrega el alumno
            mensaje = self.gestor.agregar_alumno(dni, apellidos, nombre, nota)
            messagebox.showinfo("Resultado", mensaje)  # Mostramos un mensaje de éxito
            self.limpiar_campos()  # Limpiamos los campos después de agregar al alumno
            self.listbox_alumnos.grid_forget()  # Ocultamos la lista hasta que el usuario la pida
        else:
            # Si la nota no está en el rango válido, mostramos un error
            messagebox.showerror("Error", "La nota debe estar entre 0 y 10.")

    def eliminar_alumno(self):
        """Elimina un alumno usando el DNI proporcionado en el campo de texto."""
        selected_index = self.listbox_alumnos.curselection()  # Obtiene el índice seleccionado
        if selected_index:
            alumno_str = self.listbox_alumnos.get(selected_index)  # Obtenemos el texto del alumno seleccionado
            dni = alumno_str.split()[0]  # El DNI está en la primera posición
            mensaje = self.gestor.eliminar_alumno(dni)  # Intenta eliminar al alumno
            messagebox.showinfo("Resultado", mensaje)  # Muestra el resultado de la operación
            self.mostrar_alumnos()  # Actualizamos la lista de alumnos
        else:
            messagebox.showwarning("Advertencia", "Selecciona un alumno para eliminar.")

    def modificar_nota(self):
        """Modifica la nota de un alumno dado su DNI y la nueva nota ingresada."""
        selected_index = self.listbox_alumnos.curselection()  # Obtiene el índice seleccionado
        if selected_index:
            alumno_str = self.listbox_alumnos.get(selected_index)  # Obtenemos el texto del alumno seleccionado
            dni = alumno_str.split()[0]  # El DNI está en la primera posición
            # Traemos el alumno del gestor y lo mostramos en los campos para modificar la nota
            try:
                nueva_nota = float(self.entry_nota.get().strip())  # Obtenemos la nueva nota desde el campo de texto
                if 0 <= nueva_nota <= 10:
                    mensaje = self.gestor.modificar_nota(dni, nueva_nota)  # Actualizamos la nota
                    messagebox.showinfo("Resultado", mensaje)  # Mostramos el resultado
                    self.limpiar_campos()  # Limpiamos los campos después de modificar
                    self.mostrar_alumnos()  # Actualizamos la lista de alumnos
                else:
                    messagebox.showerror("Error", "La nota debe estar entre 0 y 10.")
            except ValueError:
                messagebox.showerror("Error", "La nota debe ser un número.")
        else:
            messagebox.showwarning("Advertencia", "Selecciona un alumno para modificar la nota.")

    def mostrar_alumnos(self):
        """Muestra o esconde la lista de todos los alumnos registrados en la interfaz gráfica."""
        if self.listbox_alumnos.winfo_ismapped():  # Si la lista está visible
            self.listbox_alumnos.grid_forget()  # La ocultamos
        else:
            self.listbox_alumnos.delete(0, tk.END)  # Limpiamos la lista antes de actualizarla
            alumnos = self.gestor.obtener_alumnos()  # Obtenemos todos los alumnos como cadenas de texto
            for alumno in alumnos:
                # Insertamos cada alumno en el Listbox para que se muestren en la interfaz
                self.listbox_alumnos.insert(tk.END, alumno)
            self.listbox_alumnos.grid(row=4, column=0, columnspan=2, pady=10)  # La mostramos

# Función principal que ejecuta la aplicación de la interfaz gráfica
def main():
    root = tk.Tk()  # Creamos la ventana principal
    interfaz = Interfaz(root)  # Creamos una instancia de la interfaz
    root.mainloop()  # Ejecutamos el bucle principal de la interfaz gráfica

# Ejecutar el programa si se invoca este archivo
if __name__ == "__main__":
    main()
