class Empty():
      def __init__(self) -> None:
            pass

class Tower(Empty):
      def __init__(self) -> None:
            super().__init__()

position = (3,4)
position_lists = [[],[],[],[],[],[],[],[]]

for i, k in [(i,k) for i in range(8) for k in range(8)]:
            empty_cell = Empty()
            position_lists[i].append(empty_cell)

position_lists[3][6] = Tower()
directions = {'right':[(x,position[1]) for x in range(position[0]+1,8)],
              'left':[(x,position[1]) for x in range(position[0]-1,-1,-1)],
              'up':[(position[0],y) for y in range(position[1]+1,8)],
              'down':[(position[0],y) for y in range(position[1]-1,-1,-1)]}

def cola(direction: str):
    for x, y in directions[direction]:
        cell_to_check = position_lists[x][y]
        if type(cell_to_check) is Empty:
            print(f"{direction} {x} and {y}")
        else:
            break

cola('right')
cola('left')
cola('up')
cola('down')