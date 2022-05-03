'''NAME
cuenta de nucleotidos
VERSION
1.2
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
# La secuencia de DNA se lee desde el teclado
dna = input('Inserte secuencia de DNA:')
# Se verifica que la secuencia de DNA solo contenga letras mayusculas
if(not dna.isupper()):
    raise ValueError("La secuencia contiene letras minúsculas")
# Se verifica que no existan numeros en la secuencia de DNA
if(any(char.isdigit() for char in dna)):
    raise ValueError("La secuencia contiene uno o mas números")
# Se verifica que no existan caracteres que no correspondan a nucleotidos en la secuencia
if(any(char != 'A' or 'C' or 'G' or 'T' for char in dna)):
    raise ValueError("Se introdujo un caracter inadecuado en la secuencia")
# Se utilizan las llaves para hacer varias count en una sola línea de código.
print(f"El número de nucleotidos es \n \
A:{dna.count('A')} \n C:{dna.count('C')} \n \
T:{dna.count('T')} \n G:{dna.count('G')}")
