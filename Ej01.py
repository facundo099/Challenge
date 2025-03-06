#Desarrollar una función que reciba una palabra y devuelva True en caso de ser un
#palíndromo y False en caso de no serlo.

def esPalindromo(palabra):
    palabra_invertida = palabra[::-1]  # Invierto la palabra para guardarla en una variable
    if palabra == palabra_invertida: # Si la palabra invertida es igual a la palabra original retorno True, sino False
        return True
    else:
        return False

palabra = input("Ingrese una palabra: ")
resultado = esPalindromo(palabra)
print(resultado)
