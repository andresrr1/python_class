'''
NAME
    porcentaje_aa
VERSION
    1.2
AUTHOR
    Andres Rivera Ramirez

DESCRIPTION
    Este programa obtiene el porcentaje de un aminoacido en una secuencia dada, 
    ambos introducidos como argumentos desde la terminal
CATEGORY
    aminoacids
USAGE
    python src/porentaje_aa.py [-h] -i La secuencia de aminoacidos requerida -a AMINOACIDO
ARGUMENTS
   -h, --help            show this help message and exit
  -i La secuencia de aminoacidos requerida, --input La secuencia de aminoacidos requerida
                        Secuencia de aminoacidos
  -a AMINOACIDO, --aminoacido AMINOACIDO
                        El aminoacido a buscar
SEE ALSO


'''

import argparse

parser = argparse.ArgumentParser(
    description=" Este programa calcula el contenido de un aminoacido dado en una secuencia dada")

parser.add_argument("-i", "--input",
                    metavar="La secuencia de aminoacidos requerida",
                    help="Secuencia de aminoacidos",
                    required=True)

parser.add_argument("-a", "--aminoacido",
                    help="El aminoacido a buscar",
                    required=True)


args = parser.parse_args()

# Se obtiene el porcentaje de aminoacido con esta funcion


def get_aa_content(secuencia_aa, contar_aa):
    
    secuencia_aa = str(args.input)
    contar_aa = args.aminoacido
    
    secuencia_aa = secuencia_aa.upper()
    contar_aa = contar_aa.upper()
    
    # Se verifica que los datos sean validos para la funcion
    if(any(char.isdigit() for char in secuencia_aa)):
        raise ValueError("La secuencia contiene uno o mas numeros")
    if(len(contar_aa) > 1):
        raise ValueError("Por favor, introduzca solo un aminoacido a buscar")
    if(contar_aa.isdigit()):
        raise ValueError("Introduzca un aminoacido valido")

    len_secuencia = len(secuencia_aa)
    contenido_aa = secuencia_aa.count(contar_aa)
    porcentaje = ((contenido_aa / len_secuencia) * 100)
    
    return(porcentaje)


# Se llama a la funcion y se guarda el return en una variable para despues imprimirla
porcentaje_aa = get_aa_content(args.input, args.aminoacido)
print(
    f"El porcentaje de {args.aminoacido} en la secuencia introducida es de: \n {porcentaje_aa}%")

