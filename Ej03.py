#Desarrollar una función que reciba un texto e invierta el orden de las palabras siendo la
#última palabra la primera y la primera la última, debe devolver el texto invertido

def invertir(texto):
    palabras_separadas = texto.split() #Creamos una lista que almacena todas las palabras del texto ingresado
    palabrasInvertidas = []
    for palabra in reversed(palabras_separadas):
        palabrasInvertidas.append(palabra)

    textoInvertido = " ".join(palabrasInvertidas)
    return textoInvertido

texto = input("ingrese un texto: \n")
resultadoFuncion = invertir(texto)
print(resultadoFuncion) 