#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from abscplane import AbsComplexPlane

###
# Name: Evan A Walker, Tim Frenzel
# Student ID: 01932978 , 
# Email: walke208@mail.chapman.edu , frenz102@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 06
###

class ArrayComplexPlane(AbsComplexPlane):
    """ArrayComplexPlane that subclasses the abstract base class AbsComplexPlanes
    Args:
        xmin (float): plane's min real value
        xmax (float): plane's max real value
        xlen   (int): # pnts spanning [xmin, xmax]
        ymin (float): plane's min imag value
        ymax (float): plane's max imag value
        ylen   (int): # pnts spanning [ymin, ymax]

    Attributes:
        plane (): a meshgrid of two linspaces x, and y values. is the current state of the complex plane
        fs (list): holds all functions f that were applied to plane in a list data structure

    Functions:
        __init__(self,xmin,xmax,xlen,ymin,ymax,ylen)    :constructor, sets all args to given input, then constructs plane attribute using args
        __setPlane(self,xmin,xmax,xlen,ymin,ymax,ylen)  :private fxn that acts much like a second constructor, resets plane and args to given input. sets fs = []
        getPlane()                                      :returns plane
        printPlane(self)                                :prints plane
        refresh(self)                                   :resets plane to args values and sets fs = []. does this by calling __setPlane
        apply(self, f)                                  :applys function f to all pnts in plane
        zoom(self,xmin,xmax,xlen,ymin,ymax,ylen)        :resets plane size and reapplys all f in fs in order. does this using apply and __setPlane
    """

    def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """this function is the constructor and implements all private vars to given input,
        implements self.plane(complex plane) using the given input
        Args:
            xmin (int): minimum x value in table
            xmax (int): maximum x value in table
            xlen (int): # x points
            ymin (int): minimum y value in table
            ymax (int): maximum y value in table
            ylen (int): # y points
        Return:
            Null: returns nothing
        """
        ##  Implementing private var self.plane using numpy, this function also implements the other arguments  ##
        self.fs = []
        self.__setPlane(xmin,xmax,xlen,ymin,ymax,ylen)
        return

    def __setPlane(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """this function sets private vars to given input, and initializes fs = []
        and uses given input to create and set self.plane
        Args:
            xmin (int): minimum x value in table
            xmax (int): maximum x value in table
            xlen (int): # x points
            ymin (int): minimum y value in table
            ymax (int): maximum y value in table
            ylen (int): # y points
        Return:
            Null: returns nothing
        """
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen

        x = np.linspace(self.xmin,self.xmax,self.xlen)
        y = np.linspace(self.ymin,self.ymax,self.ylen)
        xx, yy = np.meshgrid(x, y)
        self.plane = xx + yy*1j       ##-yy1j so that the value is flipped and the top right of the plane is positive real and positive imaginary so that it conforms with convention

        self.plane = pd.DataFrame(self.plane, index=y*1j+0, columns=x)

        return

    def getPlane(self):
        """this function returns self.plane
        Args:
            none
        Return:
            self.plane (np meshgrid) : private arg self.plane that holds the complex plane
        """
        return self.plane

    def printPlane(self):
        """this function prints complex plane in a legible fashion.
        Args:
            none
        Return:
            Null: returns nothing
        """
        print("########################################-Complex Plane-######################################## \n")
        print(self.plane , "\n")
        print("############################################################################################### \n")
        return

    def refresh(self):
        """this function resets self.plane to private stored variables that define the plane
        and clears all functions applied by setting self.fs = [] using setPlane()
        Args:
           none
        Return:
           Null: returns nothing
        """
        self.fs = []
        self.__setPlane(self.xmin,self.xmax,self.xlen,self.ymin,self.ymax,self.ylen)
        return

    def apply(self, f):
        """this function adds given input f to self.fs, then
        applies f to all pnts in self.plane
        Args:
            addTofs (bool): if True, input f is appended to fs. if False, f not appended to fs
            f (fxn): complex function
        Return:
            Null: returns nothing
        """
        self.fs.append(f)
        self.plane = f(self.plane)
        return

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """this function changes the table size using given input values,
        and re-applys all f in self.fs. this is achieved by calling setPlane and
        applyAllF, see also these fxns
        Args:
            xmin (int): minimum x value in table
            xmax (int): maximum x value in table
            xlen (int): # x points
            ymin (int): minimum y value in table
            ymax (int): maximum y value in table
            ylen (int): # y points
        Return:
            Null: returns nothing
        """
        self.__setPlane(xmin,xmax,xlen,ymin,ymax,ylen)
        for k in range(len(self.fs)):
            self.apply(self.fs[k])
        return
#







"""
myPlane = ArrayComplexPlane(-1,1,3,-1,1,2)
print("myPlane = ArrayComplexPlane(-1,1,3,-1,1,2)")
myPlane.printPlane()


def f(x):
    return x*x

myPlane.apply(f)
print("myPlane.apply(f)")
myPlane.printPlane()

myPlane.refresh()
print("myPlane.refresh()")
myPlane.printPlane()

myPlane.zoom(1,2,2,1,2,2)
print("myPlane.zoom(1,2,2,1,2,2)")
myPlane.printPlane()


myPlane.getPlane()
"""
##
    # NOTE: WE DO NOT NEED A MAIN BECAUSE WE ARE NOT ACCESSING FILE THROUGH COMMAND TERMINAL.
    #       SINCE WE ARE ONLY USING THE CODE IN THE JUPYTER NOTEBOOK
##








