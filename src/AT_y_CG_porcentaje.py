'''NAME
AT_y_CG porcentaje
VERSION
1.2
AUTHOR
Andres Rivera Ramirez
DESCRIPTION
Programa para calcular el porcentaje de AT y CG de una secuencia dada por un archivo del cual se solicita su ruta como argumento a traves de la linea de comandos
CATEGORY
USAGE
Se inserta la ruta del archivo de texto plano que contiene la secuencia a analizar como el argumento -i y el archivo de salida en el que se escribira el resultado como
el argumento -o
ARGUMENTS
SEE ALSO
'''

import argparse
from email import parser

# Estos son los argumentos que requiere el programa, son paths a archivos de texto
parser = argparse.ArgumentParser(
    description=" Este programa calcula el porcentaje de AT y CG  en una secuencia utilizando argumentos de linea de comandos")

parser.add_argument("-i", "--input",
                    metavar="El path del archivo de entrada",
                    help="Archivo de secuencias de DNA",
                    required=True)

parser.add_argument("-o", "--output",
                    help="El path del archivo  de salida",
                    required=False)


args = parser.parse_args()


# Se abre el archivo para leer
try:
    file = open(args.input)
    # Se lee el archivo
    dna = file.read()
    file.close()
    # Se verifica que el archivo no contenga numeros, de lo contrario se notifica
    if(any(char.isdigit() for char in dna)):
        raise ValueError("El archivo contiene uno o mas números")

    # Se obtiene la cantidad de nucleótidos, se asume que no hay \n u otro caracter no imprimible
    dna_lenght = len(dna)
    # Se suman las A y T
    AT_content = dna.count('A') + dna.count('T')
    # Se obtiene el porcentaje de AT
    AT_percentage = (AT_content) * 100 / (dna_lenght)
    CG_percentage = 100 - AT_percentage

    print('Porcentaje de: \n')
    print("AT", AT_percentage, "%")
    # Se obtiene el porcentaje de GC a partir del porcentaje de AT
    print("CG", CG_percentage, "%")
# De no poder abrir o acceder al archivo se da la excepcion y se notifica cual fue el caso
except IOError as ex:
    print("No es posible abrir el archivo: \n" + ex.strerror)

# Se crea el archivo de salida y se guardan los porcentajes en el
if(args.output):
    try:
        archivo_porcentaje = open(args.output, "w")
        archivo_porcentaje.write("AT:\n")
        archivo_porcentaje.write(str(AT_percentage))
        archivo_porcentaje.write("\nCG:\n")
        archivo_porcentaje.write(str(CG_percentage))
    except IOError as ex:
        print("No es posible crear el archivo de salida", ex.strerror)
