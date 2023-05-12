"""
Author: Hardik B.
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle

class TriangleTest(TestCase):
    """
    Defines a test case for a triangle class
    """
    
    def setUp(self):
        """create a few test objects
        """
        self.triangle1 = Triangle(2,3,4)
        self.triangle2 = Triangle(7,8,9)
        self.triangle3 = Triangle(10,11,12)
        self.equiTriangle = Triangle(4,4,4)
    
    def test_area(self):
        """compare the test triangle area computations to the actual values
        """
        
        self.assertEqual(self.triangle1.area(), 3)   
        self.assertEqual(self.triangle2.area(),28)
        self.assertEqual(self.triangle3.area(),55)
    
    def test_perimeter(self):
        """compare the test triangle perimeter computations to the actual values
        """
        
        self.assertEqual(self.triangle1.perimeter(), 9)
        self.assertEqual(self.triangle2.perimeter(), 24)
        self.assertEqual(self.triangle3.perimeter(), 33)
            
    def test_equilateral(self):
        """confirm or deny if the triangle is equilateral
        """
        self.assertEqual(self.triangle1.is_equilateral(), False)
        self.assertEqual(self.triangle2.is_equilateral(), False)
        self.assertEqual(self.triangle3.is_equilateral(), False)
        self.assertEqual(self.equiTriangle.is_equilateral(), True)
        
          