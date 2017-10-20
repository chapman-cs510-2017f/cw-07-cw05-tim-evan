#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
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
        self.zoom(self.xmin,self.xmax,self.xlen,self.ymin,self.ymax,self.ylen)
        self.apply(julia(c))
        return
    def show(self):
        plt.figure(figsize=(10, 10), dpi=85)

        plt.axes([0.025, 0.025, 0.95, 0.95])
        plt.imshow(self.getPlane(), interpolation='nearest', cmap=plt.cm.hot, origin='lower')
        plt.colorbar(shrink=.92)      #creates color bar legend shrink=.92

        plt.xticks(())
        plt.yticks(())
        plt.show()




