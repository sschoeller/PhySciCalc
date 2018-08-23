#!/usr/bin/env python3
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
import calcModes

def main():
    # prompt for mode or mode listing
    mode = ''
    while mode != 'e':
        mode = input('Enter an input mode.  Type the word modes for list of modes. type the letter e to exit. ')
        if mode == 'modes':
            print('\nThe following modes are available\n')
            print('\tadd, sub, mul, div, sqrt')
            print('\tsin, cos, tan, sec, csc, cot')
            print('\tsinh, cosh, tanh')
            #print('\tgmol (g/mol conversion)')
            #print('\tre (relatevistic rest energy)')
        
        elif (mode == 'add' or mode == 'sub' or mode == 'mult' or mode == 'div' or mode == 'sqrt'):
            print(calcModes.arith(mode))
        
        elif (mode == 'sin' or mode == 'cos' or mode == 'tan' or mode == 'cot' or mode == 'sec' or mode == 'csc'):
            print(calcModes.trig(mode))

main()