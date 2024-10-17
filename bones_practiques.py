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


def divisio_entera():
    """Funció que realitza una divisió entera
    i mostra el resultat a la pantalla."""
    try:
        dividend = int(input("Introdueix el dividend: "))
        divisor = int(input("Introdueix el divisor: "))
        if divisor == 0:
            print("Error: No es pot dividir per zero.")
            return
        quocient = dividend // divisor
        residu = dividend % divisor
        print(f"Divisió: {dividend}/{divisor}")
        print(f"Quocient: {quocient}")
        print(f"Residu: {residu}")

    except ValueError:
        print("Error: Si us plau, introdueix nombres enters vàlids.")


if __name__ == "__main__":
    divisio_entera()
