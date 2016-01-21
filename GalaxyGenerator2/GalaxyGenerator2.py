import random

class Galaxy: # number of systems in galaxy
    def __init__(self,size):
        self.systems = []
        self.size = size
        for i in range(0,self.size):
            self.systems.append(StarSystem(i))

    def printfullsystem(self):
        for j in range(0,self.size):
            print('-' * 30)
            print(map.systems[j].starclass)
            print(map.systems[j].index)
            if map.systems[j].explored:
                print("Explored")
                for i in range(0,int(map.systems[j].bodies)):
                    print("A", map.systems[j].orbitals[i].orb[0],map.systems[j].orbitals[i].orb[2], map.systems[j].orbitals[i].orb[1], map.systems[j].orbitals[i].orb[3])
            else:
                print("Unexplored")       

    def exploresystem(self):
        u = input("What system index?")
        map.systems[int(u)].explored = True

class StarSystem:
    def __init__(self,planetindex):
        self.starclass = CreateStar()      # create one random star
        self.bodies = random.randint(0,12)   # create random number of bodies orbiting
        self.orbitals = []
        self.ideal = 1
        self.explored = False
        self.index = planetindex
        for x in range(0,self.bodies):
            self.orbitals.append(Orbital())

class Orbital:
    def __init__(self):
        PLANET_TYPES = ['barren',
                        'ice',
                        'lava',
                        'ocean',
                        'terran',
                        'gas',
                        'asteroid']

        PLANET_SIZES = ['tiny',
                        'small',
                        'average',
                        'large',
                        'huge']

        PLANET_TEMPS = ['frozen',
                        'cool',
                        'temperate',
                        'warm',
                        'scorching']

        self.orb = []
        self.orb.append(random.choice(PLANET_SIZES))
        self.orb.append(random.choice(PLANET_TYPES))
        self.orb.append(random.choice(PLANET_TEMPS))
        if self.orb[1] == 'asteroid':
            self.orb.append('belt')
        else:
            self.orb.append('planet')
            
       


def CreateStar():   # choose a star type based on various probablities, return star type (txt)
    starclass = random.randint(0,99)
    if starclass <= 1:
        star = "Class O"
    elif starclass <= 3:
        star = "Class B"
    elif starclass <= 8:
        star = "Class A"
    elif starclass <= 15:
        star = "Class F"
    elif starclass <= 30:
        star = "Class G"
    elif starclass <= 60:
        star = "Class K"
    elif starclass < 100:
        star = "Class M"
    
    return star

x = int(input("Number of Stars: "))
map = Galaxy(x)


running = True

while running:
    y = input("Now what? ")
    if y == 'print':
        map.printfullsystem()
    elif y == 'x':
        map.exploresystem()    
    elif y == 'q':
        running = False

