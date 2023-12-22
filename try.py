import tkinter as tk
from tkinter import ttk

# Función para agregar más contenido al canvas
def agregar_contenido():
    frame_contenido.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Scrolling en Canvas")

# Crear un canvas
canvas = tk.Canvas(ventana, borderwidth=0, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

# Añadir un scrollbar al canvas
scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Crear un frame dentro del canvas
frame_contenido = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame_contenido, anchor="nw")

# Configurar el tamaño del Canvas
canvas.config(width=400, height=300)  # Ajusta estos valores según tus necesidades

# Configurar el tamaño del Frame y permitir la expansión en x
frame_contenido.pack(fill="both", expand=True)

# Agregar algunos widgets al frame
for i in range(20):
    ttk.Label(frame_contenido, text=f"Etiqueta {i}").pack()

# Botón para agregar más contenido al canvas dinámicamente
boton_agregar = ttk.Button(ventana, text="Agregar más contenido", command=agregar_contenido)
boton_agregar.pack(pady=10)

# Configurar el canvas para que se expanda con el cambio de tamaño de la ventana
ventana.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Iniciar el bucle principal
ventana.mainloop()
