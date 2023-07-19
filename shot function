from enum import Enum
import random

class Lie(Enum):
    green = 1
    fairway = 2
    rough = 3
    hazard = 4
    heavy_stuff = 5

    def __str__(self):
        value = self.value
        match value:
            case 1:
                return 'green'
            case 2:
                return 'fairway'
            case 3:
                return 'rough'
            case 4:
                return 'hazard'
            case 5:
                return 'heavy stuff'
            
class Shot:
    def __init__(self, club, shot_type, distance, lie, strokes):
        self.club = club
        self.distance = distance
        self.lie = lie
        self.strokes = strokes
        self.type = shot_type

    def __repr__(self):
        return f'{self.club} {self.type}: {self.distance} yards, landed in the {self.lie}'
    
class ShotTracker:
    def __init__(self):
        self.shots = {}
        self.shot_counter = 1

    def get_input(self, prompt, options):
        while True:
            try:
                result = int(input(prompt))
                if result in options:
                    return result
                print('\n***Please enter a valid number***')
            except ValueError:
                print('\n***Please enter a valid number***')
    
    def wtbchirp(self):
        chirps = ['Let your wife hit the next one buddy']
        print(random.choice(chirps))

    def hazchirp(self):
        chirps = ['You could wrap that in bacon and the dogs wouldn\'t find it', 'I think it opens up over there']
        print(random.choice(chirps))

    def get_shot_info(self, lie):
        if lie == Lie.hazard:
            chirp = random.randrange(1,11)
            if chirp == 1:
                self.hazchirp()
        club = input('Which club did you hit? ')
        shot_type = self.get_input('\nWhat type of shot did you hit? Enter...\n'
                                   '''\n1 for full swing
                                   \n2 for punch shot
                                    \n3 for chip
                                    \n4 for putt\n''', range(1,5))
        distance = input(f'How far did your {club} go? ')
        match shot_type:
            case 1:
                shot_type = 'full swing'
            case 2:
                shot_type = 'punch shot'
            case 3:
                shot_type = 'chip'
            case 4:
                shot_type = 'putt'
        
        match lie:
            case Lie.green:
                shot = Shot(club, shot_type, distance, lie, 1)
            case Lie.fairway:
                shot = Shot(club, shot_type, distance, lie, 1)
            case Lie.rough:
                shot = Shot(club, shot_type, distance, lie, 1)
            case Lie.hazard:
                shot = Shot(club, shot_type, distance, lie, 2)
            case Lie.heavy_stuff:
                shot = Shot(club, shot_type, distance, lie, 1)

        if (int(distance) < 100 and shot_type == 'full swing' and lie != Lie.green):
            chirp = random.randrange(1,11)
            if chirp == 1:
                self.wtbchirp()
        
        return shot
    
    def shot_func(self):
        while True:
            result = self.get_input('\nHitting shot...\n'
            '''\nFor shot result enter...\n \n1 for green
            \n2 for fairway
            \n3 for rough
            \n4 for hazard
            \n5 for heavy stuff
            \n6 to remove last shot\n''', range(1,7))

            if result == 6:
                if self.shot_counter > 1:
                    removed_shot = self.shots.popitem()
                    self.shot_counter -=1
                    print(f'Removing previous shot: {removed_shot}')
                else:
                    print('You do not currently have any shots.')
            else:
                match result:
                    case 1:
                        print('You hit the green')
                        self.shots['Shot #'+str(self.shot_counter)] = self.get_shot_info(Lie.green)
                        self.shot_counter += 1
                        return
                    case 2:
                        print('You hit the fairway')
                        self.shots['Shot #'+str(self.shot_counter)] = self.get_shot_info(Lie.fairway)
                        self.shot_counter += 1
                    case 3:
                        print('You hit the rough')
                        self.shots['Shot #'+str(self.shot_counter)] = self.get_shot_info(Lie.rough)
                        self.shot_counter += 1
                    case 4:
                        print('You hit the hazard')
                        self.shots['Shot #'+str(self.shot_counter)] = self.get_shot_info(Lie.hazard)
                        self.shot_counter += 1
                    case 5:
                        print('You hit the heavy stuff')
                        self.shots['Shot #'+str(self.shot_counter)] = self.get_shot_info(Lie.heavy_stuff)
                        self.shot_counter += 1


    def putt_func(self):
        try:
            putts = int(input('How many putts did you have? '))
            self.shots['Shot #'+str(self.shot_counter)] = Shot('putter', 'putt', 0, Lie.green, putts)
        except ValueError: 
                print('\n***Please enter a valid number***')
                return self.putt_func()

    def play_hole(self):
        self.shot_func()  
        self.putt_func()
        shots = self.shots.values()
        strokes = sum([shot.strokes for shot in shots])

        return print(f'Your score was: {strokes} and your hole looked like: {self.shots}')

# test = ShotTracker()
# test.play_hole()
