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

    success = 0

    for x in range(num_experiments):
        draws = hat.draw(num_balls_drawn)
        obj = {}
        for y in draws:
            try:
                obj[y] += 1
            except Exception:
                obj[y] = 1

        test = 0

        for z in obj:
            try:
                if expected_balls[z] <= obj[z]:
                    test += 1
            except Exception:
                test += 0
            if test == len(expected_balls):
                success += 1
                break

    prob = success / num_experiments
    return prob
