#club attributes, name, average yards. clubs are instantiated by user. make bag a hashmap.

class Club:
    def __init__(self, name):
        self.name = name
        self.yards = None
        self.loft = None
        club_range = []
    
    def get_yards(self):
        try:
            self.yards = int(input('Please enter your average yardage with {0}: '.format(self.name)))
        except ValueError:
            print('Please enter a valid number')
        return self.yards
    
    def get_loft(self):
        try:
            self.loft = int(input('Please enter the loft of your {0}: '.format(self.name)))
        except ValueError:
            print('Please enter a valid number')
        return self.loft
    
    def get_range(self):
        min = round(self.yards * 0.9)
        max = round(self.yards * 1.06)
        club_range = [i for i in range(min, max, 1)]
        return club_range

        
driver = Club('Driver')
for x in range(3, 8, 2):
    wood = Club(f'{x}-Wood'.format(x))

hybrid3 = Club('3-Hybrid')
hybrid4 = Club('4-Hybrid')
for x in range(1, 10):
    iron = Club(f'{x}-iron'.format(x))
pwedge = Club('Pitching Wedge')
gwedge = Club('Gap Wedge')
for x in range(50, 64, 2):
    wedge = Club(f'{x}-degree Wedge'.format(x))
    wedge.loft = x


