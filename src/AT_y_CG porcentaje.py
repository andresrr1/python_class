'''NAME
AT_y_CG porcentaje
VERSION
1.1
AUTHOR
Andres Rivera Ramirez
DESCRIPTION
Programa para calcular el porcentaje de AT y CG de una secuencia dada por un archivo del cual se solicita su ruta
CATEGORY
USAGE
Se inserta la ruta del archivo de texto plano que contiene la secuencia a analizar.
ARGUMENTS
SEE ALSO
'''

# La ruta del archivo se lee desde el teclado
path = input(
    'Inserte la ruta del archivo que contiene la secuencia de DNA incluyendo su nombre:\n')
# Se abre el archivo para leer
try:
    file = open(path)
    # Se lee el archivo
    dna = file.read()
    file.close()
    # Se verifica que el archivo no contenga numeros, de lo contrario se notifica
    if(any(char.isdigit for char in dna)):
        raise ValueError("El archivo contiene uno o mas números")

    # Se obtiene la cantidad de nucleótidos, se asume que no hay \n u otro caracter no imprimible
    dna_lenght = len(dna)
    # Se suman las A y T
    AT_content = dna.count('A') + dna.count('T')
    # Se obtiene el porcentaje de AT
    AT_percentage = (AT_content) * 100 / (dna_lenght)

    print('Porcentaje de: \n')
    print("AT", AT_percentage, "%")
    # Se obtiene el porcentaje de GC a partir del porcentaje de AT
    print("CT", (100 - AT_percentage), "%")
# De no poder abrir o acceder al archivo se da la excepcion y se notifica cual fue el caso
except IOError as ex:
    print("No es posible abrir el archivo: \n" + ex.strerror)
