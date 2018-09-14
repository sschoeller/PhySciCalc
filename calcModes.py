#***********************************************************************
# calcModes.py
# Copyright (C) 2018 Scott Schoeller (sschoellerSTEM)
#
# This file is part of PhySciCalc
# PhySciCalc is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# PhySciCalc is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with PhySciCalc.  If not, see <https://www.gnu.org/licenses/>.
#***********************************************************************
import numpy
from ext import *

def arith(mode):
    '''arith(mode) computes the arithmetic operations
    addition (mode= add), substraction (mode= sub),
    multiplication (mode= mult), division (mode= div),
    square root (mode= sqrt)'''
    done = '' # dummy variable
    num = []
    numio = 0.0
    if mode == 'add':
        while done == '':
            try:
                numio = float(input('Type a non-zero number to add or simply enter 0 to compute and exit: '))
                if numio != 0.0: # adding anything to 0 does not affect the final result
                    num.append(numio)
                else:
                    break
            except ValueError:
                continue # handles input that can't be converted

        for number in num:
                numio = numio + number
        return numio

    elif mode == 'sub':
        while done == '':
            try:
                numio = float(input('Type a non-zero number to subtract or simply enter 0 to compute and exit: '))
                if numio != 0.0: # subtracting anything by 0 does not affect the final result
                    num.append(numio)
                else:
                    break
            except ValueError:
                continue # handles input that can't be converted

        for number in num:
                numio = number - numio
        return numio

    elif mode == 'mult':
        while done == '':
            try:
                numio = float(input('Type a non-zero number to multiply or simply enter 0 to compute and exit: '))
                if numio != 0.0: # multiplying anything by 0 is from 0
                    num.append(numio)
                else:
                    break
            except ValueError:
                continue # handles input that can't be converted

        for number in num:
                numio = numio * number
        return numio

def trig(mode):
    '''trig(mode) handles sin, cos, tan, cot, sec, csc'''
    numio = 0.0
    if mode == 'sin':
        try:
            numio = float(input('Enter an angle in radians: '))
        except ValueError:
            return 'ERROR: invalid input!'
        # if ValueError *NOT* encountered
        return numpy.sin(numio)

    elif mode == 'cos':
        try:
            numio = float(input('Enter an angle in radians: '))
        except ValueError:
            return 'ERROR: invalid input!'
            # if ValueError *NOT* encountered
        return (numpy.cos(numio))

    elif mode == 'tan':
        try:
            numio = float(input('Enter an angle in radians: '))
        except ValueError:
            return 'ERROR: invalid input!'
        # if ValueError *NOT* encountered
        return numpy.tan(numio)

    elif mode == 'cot':
        try:
            numio = float(input('Enter an angle in radians: '))
        except ValueError:
            return 'ERROR: invalid input!'
        # if ValueError *NOT* encountered
        if numio != 0.0:
            return 1/(numpy.tan(numio))
        else:
            return 'ERROR: can not divide by 0'

    elif mode == 'sec':
        try:
            numio = float(input('Enter an angle in radians: '))
        except ValueError:
            return 'ERROR: invalid input!'
        # if ValueError *NOT* encountered
        if numio != 0.0:
            return 1/(numpy.cos(numio))
        else:
            return 'ERROR: can not divide by 0'

    elif mode == 'csc':
        try:
            numio = float(input('Enter an angle in radians: '))
        except ValueError:
            return 'ERROR: invalid input!'
        # if ValueError *NOT* encountered
        if numio != 0.0:
            return 1/(numpy.sin(numio))
        else:
            return 'ERROR: can not divide by 0'

# Scientific modes below this point
def gmol():
        try:
            grams = float(input('Enter grams of material: '))
            MW = float(input('Enter MW of material: '))
            numio = ext_mod.gmol(grams, MW)
            return numio
        except ValueError:
            return 'ERROR: invalid input!'

def re():
    try:
        kilograms = float(input('Enter mass of object (in kg): '))
        numio = ext_mod.re(kilograms)
        return numio
    except ValueError:
        return 'ERROR: invalid input!'
