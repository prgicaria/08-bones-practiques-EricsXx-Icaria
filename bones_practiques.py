#!/usr/bin/env python3
'''Bones practiques. divisió entre nombres enters
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Aquest programa et demana dos nombres enters,
després automàticament et fa la divisió
i et surt el residu i el quocient
'''

__author__ = "Eric Navarro"
__email__ = "enavarros@instituticaria.cat"
__date__ = "2024/10/17"


Divident = int(input("Introdueix el Divident:"))
Divisor = int(input("Introdueix el Divisor:"))
Quocient = Divident // Divisor
Residu = Divident % Divisor
print(f"Divisió: {Divident}/{Divisor}")
print(f"Quocient: {Quocient}")
print(f"Residu: {Residu}")
