'''NAME
    trimming
    VERSION
    1.0
    AUTHOR
    Andres Rivera Ramirez

    DESCRIPTION
    Remover las secuencias adaptadoras
    CATEGORY

    USAGE

    ARGUMENTS

    SEE ALSO


    '''

# Abrir el archivo
input_adapters = ("..\data\input_adapters.txt")
input_adapters_content = open(input_adapters)
# Leer el archivo por líneas
secuencias = input_adapters_content.readlines()
input_adapters_content.close()
# Crear el archivo que contendrá el resultado
output_noadapters = open("output_noadapters.txt", "a")
# Quitar el adaptador de cada línea y hacer append al archivo
for secuencia in secuencias:
    output_noadapters.write(secuencia[13:])
output_noadapters.close()
