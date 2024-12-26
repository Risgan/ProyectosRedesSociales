# Escribir los n números primos segun sea ingresado por el usuario

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def main():
    contador = 0
    numeroPrimos = int(input("Ingrese un número: ")) 
    numero = 0


    while contador < numeroPrimos:
        if es_primo(numero):
            print(numero)
            contador += 1
        numero += 1

main()