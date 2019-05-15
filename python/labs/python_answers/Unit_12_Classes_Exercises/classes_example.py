"""
title: classes_example
author: eam3kzn
date: 8/10/18 8:43 AM
"""


class Player:
    """
    Creates a game Player template.
    """
    def gain_point(self, points):
        """Prints that the user has gained a certain number of points."""
        self.points += points
        print(f"Yay! You have gained {points} point(s)! That means you now have {self.points} points!")

    def lose_point(self, points):
        """Prints that the user has lost a certain number of points."""
        self.points -= points
        print(f"Oh no! You have lost {points} point(s)! That means you now have {self.points} points!")


def main():
    ralph = Player()
    ralph.gain_point(10)
    ralph.lose_point(5)


if __name__ == "__main__":
    main()

print(Player.__doc__) # Prints out docstring within the Class
