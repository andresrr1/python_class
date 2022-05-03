'''NAME
fasta
VERSION
1.1
AUTHOR
Andres Rivera Ramirez
DESCRIPTION
Se genera un archivo un fasta con la secuencia dentro de un archivo de texto llamado dna.txt
CATEGORY
USAGE
Se requiere de un archivo dna.txt dentro de una carpeta data
ARGUMENTS
SEE ALSO
'''
# Se obtiene la ruta del archivo
from typing import IO


try:
    archivo_txt = (".\data\dna.txt")
    # Se abre el archivo para lectura
    my_file = open(archivo_txt)
    # Se lee el archivo y se guarda su contenido en una variable
    my_file_content = my_file.read()

    # Se crea el archivo fasta y se puede escribir en el
    archivo_fasta = open(".\myresults\dna.fasta", "w")

    # Se escribe en el archivo
    archivo_fasta.write(">sequence_name\n")
    archivo_fasta.write(my_file_content)

    # Se cierran los archivos
    archivo_fasta.close()
    my_file.close()
except IOError as ex:
    print("No es posible acceder al archivo" + ex.strerror)
