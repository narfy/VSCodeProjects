
# Makes a grid 5 units high and 10 units wide
grid = []
for i in range(10):
    row = []
    for j in range(5):
        row.append([])
    grid.append(row)

# Prints the grid nicely
def printGrid():
    toPrint = ""
    for i in range(5):
        for j in range(10):
            position = grid[j][i]
            if len(position) == 0:
                toPrint += "_"
            elif len(position) == 1:
                toPrint += position[0].name
            else:
                toPrint += "X" # An X means a collision is happening!
            toPrint += "  "
        toPrint += "\n\n"
    print(toPrint)

# An object to put in the grid
# A Man has a name, x, y, and can move right
# (I have not dealt with the wall case)
class Man:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        grid[x][y].append(self)
    def moveRight(self):
        grid[self.x+1][self.y].append(self)
        grid[self.x][self.y].remove(self)
        self.x += 1

# Some instances of the Man object
man1 = Man("A", 1, 3)
man2 = Man("B", 5, 3)

# Demo - prints the grid and moves objects around
printGrid()
man1.moveRight()
printGrid()
man1.moveRight()
printGrid()
man1.moveRight()
printGrid()
man1.moveRight()
printGrid()