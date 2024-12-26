
# Dados 2 ascensores (llamados "izquierdo" y "derecho") en 
# un edificio de 3 pisos (numerados del 1 0al 2), 
# escriba una función que acepte 3

ejecution = True

left = 0
right = 0
call = 0

def ascensorMasCercano(leftIn, rightIn, callIn):
    global left, right
    if abs(leftIn - callIn) < abs(rightIn - callIn):
        left = callIn
        return "left"
    else:
        right = callIn
        return "right"
    
def main():
    global left, right, call, ejecution
    try:
        call = int(input("Ingrese el piso a llamar: "))
        masCercano = ascensorMasCercano(left, right, call)
        print("left\t", "right\t","call\t", "masCercano")
        print(left,"\t", right,"\t",call,"\t", masCercano)
    except ValueError:
        ejecution = False
        return
        
    

while ejecution:
    main()
