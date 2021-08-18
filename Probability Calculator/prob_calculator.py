import copy
import random

class Hat:
    def __init__(self, **balls):
        contents = []
        for x in balls.keys():
            for y in range(balls[x]):
                contents.append(x)
        self.contents = contents   
        self.copy = contents
            
    def draw(self, draws):
        self.contents = copy.deepcopy(self.copy)
        if draws > len(self.contents):
            return self.contents
        result = []
        for x in range(draws):
            ball = random.randrange(0, len(self.contents))
            result.append(self.contents[ball])
            self.contents.pop(ball)
        return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    current_hat = copy.deepcopy(hat.contents)
    success = 0

    for x in range(num_experiments):
        draws = hat.draw(num_balls_drawn)
        obj = {}

        for y in draws:
            try:
                obj[y] += 1
            except Exception:
                obj[y] = 1

        #print(obj)                      # debug

        test = 0
        
        for z in obj:
            try:
                if expected_balls[z] <= obj[z]:
                    test += 1
            except:
                test += 0
            if test == len(expected_balls):
                success += 1
            
        #print(success)                  # debug

    prob = success / num_experiments
    return prob




hat = Hat(blue=3, red=2, green=6)
expected_balls = {"blue":2,"green":1}
num_balls_drawn = 4                                 # excpected 0.272
num_experiments = 100000


x = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
print(x)







'''
hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
actual = probability
expected = 1.0
self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')
'''