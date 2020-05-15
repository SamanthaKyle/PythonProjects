""""
Defining rules of magic and spells in RPG.
Author: Samantha Kyle
Date: May 14th, 2020

Project made alongside the course, "The Complete Python 3 Course:
Beginner to Advanced!" by Nick Germaine and Joseph Delgadillo on Udemy.
"""
import random


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_dmg(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)


