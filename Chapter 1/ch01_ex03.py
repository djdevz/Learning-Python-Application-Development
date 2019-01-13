from __future__ import print_function
from AttackOfTheOrcs import AttackOfTheOrcs

"""ch01_ex03

A text-based game to acquire a hut by defeating the enemy (OOP).

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

This is a supporting example code for example 3 of Chapter 1. It is a
command line program that illustrates use of OOP concepts. The player
inputs a hut number. If the occupant is an enemy, the player is given an
option to 'attack'. Player wins if he defeats the enemy.
 Additionally,the player can 'run away' from the combat, get healed
in friendly hut and then resume the fight.

In the aforementioned book this is also referred to as
"Attack of the Orcs v1.0.0". More details can be found in the relevant
chapter of the book..

RUNNING THE PROGRAM:
--------------------
- Python 3.5.x must be installed on your system.
- It is assumed that you have Python 3.5 available in your environment
  variable PATH. It will be typically available as 'python' or 'python3'.
- Here is the command to execute this code from command prompt

        $ python ch01_ex03.py     ( OR $ python3 ch01_ex03.py)

- See the README file for more information. Or visit python.org for OS
  specific instructions on executing Python from a command prompt.

.. todo::

1. The code comments and function descriptions in this file are
   intentionally kept to a minimum! See a later chapter of the book to
   learn about the code documentation and best practices!
   Feel free to add documentation after reading that chapter.
   Description of the code can be found in the book.
2. Split the code into smaller modules
3. Make GameUnit to an abstract base class
4. See the other TODO comments..things you can try fixing as an exercise!

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

import random
import sys

if sys.version_info < (3, 0):
    print("This code requires Python 3.x and is tested with version 3.5.x ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0],
                                      sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)


if __name__ == '__main__':
    game = AttackOfTheOrcs()
    game.play()

