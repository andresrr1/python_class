'''NAME
    fasta files
    VERSION
    1.0
    AUTHOR
    Andres Rivera Ramirez

    DESCRIPTION
    Convertir las secuencias en formato fasta
    CATEGORY

    USAGE

    ARGUMENTS

    SEE ALSO


    '''

# Abrir el archivo con las secuencias
dna_sequences = ("..\data\dna_sequences.txt")
archivoseq = open(dna_sequences)
secuencias = archivoseq.readlines()
archivoseq.close()
# Guardar en variables los caracteres que quiero borrar
guiones = "-"
alt = "—"
# Utilizar replace para eliminar los caracteres no deseados
secuencias[2] = secuencias[2].replace(guiones, "")
secuencias[2] = secuencias[2].replace(alt, "")
# Crear un archivo fasta en append
dna_fasta = open("dna_sequences.fasta", "a")
# Escribir cada secuencia en formato fasta en el archivo
for seq in secuencias:
    dna_fasta.write("> " + seq[:5] + "\n" + seq[8:])
dna_fasta.close()
