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
        try:
            self.container = container.canvas
        except:
            self.container = container
        self.piece_image = tk.PhotoImage(file= r'assets\empty.png')
        self.color = ""

        self.instances.append(self)

    def position_piece(self, row:int, column:int):
        self.Label = tk.Label(self.container, image= self.piece_image, background= "white", width= 48, height= 48)
        self.Label.bind('<Button-1>', self.select_piece)
        self.Label.grid(row= row, column= column)
        
        # Position and directions need to be defined after positioning the piece
        self.position = (row,column)
        self.directions = {
            'NW':[(row, column) for row, column in zip(range(self.position[0]-1,-1,-1), range(self.position[1]-1,-1,-1))],
            'NE':[(row, column) for row, column in zip(range(self.position[0]-1,-1,-1), range(self.position[1]+1,8))],
            'SW':[(row, column) for row, column in zip(range(self.position[0]+1,8), range(self.position[1]-1,-1,-1))],
            'SE':[(row, column) for row, column in zip(range(self.position[0]+1,8), range(self.position[1]+1,8))],
            'N':[(row,self.position[1]) for row in range(self.position[0]+1,8)],
            'S':[(row,self.position[1]) for row in range(self.position[0]-1,-1,-1)],
            'E':[(self.position[0],column) for column in range(self.position[1]+1,8)],
            'W':[(self.position[0],column) for column in range(self.position[1]-1,-1,-1)],
            # The Tuple is in a list just because check_movements expects an iterable object
            # Also, this are the L movements from the horse
            'L1':[(self.position[0]-2, self.position[1]+1)],
            'L2':[(self.position[0]-1, self.position[1]+2)],
            'L3':[(self.position[0]+1, self.position[1]+2)],
            'L4':[(self.position[0]+2, self.position[1]+1)],
            'L5':[(self.position[0]+2, self.position[1]-1)],
            'L6':[(self.position[0]+1, self.position[1]-2)],
            'L7':[(self.position[0]-1, self.position[1]-2)],
            'L8':[(self.position[0]-2, self.position[1]-1)],
            }
        # YES, i just learned how to use coprehensions, what, You having problems comprehending?
        self.board.position_lists[row][column] = self
    
    def select_piece(self,event):
        pass

    def check_movements(self, direction:str):
        for row, column in self.directions[direction]:
            try:
                cell_to_check = self.board.position_lists[row][column]
            except IndexError: # L directions in self.directions can get out of range (Horses, Pawns)
                continue
            if cell_to_check.color is self.color:
                break 
            cell_to_check.Label.configure(background= 'yellow')
            cell_to_check.Label.bind('<Button-1>', lambda event, piece_eating=self, new_position=cell_to_check.position:
                                      cell_to_check.eat_piece(piece_eating,new_position,event))
            if not type(cell_to_check).__name__ == 'Empty':
                break
    
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


class Horse(Empty):
    colors = {'black':r'assets\black_horse.png','white':r'assets\white_horse.png'}
    def __init__(self, container: Board, color:str):
        super().__init__(container= container)
        # Value asignation  
        self.color = color
        self.piece_image = tk.PhotoImage(file= Horse.colors[color])
    
    def select_piece(self, event):
        self.board.clear_board()
        self.Label.configure(background= 'red')
        self.check_movements('L1')
        self.check_movements('L2')
        self.check_movements('L3')
        self.check_movements('L4')
        self.check_movements('L5')
        self.check_movements('L6')
        self.check_movements('L7')
        self.check_movements('L8')


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
        self.check_movements()
    
    def check_movements(self):
        # Each tuple is the position of the posible pawn movements divided in directions by colors 
        EAT_POSITIONS = {'black':[(self.position[0]+1,self.position[1]-1), (self.position[0]+1,self.position[1]+1)],
                         'white':[(self.position[0]-1,self.position[1]-1), (self.position[0]-1,self.position[1]+1)]}
        # This cicle detects if the pawn can or not eat a piece
        for row, column in EAT_POSITIONS.get(self.color):
            try:
                cell_to_check = self.board.position_lists[row][column]
            except IndexError: # Pawns can try to get values in the border of the board
                continue
            if type(cell_to_check) is Empty:
                continue
            if cell_to_check.color is self.color:
                continue 
            cell_to_check.Label.configure(background= 'yellow')
            cell_to_check.Label.bind('<Button-1>', lambda event, piece_eating=self, new_position=cell_to_check.position:
                                      cell_to_check.eat_piece(piece_eating,new_position,event))
        # This part checks for the front position
        MOVE_POSITIONS = {'black':(self.position[0]+1,self.position[1]),
                          'white':(self.position[0]-1, self.position[1])}
        row = MOVE_POSITIONS.get(self.color)[0]
        column = MOVE_POSITIONS.get(self.color)[1]
        if type(self.board.position_lists[row][column]) is not Empty:
            pass
        else:
            cell_to_check = self.board.position_lists[row][column]
            cell_to_check.Label.configure(background= 'yellow')
            cell_to_check.Label.bind('<Button-1>', lambda event, piece_eating=self, new_position=cell_to_check.position:
                                    cell_to_check.eat_piece(piece_eating,new_position,event))
        # This part checks if it's the first turn so the pawn can move 2 cells
        if self.color == 'black' and self.position[0] == 1:
            if type(self.board.position_lists[self.position[0]+2][column]) is not Empty:
                pass
            else:
                cell_to_check = self.board.position_lists[self.position[0]+2][column]
                cell_to_check.Label.configure(background= 'yellow')
                cell_to_check.Label.bind('<Button-1>', lambda event, piece_eating=self, new_position=cell_to_check.position:
                                        cell_to_check.eat_piece(piece_eating,new_position,event))
        if self.color == 'white' and self.position[0] == 6:
            if type(self.board.position_lists[self.position[0]-2][column]) is not Empty:
                pass
            else:
                cell_to_check = self.board.position_lists[self.position[0]-2][column]
                cell_to_check.Label.configure(background= 'yellow')
                cell_to_check.Label.bind('<Button-1>', lambda event, piece_eating=self, new_position=cell_to_check.position:
                                        cell_to_check.eat_piece(piece_eating,new_position,event))
        # This part checks for color if the pawn can crown
        if self.color == 'black' and self.position[0] == 7:
            new_queen = Queen(self.board, self.color)
            new_queen.position_piece(self.position[0],self.position[1])
        if self.color == 'white' and self.position[0] == 0:
            new_queen = Queen(self.board, self.color)
            new_queen.position_piece(self.position[0],self.position[1])

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
    b = Horse(board, 'black')

    c.position_piece(3,5)
    a.position_piece(4,2)
    b.position_piece(4,3)
    
    root.mainloop()

if __name__ == "__main__":
    main()
