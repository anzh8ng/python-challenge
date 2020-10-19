# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:24:47 2020

@author: Dorisu
"""
userinput = 'y'

while userinput == 'y':
    i=0
    numchain=int(input("How many numbers?"))

    while numchain >= 0:
        print(i)
        i=i+1
        numchain=numchain -1

    userinput=input("Would you like to continue? (y/n)")

