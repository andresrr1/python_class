'''NAME
AT_y_CG porcentaje
VERSION
1.4
AUTHOR
Andres Rivera Ramirez
DESCRIPTION
Programa para calcular el porcentaje de AT y CG de una secuencia
dada por un archivo del cual se solicita su ruta como argumento 
a traves de la linea de comandos, ademas busca codones de paro e inicio e imprimime
las posiciones en que se encuentran.
CATEGORY
USAGE
    python src/AT_y_CG_porcentaje.py [-h] -i El path del archivo de entrada
                             [-o OUTPUT]
ARGUMENTS
  -h, --help            show this help message and exit
  -i El path del archivo de entrada, --input El path del archivo de entrada
                        Archivo de secuencias de DNA
  -o OUTPUT, --output OUTPUT
                        El path del archivo de salida
SEE ALSO
'''

import argparse
import re

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


def encontrar_start_stop(dna):
    if(re.search("ATG", dna)):
        match = re.search("ATG", dna)
        print("La secuencia contiene un codon de inicio")
        print(match.span())
    if(re.search("TAC", dna)):
        match = re.search("TAC", dna)
        print("La secuencia contiene un codon de inicio")
        print(match.span())
    if(re.search("UA(A|G)", dna)):
        print("La secuencia contiene un codon de paro")
        match = re.search("UA(A|G)", dna)
        print(match.span())
    if(re.search("UGA", dna)):
        print("La secuencia contiene un codon de paro")
        match = re.search("UGA", dna)
        print(match.span())
    return(1)


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
        archivo_porcentaje.close()
    except IOError as ex:
        print("No es posible crear el archivo de salida", ex.strerror)

m = encontrar_start_stop(dna)
