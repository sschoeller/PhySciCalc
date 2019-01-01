#***********************************************************************
# calcModes.py
# Copyright (C) 2018 - 2019 Scott Schoeller (sschoellerSTEM)
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

class calcModes:
    # answer will store the current answer
    answer = 0.0

    def arith(self, mode):
        '''arith(self, mode) computes the arithmetic operations
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
            answer = numio
            return answer

        elif mode == 'sub':
            while done == '':
                try:
                    tmp = float(input('Type a non-zero number to subtract or simply enter 0 to compute and exit: '))
                    if tmp != 0.0: # subtracting anything by 0 does not affect the final result
                        num.append(tmp)
                    else:
                        break
                except ValueError:
                    continue # handles input that can't be converted

            for number in num:
                numio = number - numio
            answer = - numio
            return answer

        elif mode == 'mult':
            while done == '':
                try:
                    tmp = float(input('Type a non-zero number to multiply or simply enter 0 to compute and exit: '))
                    if tmp != 0.0: # multiplying anything by 0 is from 0
                        num.append(tmp)
                    else:
                        break
                except ValueError:
                    continue # handles input that can't be converted

            for number in num:
                numio = numio * number
            answer = numio
            return answer

        elif mode == 'div':
                    num = float(input('Enter any number: '))
                    divnum = float(input('Enter a non-zero number to divide by or simply enter 0 to cancel: '))
                    if divnum != 0.0: # can't divide by 0
                        return num/divnum
                    else:
                        return 0.0
        elif mode == 'sqrt': # make sure to handle complex numbers
            try:
                numio = complex(input('Enter any number: '))
            except ValueError:
                return 'Error: invalid input!'
            # else, return the sqrt
            answer = numpy.sqrt(numio)
            return answer

    def trig(self, mode):
        '''trig(self, mode) handles sin, cos, tan, cot, sec, csc'''
        numio = 0.0
        if mode == 'sin':
            try:
                numio = float(input('Enter an angle in radians: '))
            except ValueError:
                return 'ERROR: invalid input!'
            # if ValueError *NOT* encountered
            answer = numpy.sin(numio)
            return answer

        elif mode == 'cos':
            try:
                numio = float(input('Enter an angle in radians: '))
            except ValueError:
                return 'ERROR: invalid input!'
            # if ValueError *NOT* encountered
            answer = (numpy.cos(numio))
            return answer

        elif mode == 'tan':
            try:
                numio = float(input('Enter an angle in radians: '))
            except ValueError:
                return 'ERROR: invalid input!'
            # if ValueError *NOT* encountered
            answer = numpy.tan(numio)
            return answer

        elif mode == 'cot':
            try:
                numio = float(input('Enter an angle in radians: '))
            except ValueError:
                return 'ERROR: invalid input!'
            # if ValueError *NOT* encountered
            if numio != 0.0:
                answer = 1/(numpy.tan(numio)) 
                return answer
            else:
                return 'ERROR: can not divide by 0'

        elif mode == 'sec':
            try:
                numio = float(input('Enter an angle in radians: '))
            except ValueError:
                return 'ERROR: invalid input!'
            # if ValueError *NOT* encountered
            if numio != 0.0:
                answer = 1/(numpy.cos(numio))
                return answer
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
    def gmol(self):
            try:
                grams = float(input('Enter grams of material: '))
                MW = float(input('Enter MW of material: '))
                answer = ext_mod.gmol(grams, MW)
                return answer
            except ValueError:
                return 'ERROR: invalid input!'

    def re(self):
        try:
            kilograms = float(input('Enter mass of object (in kg): '))
            answer = ext_mod.re(kilograms)
            return answer
        except ValueError:
            return 'ERROR: invalid input!'
