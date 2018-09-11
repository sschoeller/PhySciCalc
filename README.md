# PhySciCalc [![GitHub top language](https://img.shields.io/github/languages/top/sschoellerSTEM/PhySciCalc.svg)](https://github.com/sschoellerSTEM/PhySciCalc)  [![GitHub contributors](https://img.shields.io/github/contributors/sschoellerSTEM/PhySciCalc.svg)](https://github.com/sschoellerSTEM/PhySciCalc)



> An expanded Scientific Calculator CLI for Physical Science

## Requirements:

- [Python 3](https://www.python.org) or later
- [f2py](http://www.f2py.com/) wrapper: a command line tool for binding Python and Fortran code

### Set up development environment

> From root directory install dependencies

```
pip install -r requirements.txt
```

> `f2py` wrapper usage

```
f2py -c ext_mod.f90 -m ext
```

## Try it

> ⚠️  Must have Python3 installed on your `PATH`

```
python physcicalc.py
```

## Available operations

- add: Addition
- sub: Subtraction
- mul: Multiplication
- div: Division
- sqrt: Square root
- sin: Sine
- cos: Cosine
- tan: Tangent
- sec: Secant
- csc: Cosecant
- cot: Cotangent
- sinh: Hyperbolic sine of a number
- cosh: Hyperbolic cosine of a number
- tanh: Hyperbolic tangent of a number

# License

[GPL-3.0](https://github.com/sschoellerSTEM/PhySciCalc/blob/master/LICENSE) © [Scott Schoeller](https://github.com/sschoellerSTEM)
