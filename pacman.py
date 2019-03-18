
class Pacman:

    def __init__(self):
        self.total_points = 5000
        self.points = 5000
        self.lives = 3
        self.ghost_multiplier = 200
        self.lives_gained = 0

    def add_points(self, points):
        self.points += points
        self.total_points += points
        if self.points >= 10000:
            self.gain_life()
            self.points -= 10000

    def gain_life(self):
        self.lives += 1
        self.lives_gained += 1

    def lose_life(self):
        self.lives -= 1

    def ghost_killed(self):
        self.ghost_multiplier *= 2
        self.points += self.ghost_multiplier
        self.total_points += self.ghost_multiplier


fruits = {
        'Cherry': 100,
        'Strawberry': 300,
        'Orange': 500,
        'Apple': 700,
        'Melon': 1000,
        'Galaxian': 2000,
        'Bell': 3000,
        'Key': 5000
    }

