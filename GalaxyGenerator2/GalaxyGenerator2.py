import random

class Galaxy(self, size): # number of systems in galaxy
    def __init__(self):
        self.size = size
        pass

class StarSystem(self):
    def __init__(self):
        self.starclass = CreateStar()      # create one random star
        
        pass


def CreateOrbitals():  
     
    # planet type, size, temperature, biomass, atmosphere
    
    PLANET_TYPES = ['Barren',
                    'Ice',
                    'Lava',
                    'Ocean',
                    'Terran',
                    'Gas',
                    'Asteroid Belt']

    PLANET_SIZES = ['Tiny',
                    'Small',
                    'Average',
                    'Large',
                    'Huge']

    PLANET_TEMPS = ['Frozen',
                    'Cool',
                    'Temperate',
                    'Warm',
                    'Scorching']

    




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

