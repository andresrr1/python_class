'''NAME
cuenta de nucleotidos
VERSION
1.1
AUTHOR
Andres Rivera Ramirez

DESCRIPTION
Se cuenta la repetición de cada nucleotido en una secuencia dada por el usuario a traves del teclado
CATEGORY

USAGE
Se lee la secuencia desde el teclado, esta es introducida por el usario
ARGUMENTS

SEE ALSO


'''
#La secuencia de DNA se lee desde el teclado
dna = input('Inserte secuencia de DNA:')
#Se utilizan las llaves para hacer varias count en una sola línea de código.
print(f"El número de nucleotidos es \n \
A:{dna.count('A')} \n C:{dna.count('C')} \n \
T:{dna.count('T')} \n G:{dna.count('G')}")
