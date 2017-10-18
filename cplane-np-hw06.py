#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import cplane_np
import sys
import cmath
import csv

from cplane_np import ArrayComplexPlane

###
# Name: Evan A Walker, Tim Frenzel
# Student ID: 01932978 ,
# Email: walke208@mail.chapman.edu , frenz102@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Homework 06
###



def julia(c,max = 100):
    def f(z):
        if (abs(z) > 2):
            return 1
        else:
            n = 1
        while (abs(z) < 2):
            n += 1
            z = z**2 + c
            if (abs(z) > 2):
                return n
            if max == n:
                return 0
        return n
    return np.vectorize(f)


class JuliaPlane(ArrayComplexPlane):
    complex_in = 0
    def __init__(self,c):
        self.complex_in = c
        ArrayComplexPlane.__init__(self,-2,2,1000,-2,2,1000)
        self.apply(julia(c))

    def refresh(self,c):
        """this function resets self.plane to private stored variables that define the plane
        and clears all functions applied by setting self.fs = [] using setPlane()
        Args:
           none
        Return:
           Null: returns nothing
        """
        self.fs = []
        self.__setPlane(self.xmin,self.xmax,self.xlen,self.ymin,self.ymax,self.ylen)
        self.apply(julia(c))
        return



    def toCSV(self,filename):
        """exports transformed plane of integers to csv files """
        print("here1")
        with open(filename, 'wb') as csvfile:
            print("here2")
            writer = csv.writer(csvfile, delimiter=',')
            print("here3")
            float_list = [self.xmin , self.xmax , self.xlen , self.ymin , self.ymax , self.ylen , self.complex_in]
            print(float_list)
            writer.writerow(float_list)
            #writer.writerow([self.plane])
        pass

    def fromCSV(self,filename):
        """imprts a csv file, and reset the plane parameters to those of the file, and refressh the plane array to the vals in the csv directly"""
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            line1 = next(reader)
            self.__setPlane(line1[0],line1[1],line1[2],line1[3],line1[4],line1[5])
            self.apply(julia(line1[6]))
        pass


x = 5
y = 2
z = complex(x,y)

myplane = JuliaPlane(z)
#myplane.printPlane()

myplane.toCSV("plane.csv")
myplane.fromCSV("plane.csv")



