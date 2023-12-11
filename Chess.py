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
        self.position_lists = [[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],
                               [0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]]
        self.color_turn = "white"

        #Extramethods
        for i in range(0,8):
            self.canvas.columnconfigure(i, minsize= 54)
            self.canvas.rowconfigure(i, minsize= 54)
        
        for i, k in [(i,k) for i in range(8) for k in range(8)]:
            empty_cell = Empty(self)
            empty_cell.position_piece(i, k)  

    def clear_board(self):
        for i, k in [(i,k) for i in range(8) for k in range(8)]:
            cell_to_clear = self.position_lists[i][k]
            cell_to_clear.Label.configure(background= 'white')

    def next_turn(self):
        if self.color_turn == "black":
            for i, k in [(i,k) for i in range(8) for k in range(8)]:
                cell_to_check = self.position_lists[i][k]
                cell_to_check.check_turn()
                self.color_turn = "white"
        elif self.color_turn == "white":
            for i, k in [(i,k) for i in range(8) for k in range(8)]:
                cell_to_check = self.position_lists[i][k]
                cell_to_check.check_turn()
                self.color_turn = "black"


#Sets an Empty Label in the board, is the Mother class for all the other pieces
class Empty():
    instances = []
    def __init__(self, container:Board):
        self.board = container
        self.container = container.canvas
        self.piece_image = tk.PhotoImage(file= r'assets\empty.png')
        self.color = ""

        self.instances.append(self)

    def position_piece(self, row:int, column:int):
        self.Label = tk.Label(self.container, image= self.piece_image, background= "white", width= 48, height= 48)
        self.Label.bind('<Button-1>', self.select_piece)
        self.Label.grid(row= row, column= column)
        
        self.position = (row,column)
        self.board.position_lists[row][column] = self
    
    def select_piece(self,event):
        pass

    def check_turn(self):
        if self.board.color_turn == self.color:
            self.Label.bind('<Button-1>', self.select_piece)
        elif self.board.color_turn != self.color:
            self.Label.unbind('<Button-1>')

    def eat_piece(self,piece_eating,new_position,event):
        original_position  = piece_eating.position
        new_empty = Empty(self.board)
        new_empty.position_piece(original_position[0],original_position[1])
        piece_eating.position_piece(new_position[0],new_position[1])

        for i,k in [(i,k) for i in range(8) for k in range(8)]:
            cell = self.board.position_lists[i][i]
            cell.Label.unbind('<Button-1>')
        self.board.clear_board()
        self.board.next_turn()


class Tower(Empty):
    colors = {'black':r'assets\black_tower.png','white':r'assets\white_tower.png'}
    def __init__(self, container: Board, color:str):
        super().__init__(container= container)
        #Value asignation
        self.color = color
        self.piece_image = tk.PhotoImage(file= Tower.colors[color])  

    #Turns the background red and marks the posible moves for the piece
    def select_piece(self,event):
        self.board.clear_board()
        self.Label.configure(background= 'red')
        self.check_movements('N')
        self.check_movements('S')
        self.check_movements('E')
        self.check_movements('W')
    
    def check_movements(self, direction:str):
        #YES, i just learned how to use coprehensions, what, You having problems comprehending?
        directions = {'N':[(row,self.position[1]) for row in range(self.position[0]+1,8)],
                      'S':[(row,self.position[1]) for row in range(self.position[0]-1,-1,-1)],
                      'E':[(self.position[0],column) for column in range(self.position[1]+1,8)],
                      'W':[(self.position[0],column) for column in range(self.position[1]-1,-1,-1)]}
        for row, column in directions[direction]:
            cell_to_check = self.board.position_lists[row][column]
            if cell_to_check.color is self.color:
                break 
            cell_to_check.Label.configure(background= 'yellow')
            cell_to_check.Label.bind('<Button-1>', lambda event, piece_eating=self, new_position=cell_to_check.position:
                                      cell_to_check.eat_piece(piece_eating,new_position,event))
            if not type(cell_to_check).__name__ == 'Empty': 
                break


class Bishop(Empty):
    colors = {'black':r'assets\black_bishop.png', 'white':r'assets\white_bishop.png'}
    def __init__(self, container: Board, color:str):
        super().__init__(container= container)
        #Value assignation
        self.color = color
        self.piece_image = tk.PhotoImage(file= Bishop.colors[color])
    
    def select_piece(self,event):
        self.board.clear_board()
        self.Label.configure(background= 'red')
        self.check_movements('NE')
        self.check_movements('NW')
        self.check_movements('SE')
        self.check_movements('SW')

    def check_movements(self, direction:str):
        directions = {'NW':[(row, column) for row, column in zip(range(self.position[0]-1,-1,-1), range(self.position[1]-1,-1,-1))],
                      'NE':[(row, column) for row, column in zip(range(self.position[0]-1,-1,-1), range(self.position[1]+1,8))],
                      'SW':[(row, column) for row, column in zip(range(self.position[0]+1,8), range(self.position[1]-1,-1,-1))],
                      'SE':[(row, column) for row, column in zip(range(self.position[0]+1,8), range(self.position[1]+1,8))],}
        for row, column in directions[direction]:
            cell_to_check = self.board.position_lists[row][column]
            if cell_to_check.color is self.color:
                break 
            cell_to_check.Label.configure(background= 'yellow')
            cell_to_check.Label.bind('<Button-1>', lambda event, piece_eating=self, new_position=cell_to_check.position:
                                      cell_to_check.eat_piece(piece_eating,new_position,event))
            if not type(cell_to_check).__name__ == 'Empty': 
                break


class Queen(Empty):
    colors = {'black':r'assets\black_queen.png', 'white':r'assets\white_queen.png'}
    def __init__(self, container: Board, color:str):
        super().__init__(container= container)
        #Value asignation
        self.color = color
        self.piece_image = tk.PhotoImage(file= Queen.colors[color])

    def select_piece(self, event):
        self.board.clear_board()
        self.Label.configure(background= 'red')
        self.check_movements('NW')
        self.check_movements('NE')
        self.check_movements('SW')
        self.check_movements('SE')
        self.check_movements('N')
        self.check_movements('S')
        self.check_movements('E')
        self.check_movements('W')

    def check_movements(self, direction:str):
        directions = {'NW':[(row, column) for row, column in zip(range(self.position[0]-1,-1,-1), range(self.position[1]-1,-1,-1))],
                      'NE':[(row, column) for row, column in zip(range(self.position[0]-1,-1,-1), range(self.position[1]+1,8))],
                      'SW':[(row, column) for row, column in zip(range(self.position[0]+1,8), range(self.position[1]-1,-1,-1))],
                      'SE':[(row, column) for row, column in zip(range(self.position[0]+1,8), range(self.position[1]+1,8))],
                      'N':[(row,self.position[1]) for row in range(self.position[0]+1,8)],
                      'S':[(row,self.position[1]) for row in range(self.position[0]-1,-1,-1)],
                      'E':[(self.position[0],column) for column in range(self.position[1]+1,8)],
                      'W':[(self.position[0],column) for column in range(self.position[1]-1,-1,-1)]}
        for row, column in directions[direction]:
            cell_to_check = self.board.position_lists[row][column]
            if cell_to_check.color is self.color:
                break 
            cell_to_check.Label.configure(background= 'yellow')
            cell_to_check.Label.bind('<Button-1>', lambda event, piece_eating=self, new_position=cell_to_check.position:
                                     cell_to_check.eat_piece(piece_eating,new_position,event))
            if not type(cell_to_check).__name__ == 'Empty': 
                break


class Pawn(Empty):
    colors = {'black':r'assets\black_pawn.png','white':r'assets\white_pawn.png'}
    instances = []
    def __init__(self, container, color:str):
        super().__init__(container)
        #Value asignation
        self.color = color
        self.piece_image = tk.PhotoImage(file= Pawn.colors[color])
        #Extra methods
        Pawn.instances.append(self)

    def select_piece(self,event):
        self.board.clear_board()
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

    c = Queen(board, 'black')
    a = Bishop(board, 'white')

    c.position_piece(3,5)
    a.position_piece(4,2)
    
    root.mainloop()

if __name__ == "__main__":
    main()
