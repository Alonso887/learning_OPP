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
        self.position_lists = [[],[],[],[],[],[],[],[]]
        
        #Extramethods
        for i in range(0,8):
            self.canvas.columnconfigure(i, minsize= 54)
            self.canvas.rowconfigure(i, minsize= 54)
        
        for i, k in [(i,k) for i in range(8) for k in range(8)]:
            empty_cell = Empty(self)
            empty_cell.position_piece(i, k)
            self.position_lists[i].append(empty_cell)            

#Sets an Empty Label in the board, is the Mother class for all the other pieces
class Empty():
    instances = []
    def __init__(self, container:Board):
        self.board = container
        self.container = container.canvas
        self.piece_image = tk.PhotoImage(file= r'assets\empty.png')

    def position_piece(self, row:int, column:int):
        self.Label = tk.Label(self.container, image= self.piece_image, background= "white", width= 48, height= 48)
        self.Label.bind('<Button-1>', self.select_piece)
        self.Label.grid(row= row, column= column)
        
        self.position = (row,column)
        if not type(self) is Empty:
            self.board.position_lists[row][column] = self
    
    def select_piece(self,event):
        pass

    #Clears all the cells in ALL of the boards    
    @staticmethod
    def clear_boards_background():
        for cell in Empty.instances:
            cell.Label.configure(background= 'white')

class Tower(Empty):
    colors = {'black':r'assets\black_tower.png','white':r'assets\white_tower.png'}
    instances = []
    def __init__(self, container, color:str):
        super().__init__(container= container)
        #Value asignation
        self.piece_image = tk.PhotoImage(file= Tower.colors[color])  
        #Extra methods
        Tower.instances.append(self)

    #Turns the background red and marks the posible moves for the piece
    def select_piece(self,event):
        self.clear_boards_background()
        self.Label.configure(background= 'red')
        self.check_movements('right')
        self.check_movements('left')
        self.check_movements('up')
        self.check_movements('down')
    
    def check_movements(self, direction:str):
        #YES, i just learned how to use coprehensions, what, You having problems comprehending?
        list_of_pieces = [Tower, Pawn]
        directions = {'up':[(row,self.position[1]) for row in range(self.position[0]+1,8)],
                      'down':[(row,self.position[1]) for row in range(self.position[0]-1,-1,-1)],
                      'right':[(self.position[0],column) for column in range(self.position[1]+1,8)],
                      'left':[(self.position[0],column) for column in range(self.position[1]-1,-1,-1)]}
        for row, column in directions[direction]:
            cell_to_check = self.board.position_lists[row][column]
            cell_to_check.Label.configure(background= 'yellow')
            if type(cell_to_check).__name__ == 'Empty':
                print(type(cell_to_check).__name__)
            else:
                break
    

class Pawn(Empty):
    colors = {'black':r'assets\black_pawn.png','white':r'assets\white_pawn.png'}
    instances = []
    def __init__(self, container, color:str):
        super().__init__(container)
        #Value asignation
        self.piece_image = tk.PhotoImage(file= Pawn.colors[color])
        #Extra methods
        Pawn.instances.append(self)

    def select_piece(self,event):
        self.clear_boards_background()
        self.Label.configure(background= 'red')

def main():
    root = tk.Tk()
    root.geometry("720x540")
    root.resizable(False,False)
    board = Board(root)
    for i in range(0,8):
        black_pawn = Tower(board, 'black')
        black_pawn.position_piece(row= 1, column= i)
        white_pawn = Pawn(board, 'white')
        white_pawn.position_piece(row= 6, column= i)

    a = Tower(board,'white')
    b = Tower(board,'white')

    a.position_piece(3,6)
    b.position_piece(3,4)
    
    root.mainloop()

if __name__ == "__main__":
    main()
