from lea import *
import random, os


# x = int(input("Number of Systems: "))

x = 10
galaxy = []

starset = Lea.fromValFreqs(("Class O", 0.0001),("Class B", 0.125),("Class A", 0.625),("Class F", 3),("Class G", 7.5),("Class K", 12),("Class M", 76))

galaxy =(starset.random(x))



'''
classm = 0
classk = 0
classg = 0
classf = 0
classa = 0
classb = 0
classo = 0


for i in range(x):
    if galaxy[i] == "Class M":
        classm += 1
    elif galaxy[i] == "Class K":
        classk += 1
    elif galaxy[i] == "Class G":
        classg += 1
    elif galaxy[i] == "Class F":
        classf += 1
    elif galaxy[i] == "Class A":
        classa += 1
    elif galaxy[i] == "Class B":
        classb += 1
    elif galaxy[i] == "Class O":
        classo += 1
     

print("Class M:", classm)
print("Class K:", classk)
print("Class G:", classg)
print("Class F:", classf)
print("Class A:", classa)
print("Class B:", classb)
print("Class O:", classo)

'''

def creategrid(h,w):
    mapgrid = [[0 for x in range(h)] for x in range(w)]
    for i in range(h):
        for j in range(w):
            mapgrid[j][i] = random.randint(0,3)

    return mapgrid



def drawmap(t,l,h,w,mg):  # top, left, height, width
    os.system('cls')
    
    print(" "*20 + "#" + "#"*w + "#")  #top line
    for i in range(t,t+h):
        print(" "*20 + "#", end="")
        for j in range(l,l+w):
            print(mg[i][j], end="")
        print("#")

    print(" "*20 + "#" + "#"*w + "#")  #bottom line


grid = creategrid(100,100)
running = True
a = 0
b = 0
height = 20
width = 40

while running:
    drawmap(a,b,height,width,grid)
    print(a,b)
    key = input(" >> ")
    if key == 'q':
        running = False
    elif key == 'a':
        b -= 1
    elif key == 'd':
        b += 1
    elif key == 's':
        a += 1
    elif key == 'w':
        a -= 1

    