#Desarrollar una función que reciba un texto e identifique que todos los paréntesis estén
#balanceados (chequear que siempre que se abra un paréntesis este se cierre), devolver
#True caso que así sea, False caso contrario

def identificar(texto):
    tam = len(texto)
    contador = 0
    for i in range(tam):
        if(texto[i] == '('): #Si encuentro un ( sumo 1 al contador
            contador += 1
        if(texto[i] == ')' and contador == 1):#Si encuentro un ) y el contador esta en 1 por haber encontrado el ( entonces pongo en 0 al contador y retorno true
            contador = 0

    if(contador == 2 or texto[tam - 1] == '(' ): #Si el contador llega a 2 es porque encontro dos ( o si el ultimo caracter es tambien un (
        return False
    return True

texto = input("ingrese un texto e identificare si hay parentesis desbalanceados: \n")
resultadoFuncion = identificar(texto)
print(resultadoFuncion)