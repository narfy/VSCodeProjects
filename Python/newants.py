import turtle
import time
import random

preSet = False
edit = False

preSetinp = input("Do you want a pre decided set up for the settings or do you want the editor? yes, no, editor (The editor will provide exta info to help with problems).\n")

if preSetinp == "yes":
    preSet = True

if preSetinp == "editor":
    edit = True

delay = 0

if preSet == False:
    delay = input("How fast do you want the Ants to move? 0 is fastest, 20 will be VERY slow.\n")
    delay = int(delay)

t = turtle.Turtle()
t.hideturtle()
turtle.delay(delay)
turtle.Screen().bgcolor(0,0,0)

global stop
stop = 0

colors = ["Red", "Blue", "Yellow", "Orange", "Green", "Purple", "Brown", "Azure", "Ivory", "Teal", "Silver", "Gray", "Cyan", "Maroon", "Lime", "Pink", "Olive", "Tan", "Coral", "Light green", "Light blue", "Magenta", "Violet", "Gold", "Crimson", "Dark green"]

allAnts = {}
bases ={}

grid = []

grid1 = 5

if preSet == False:
    grid1 = input("How far do you want the ants to spawn away from each other? Please use whole numbers.\n")
    grid1 = int(grid1)

grid2 = 1
grid2 = grid1 * -1

spawn1 = grid1 * 40
spawn2 = grid2 * 40

grid1 = grid1 + 500
grid2 = grid2 + 500

# creats the grid
for i in range(1000):
    row = []

    for j in range(1000):
        row.append([])
    grid.append(row)

# prints the grid
def printGrid():
    toPrint = ""

    for i in range(100):

        for j in range(100):

            position = grid[j][i]
            if len(position) == 0:
                toPrint += "_"

            elif len(position) == 1:
                toPrint += position[0].name

            else:
                toPrint += "X" # An X means a collision is happening!
            toPrint += "  "

        toPrint += "\n\n"
        
    #print(toPrint)

# An object to put in the grid
class Ant:

    def __init__(self, name, c):

        self.t = turtle.Turtle()
        self.t.speed(100)
        self.t.color(c)
        self.name = name

        # sets cords for base ant
        if name == "bA":

            self.x = 0
            self.y = 0

        # makes ants spawn at their bases
        else:

            self.x = int(bases[name][0] / 40)
            self.y = int(bases[name][1] / 40)

            self.t.penup()
            self.t.goto(bases[name][0], bases[name][1])
            self.t.pendown()

            grid[self.x][self.y].append(self)

    # Draws a box on the grid
    def box(self):

        self.t.color("white")
        self.t.begin_fill()
        self.t.forward(-3)
        self.t.left(90)
        self.t.forward(3)
        for i in range(3):
            self.t.right(90)
            self.t.forward(6)
        self.t.right(90)
        self.t.forward(3)
        self.t.right(90)
        self.t.forward(3)
        self.t.end_fill()

    # draws a base
    def base(self):

        self.t.begin_fill()
        self.t.forward(10)
        self.t.left(90)
        self.t.forward(10)
        for i in range(3):
            self.t.left(90)
            self.t.forward(20)
        self.t.left(90)
        self.t.forward(10)
        self.t.left(90)
        self.t.forward(10)
        self.t.end_fill()

    # gives instructions to the base building ant
    def baseSpawn(self, i):
        
        self.t.penup()
        self.t.goto(0,0)
        self.t.color(colors[i])
        self.t.setheading(i * spawnPos)
        self.t.forward(spawn1)
        self.t.setheading(0)
        x = int(self.t.xcor())
        roundedx = x - (x % 40)
        y = int(self.t.ycor())
        roundedy = y - (y % 40)
        bases[chr(i + 65)] = [roundedx, roundedy, False]
        self.t.goto(roundedx, roundedy)
        self.t.pendown()
        self.base()
        self.t.penup

        if edit == True:
            print("\n", i * spawnPos, "\n")
        
    # decides how the ants move
    def move(self):

        #r1 = random.randint(1,4)
        r1 = 5

        if edit == True:

            print("\n", self.t.xcor(), self.t.ycor(), "\n")

        if r1 == 1:
            self.moveRight()
        if r1 == 2:
            self.moveLeft()
        if r1 == 3:
            self.moveUp()
        if r1 == 4:
            self.moveDown()
        if r1 == 5:
            self.move1Base()

        if edit == True:

            print("\n", self.t.xcor(), self.t.ycor(), "\n")

    # moves right
    def moveRight(self):
        grid[self.x+1][self.y].append(self)
        grid[self.x][self.y].remove(self)
        self.x += 1

        self.t.setheading(0)
        self.t.forward(40)

    # moves left
    def moveLeft(self):
        grid[self.x-1][self.y].append(self)
        grid[self.x][self.y].remove(self)
        self.x -= 1

        self.t.setheading(180)
        self.t.forward(40)

    # moves up
    def moveUp(self):
        grid[self.x][self.y+1].append(self)
        grid[self.x][self.y].remove(self)
        self.y += 1

        self.t.setheading(90)
        self.t.forward(40)

    #moves down
    def moveDown(self):
        grid[self.x][self.y-1].append(self)
        grid[self.x][self.y].remove(self)
        self.y -= 1

        self.t.setheading(270)
        self.t.forward(40)

    def move1Base(self):

        xcordSaved = 100000
        ycordSaved = 100000
        cordXYSaved = 100000
        cordXY = 0
        xcordAbs = 0
        ycordAbs = 0
 
        for key in bases:

            if self.name != key and bases[key][2] == False:

                xcordClose = int(bases[key][0])
                ycordClose = int(bases[key][1]) 

                xcordAbs = abs(self.t.xcor() - xcordClose)
                ycordAbs = abs(self.t.ycor() - ycordClose)
                cordXY = xcordAbs + ycordAbs


                if cordXY < cordXYSaved:

                    xcordSaved = xcordClose
                    ycordSaved = ycordClose
                    cordXYSaved = cordXY

        r2 = random.randint(1,2)

        if r2 == 2:


            if self.t.ycor() < ycordSaved:

                self.moveUp()

            else:

                self.moveDown()

        if r2 == 1:

            if self.t.xcor() < xcordSaved:

                self.moveRight()

            else:

                self.moveLeft()

    def move2Base(self):

        r2 = random.randint(1,2)

        if r2 == 2:

            if self.x > 0:
                if self.y < 0:
                    self.moveDown()
                else:
                    self.moveUp()
            else:
                r2 = 1

        if r2 == 1:

            if self.x < grid1:
                self.moveRight()
            else:
                self.moveLeft()
    
    # kills ants 
    def death(self):

        group = grid[self.x][self.y]

        deathF = False

        for i in range(len(group)):

            if group[i].name != self.name:

                deathF = True
            
        if deathF:  #crA = currentAnt crAN = currentAntName    

                for j in range(len(group)):

                    crA = group[j]
                    crAN = crA.name

                    if len(allAnts[crAN]) == 0: continue

                    group[j].t.color("white")

                    if edit == True:
                        print("\n",allAnts[crAN], crA, "\n")

                    allAnts[crAN].remove(crA)
                    self.box()
                    print("Death")

                    if edit == True:
                        print("\n", crAN, "\n")

                grid[self.x][self.y].clear()
        
    # apoints a winner
    def win(self):

        winCount = 0
        colorFind = 0

        for key in bases:

            if self.name != key:

                if edit == True:
                    print("\n base x: ", int(bases[key][0]), "   base y:", int(bases[key][1]))
                    print("\n ant x: ", round(self.t.xcor()), "   ant y:", round(self.t.ycor()), "\n")
                    
                if int(bases[key][0]) == round(self.t.xcor()):

                    if int(bases[key][1]) == round(self.t.ycor()):

                        bases[key][2] = True

                        for i in range (len(allAnts[key])):

                            allAnts[key][i].box()

                        allAnts[key].clear()

        for key in bases:

            if bases[key][2] == True: # I am not doing boolean zen

                winCount = winCount + 1
            
            if winCount == numBase - 1:

                for key in bases:

                    colorFind = colorFind + 1

                    if bases[key][2] == False:

                        colorFind = colorFind - 1

                        print("\n", colors[colorFind], "wins!\n")

                        global st
                        st = True

                    if st == True:
                        break

m = 300

if preSet == False:
    # amount of moves
    m = input("How many moves?\n")
    m = int(m)

a = 30

if preSet == False:
    # amount of ants
    a = input("How many ants do you want?\n")
    a = int(a)

numBase = 5

if preSet == False:
    # amount of teams
    numBase = input("How many teams do you want?\n")
    numBase = int(numBase)

spawnPos = 360 / numBase 
baseAnt = Ant("bA", "white")

global st
st = False

# makes bases
for i in range(numBase):
    
    baseAnt.baseSpawn(i)
    allAnts[chr(i + 65)] = []

# makes ants
for i in range(numBase):

    antName = chr(i + 65)

    for j in range(a):
    
        ant = Ant(antName, colors[i])

        allAnts[antName].append(ant)

# controls ants
for i in range(m): # m is for move

    for j in range(a): # a in num of ants

        for b in bases: # b is num bases

            if j < len(allAnts[b]):
                
                allAnts[b][j].win()

                if st == True:
                    break

                allAnts[b][j].move()
                allAnts[b][j].death()
        
            if st == True:
                break
        
        if st == True:
            break
    
    if st == True:
        break

# this makes the map not dissapire after all moves are finished
Stop = input("Say stop to stop.\n")

if Stop == "stop":
    pass