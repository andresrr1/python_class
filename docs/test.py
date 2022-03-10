saludo = "Buenos días"
nombre = "Andrea"
mensaje = saludo + ' ' + nombre
mensaje += '!'
print(len(mensaje)) #funcion
print(mensaje.find('Andrea')) #metodo, esta asociado a un objeto, encuentra la cadena dentro de otra cadena, rregresa -1 si no lo encuentra.

dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'
codon_inicio = 'TAC'
print('El codon de inicio se encuentra en la posición' ,dna.find(codon_inicio))