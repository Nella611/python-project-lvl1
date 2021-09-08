#!/usr/bin/env python3
import random
from brain_games.scripts.game_engine import welcome_user, game


def gcf(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return str(num1 + num2)


def questions_answers():
    result = []
    for i in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        result.append((f'{num1} {num2}', gcf(num1, num2)))
    return result


def main():
    rule = 'Find the greatest common divisor of given numbers.'
    name = welcome_user()
    game(name, rule, questions_answers())


if __name__ == '__main__':
    main()