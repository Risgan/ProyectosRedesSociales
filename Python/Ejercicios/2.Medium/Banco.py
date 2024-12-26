# Banco GranJohn para ingresar y sacar dinero 
import os


class Banco:
    def __init__(self):
        self.saldo = 0

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            print('Saldo insuficiente')
            input('Presione enter para continuar')
        else:
            self.saldo -= monto

    def consultar_saldo(self):
        return self.saldo

banco = Banco()


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    print('1. Depositar')
    print('2. Retirar')
    print('3. Consultar saldo')
    print('4. Salir')
    return int(input('Ingrese una opción: '))
    



def main():
    global banco
    clear()
    opcion = menu()
    while opcion != 4:
        if opcion == 1:
            clear()
            monto = int(input('Ingrese el monto a depositar: '))
            banco.depositar(monto)
        elif opcion == 2:
            clear()
            monto = int(input('Ingrese el monto a retirar: '))
            banco.retirar(monto)
        elif opcion == 3:
            clear()
            print(f'Su saldo es: {banco.consultar_saldo()}')
            input('Presione enter para continuar')
        else:
            print('Opción inválida')
        clear()
        opcion = menu()
        clear()

main()




