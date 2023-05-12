#!/usr/bin/env python

"""
    Author: Hardik B.
    File: triangle.py
    Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape

class Triangle(Shape):
    """
    Represents a Triangle shape, and contains a base length value
    and height value and a hypotenuse length value.
    """

    def __init__(self, base, height, hypotenuse):
        self.base = base
        self.height = height
        self.hypotenuse = hypotenuse
    
    def area(self):
        """
        compute the Area using the formula base * height / 2
        """
        return self.base * self.height / 2

    def perimeter(self):
        """
        compute the perimeter using the formula base + height + hypotenuse
        """
        return self.height + self.base + self.hypotenuse
    def is_equilateral(self):
        """
        compute the is_equilateral using the formula base = height = hypotenuse
        """
        return self.base == self.height == self.hypotenuse

    def is_scalene(self):
        """
        compute the is_scalene using the formula base != height != hypotenuse
        """
        return self.base != self.height != self.hypotenuse

    def is_isosceles(self):
        """
        compute the is_isosceles using the formula base == height != hypotenuse
        """
        return self.base == self.height != self.hypotenuse






