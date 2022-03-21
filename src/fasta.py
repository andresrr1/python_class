#Se obtiene la ruta del archivo
my_file_name = ("..\data\dna.txt")
#Se abre el archivo para lectura
my_file = open(my_file_name)
#Se lee el archivo y se guarda su contenido en una variable
my_file_content = my_file.read()
#Se crea el archivo fasta y se puede escribir en el
my_file_two = open("dna.fasta", "w")
#Se escribe en el archivo
my_file_two.write(">sequence_name\n")
my_file_two.write(my_file_content)
#Se cierra el archivo
my_file_two.close()
