"""
title: tuple_exercises
author: eam3kzn
date: 6/11/18 3:16 PM
"""

import random


def gym_scores():
    gymnast_scores = (1, 2, 3, 4, 5)

    print("The lowest possible score is", gymnast_scores[0], "and the highest possible score is", gymnast_scores[-1])
    print("A judge can give a gymnast a score of", random.choice(gymnast_scores))


gym_scores()
