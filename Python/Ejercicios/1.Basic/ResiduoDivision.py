# Escriba una función que acepte dos números enteros y 
# devuelva el residuo de dividir el valor mayor 
# por el valor menor.

def residuoDivision(a, b):
    if a > b:
        if b == 0:
            return "NaN"
        return a % b
    else:
        if a == 0:
            return "NaN"
        return b % a
    
def main():
    n = int(input("Ingrese el primer número: "))
    m = int(input("Ingrese el segundo número: "))
    result = residuoDivision(n, m)
    print("n = ", n, "\nm = ", m, "\nResiduo = ", result)

main()