"""
title: list_exercise
author: eam3kzn
date: 6/11/18 3:12 PM
"""

import random


def shake_eight_ball():
    input("Ask a question: ")
    all_responses = ["Yes, definitely!", "As I see it, yes.", "Ask again later.", "Cannot predict now",
                     "Don't count on it.", "Very doubtful"]
    random_response = random.choice(all_responses)
    return random_response


print(shake_eight_ball())
