import tkinter as tk
from tkinter import ttk

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
    
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.bind("<Configure>", lambda e: self.on_frame_configure())

    def on_frame_configure(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

# Crear la aplicación
app = tk.Tk()
app.title("Ejemplo Scrollable Frame")

# Crear frames superior e inferior
frame_top = tk.Frame(app, height=50, bg="lightblue")
frame_top.pack(fill="x")

frame_bottom = tk.Frame(app, height=50, bg="lightgreen")
frame_bottom.pack(side="bottom", fill="x")

# Crear el frame scrollable en el medio
scrollable_frame = ScrollableFrame(app)
scrollable_frame.pack(fill="both", expand=True)

# Agregar algunos frames con etiquetas al frame scrollable
for i in range(20):
    frame_inside = tk.Frame(scrollable_frame.scrollable_frame, bd=2, relief="solid")
    frame_inside.pack(pady=10, padx=10)
    label = tk.Label(frame_inside, text=f"Etiqueta {i}")
    label.pack()

# Iniciar la aplicación
app.mainloop()