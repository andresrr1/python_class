'''NAME
    crear_fasta
    VERSION
    2.0
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
try:
    dna_sequences = (".\data\dna_sequences.txt")
    archivoseq = open(dna_sequences)
    secuencias = archivoseq.readlines()
    archivoseq.close()
# Guardar en variables los caracteres que quiero borrar
    guiones = "-"
    alt = "—"
# Crear un archivo fasta en append
    dna_fasta = open(".\myresults\dna_sequences.fasta", "w")
# Escribir cada secuencia en formato fasta en el archivo
    for seq in secuencias:
        seq = seq.replace(guiones, "")
        seq = seq.replace(alt, "")
        seq = seq.replace('a', 'A')
        seq = seq.replace('g', 'G')
        seq = seq.replace('t', 'T')
        seq = seq.replace('c', 'C')
        dna_fasta.write(">" + seq[:5] + "\n" + seq[8:])
    dna_fasta.close()
    # En caso de que el archivo no se encuentre en la carpeta o no sea posible accesarlo
except IOError as ex:
    print("No es posible abrir el archivo: \n" + ex.strerror)
