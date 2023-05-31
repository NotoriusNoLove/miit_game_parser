from copy import copy
from dataclasses import dataclass


class Robot:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __copy__(self):
        return Robot(self.name + ".copy", self.weight, self.price)

    def __str__(self):
        return f"{self.name} {self.weight} {self.price}"


a = Robot("A", 10, 999)
b = copy(a)
print(a)
print(b)
