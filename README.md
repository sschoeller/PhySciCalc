# PhySciCalc
An expanded scientific calculator for physical science

Requires: Python 3.x, numpy and standalone f2py wrapper

## f2py wrapper usage for Fortran extension module
sschoellerSTEM tested the wrapper and integrated ext_mod.f90 as follows: 

1. f2py -c ext_mod.f90 -m ext

2. Then import into Python 3.x: from ext import *

3. A given function, fn(args) in the following example, can then be accessed from Python 3.x: ext_mod.fn(args) 
