'''
### Random Walk

- A path that is determined by a series of simple decisions, 
    each of which is left entirely to chance
- In simple words, ie the path a confused ant would take 
    if it took every step in a random direction
'''

# use choice() to make random decisions
# store possible moves in a list -> decide which move to make each time a step is taken
from random import choice

class RandomWalk:
    '''A class to generate random walks'''
    
    def __init__(self, num_points=5000):
        '''Initialize attributes of a walk'''
        self.num_points = num_points

        # All walks start at point (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''Calculate all points in the walk'''

        # Keep taking steps until the walk reaches desired length
        while len(self.x_values) < self.num_points:

            # Decide which direction to go, how far to go
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            # x_step: positive value -> move to right; negative -> move to left; 0 -> move vertically
            # y_step: positive -> move up; negative -> move down; 0 -> move horizontally
            # if x_step and y_step are both 0 -> stay still -> continue the loop
            self.x_values.append(x)
            self.y_values.append(y)