#!/usr/bin/env python3

from pacman import Pacman, fruits


def game_loop():

    pacman = Pacman()

    with open('sequence.txt', 'r') as f:
        sequence = f.read().split(',')
        sequence[-1] = sequence[-1].rstrip()

    for dot in sequence:
        if dot == 'Dot':
            pacman.add_points(10)
        if dot in fruits:
            pacman.add_points(fruits[dot])
        if dot == 'InvincibleGhost':
            pacman.lose_life()
        if dot == 'VulnerableGhost':
            pacman.ghost_killed()
        if pacman.lives == 0:
            break

    return pacman


if __name__ == '__main__':
    pacman = game_loop()
    print(f'total points: {pacman.total_points}')
    print(f'lives gained {pacman.lives_gained}')

