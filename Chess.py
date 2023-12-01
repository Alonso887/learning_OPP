import tkinter as tk
from tkinter import ttk

#Sets a Canvas with the needed proportions, i think it's unnecesarie to use a class for this
# But i'm doing it to learn i guess 
class Board():
    def __init__(self, container):
        #Value asignation
        self.container = container
        self.canvas = tk.Canvas(self.container,height= 480, width= 480, background= "black", highlightbackground="black")
        self.canvas.place(x= 360, y= 270, anchor= tk.CENTER)
        
        #Extramethods
        for i in range(0,8):
            self.canvas.columnconfigure(i, minsize= 54)
            self.canvas.rowconfigure(i, minsize= 54)

        #This sets a blank image to all the cellsin the board
        for i in range(0,8):
            for k in range(0,8):
                empty_cell = Empty(self)
                empty_cell.position_piece(i, k)

#Sets an Empty Label in the board, is the Mother class for all the other pieces
class Empty():
    def __init__(self, container):
        self.container = container.canvas
        self.image_file = r'assets\empty.png'

    def position_piece(self, row:int, column:int):
        self.piece_image = tk.PhotoImage(file= self.image_file)
        self.Label = tk.Label(self.container, image= self.piece_image, background= "white", text="a")
        self.Label.grid(row= row, column= column)
        #Sets the postion given as an atribute of the instance so its position in the board
        #can be used later when 
        self.row = row
        self.column = column

class Tower(Empty):
    colors = {'black':r'assets\black_tower.png','white':r'assets\white_tower.png'}
    instances = []
    def __init__(self, container, color:str):
        super().__init__(container= container)
        #Value asignation
        self.image_file = Tower.colors[color]  
        #Extra methods
        Tower.instances.append(self)

class Pawn(Empty):
    colors = {'black':r'assets\black_pawn.png','white':r'assets\white_pawn.png'}
    instances = []
    def __init__(self, container, color:str):
        super().__init__(container)
        #Value asignation
        self.image_file = Pawn.colors[color]
        #Extra methods
        Pawn.instances.append(self)


def main():
    root = tk.Tk()
    root.geometry("720x540")
    root.resizable(False,False)
    board = Board(root)
    for i in range(0,8):
        black_pawn = Pawn(board, 'black')
        black_pawn.position_piece(row= 1, column= i)
        white_pawn = Pawn(board, 'white')
        white_pawn.position_piece(row= 6, column= i)
    
    root.mainloop()

if __name__ == "__main__":
    main()
