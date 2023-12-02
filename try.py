import tkinter as tk

def configurar_label(row, column):
    # Obtener la referencia a la Label en la posición dada
    label = labels[(row, column)]

    # Configurar propiedades de la Label
    label.config(text=f"Label en ({row}, {column})", bg="lightblue", padx=10, pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Configuración de Labels en un Canvas")

# Crear un Canvas
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Crear Labels y colocarlos en el Canvas usando grid
labels = {}
for i in range(3):
    for j in range(3):
        label = tk.Label(canvas, text=f"Label en ({i}, {j})", borderwidth=2, relief="solid")
        label.grid(row=i, column=j, padx=5, pady=5)
        labels[(i, j)] = label

# Configurar la Label en la posición (1, 1)
configurar_label(1, 1)

# Puedes llamar a la función configurar_label para otras posiciones según sea necesario

# Iniciar el bucle principal de la aplicación
root.mainloop()
