'''
NAME
    noadapters.py
VERSION
    1.1
AUTHOR
    Andres Rivera Ramirez
DESCRIPTION
    Remover las secuencias adaptadoras
CATEGORY
USAGE
    python noadapters.py
ARGUMENTS
SEE ALSO
'''

# Abrir el archivo
try:
    input_adapters = (".\data\input_adapters.txt")
    input_adapters_content = open(input_adapters)

    # Leer el archivo por líneas
    secuencias = input_adapters_content.readlines()
    input_adapters_content.close()

    # Crear el archivo que contendrá el resultado
    output_noadapters = open(".\myresults\output_noadapters.txt", "w")

    # Quitar el adaptador de cada línea y escribir en el archivo
    for secuencia in secuencias:
        output_noadapters.write(secuencia[14:])

    output_noadapters.close()

except IOError as ex:
    print("No se pudo abrir el archivo: \n" + ex.strerror)
