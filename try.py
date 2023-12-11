import tkinter as tk

def on_button_click(event):
    print("Botón clicado")

def desvincular_evento():
    # Verificar si el evento está vinculado antes de desvincularlo
    if ("<Button-1>", on_button_click) in boton.bind():
        boton.un
        print("Evento desvinculado")
    else:
        print("Evento no vinculado")

# Crear la ventana principal
ventana = tk.Tk()

# Crear un botón
boton = tk.Button(ventana, text="Clic aquí")

# Vincular el evento de clic izquierdo del ratón a la función on_button_click
boton.bind("<Button-1>", on_button_click)

# Crear un botón para desvincular el evento
boton_desvincular = tk.Button(ventana, text="Desvincular evento", command=desvincular_evento)

# Colocar los botones en la ventana
boton.pack(pady=20)
boton_desvincular.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
