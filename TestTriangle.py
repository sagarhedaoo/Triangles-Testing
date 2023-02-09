# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import xmlrunner
import io

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(400,400,400),'InvalidInput','400,400,400 is not a valid input')

    def testCharInput(self):
        self.assertEqual(classifyTriangle('a','b','c'),'InvalidInput','a,b,d is not a Valid Input')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(23,24,7),'Scalene','23,24,7 is a Scalene Triangle')

    def testNegativeInput(self):
        self.assertEqual(classifyTriangle(-4, -6, 0), 'InvalidInput', '-4,-6,0 is not a Valid Input')

    def testZeroInput(self):
        self.assertEqual(classifyTriangle(0 ,0 ,0),'InvalidInput','0,0,0 is not a Valid Input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

