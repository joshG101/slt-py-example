#!/usr/bin/env python

"""
Author: Nick Russo
File: shape_pytest.py
Purpose: Simple pytest demonstration for the defined
shape classes.
"""

from shapes.rectangle import Rectangle
from shapes.circle import Circle
from shapes.triangle import Triangle


def test_rectangle():
    """
    Defines tests on some specific rectangle objects.
    """
    len7wid3 = Rectangle(7, 3)
    len1wid6 = Rectangle(1, 6)
    len5wid5 = Rectangle(5, 5)

    # Test areas, perimeters, and whether they are squares
    assert len7wid3.area() == 21
    assert len1wid6.area() == 6
    assert len5wid5.area() == 25
    assert len7wid3.perimeter() == 20
    assert len1wid6.perimeter() == 14
    assert len5wid5.perimeter() == 20
    assert not len7wid3.is_square()
    assert not len1wid6.is_square()
    assert len5wid5.is_square()


def test_circle():
    """
    Defines tests on some specific circle objects.
    """
    radius5 = Circle(5)
    radius8 = Circle(8)

    # Test areas, perimeters, and diameters
    assert radius5.area() == 78.54
    assert radius8.area() == 201.06
    assert radius5.perimeter() == 31.42
    assert radius8.perimeter() == 50.27
    assert radius5.diameter() == 10
    assert radius8.diameter() == 16

def test_triangle():
    """
    Defines tests on some specific triangle objects.
    """
    
    triangle1 = Triangle(3, 4, 5)
    triangle2 = Triangle(5, 5, 5)
    triangle3 = Triangle(10, 10, 15)
    
    
    # Test areas, perimeters, and whether they are equilateral, isosceles, or scalene
    
    assert triangle1.area() == 6
    assert triangle2.area() == 12.5
    assert triangle3.area() == 50
    
    assert triangle1.perimeter() == 12
    assert triangle2.perimeter() == 15
    assert triangle3.perimeter() == 35
    
    assert triangle1.is_equilateral() == False
    assert triangle2.is_equilateral() == True
    assert triangle3.is_equilateral() == False
    
    assert triangle1.is_scalene() == True
    assert triangle2.is_scalene() == False
    assert triangle3.is_scalene() == False
    
    
    
    