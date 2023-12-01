import tkinter as tk 

root = tk.Tk()
root.geometry("720x540")
root.resizable(False,False)

canvas = tk.Canvas(root, height= 480, width= 480, background= "black", highlightbackground="black")
canvas.place(x= 360, y= 270, anchor= tk.CENTER)
for i in range(0,8):
    canvas.columnconfigure(i, minsize= 54)
    canvas.rowconfigure(i, minsize= 54)

foto = tk.PhotoImage(file=r'C:\Users\aadri\Desktop\Coding\Repositories\learning_OOP\assets\white_pawn.png')

for i in range(0,8):
    for k in range(0,8):
        Label1 = tk.Label(canvas, background= "white", image= foto)
        Label1.grid(column= i, row= k)



root.mainloop()
#1-Parrafo de presentacion-Alonso
#2-Sintomas-Alonso
#3-Factores de riesgo-Johan
#4-Estadisticas-Johan
#5-Tratamientos-Felix