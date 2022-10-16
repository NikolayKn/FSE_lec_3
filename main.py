#!/usr/bin/env python3
from sys import argv
from useful_package.module_a import polynom_3
from useful_package.module_b import hyperbola

def main():
    x = float(argv[1])
    print(f'x = {x}, x**3 = {polynom_3(x)}, hyperbola(x) = {hyperbola(x)}')

if __name__ == '__main__':
    main()


