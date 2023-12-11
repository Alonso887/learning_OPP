r = 3
d = 5

comp = [(row,column) for row, column in zip(range(r-1,-1,-1),range(d-1,-1,-1))]

for row, column in comp:
    print(row,column)
