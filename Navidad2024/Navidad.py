import os
import time

# Códigos de color ANSI
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BROWN = "\033[38;5;94m"  # color café (tronco)
RESET = "\033[0m"

def clear_console():
    """Limpia la consola en Windows, Linux o macOS."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear_console()
    print("Presiona ENTER para")
    print("ver tu árbol de Navidad...")
    input()  # Espera a que el usuario presione Enter
    clear_console()

    # --- FRAME 1: Árbol básico (solo una estrella en la punta) ---
    frame1 = f"""\
      {YELLOW}*{RESET}      
     {GREEN}***{RESET}     
    {GREEN}*****{RESET}    
   {GREEN}*******{RESET}   
  {GREEN}*********{RESET}  
 {GREEN}***********{RESET} 
{GREEN}*************{RESET}
     {BROWN}|||{RESET}     
     {BROWN}|||{RESET}     
"""

    # --- FRAME 2: Con algunos adornos rojos (o) ---
    frame2 = f"""\
      {YELLOW}*{RESET}      
     {GREEN}***{RESET}     
    {GREEN}**{RED}o{GREEN}**{RESET}    
   {GREEN}***{RED}o{GREEN}***{RESET}   
  {GREEN}***{RED}o{GREEN}*{RED}o{GREEN}***{RESET}  
 {GREEN}*****{RED}o{GREEN}*****{RESET} 
{GREEN}***{RED}o{GREEN}*****{RED}o{GREEN}***{RESET}
     {BROWN}|||{RESET}     
     {BROWN}|||{RESET}     
"""

    # --- FRAME 3: Cambiamos la posición de los adornos ---
    frame3 = f"""\
      {YELLOW}*{RESET}      
     {GREEN}***{RESET}     
    {GREEN}*{RED}o{GREEN}*{RED}o{GREEN}*{RESET}    
   {GREEN}**{RED}o{GREEN}*{RED}o{GREEN}**{RESET}   
  {GREEN}**{RED}o{GREEN}***{RED}o{GREEN}**{RESET}
 {GREEN}**{RED}o{GREEN}*****{RED}o{GREEN}**{RESET}
{GREEN}**{RED}o{GREEN}***{RED}o{GREEN}***{RED}o{GREEN}**{RESET}
     {BROWN}|||{RESET}     
     {BROWN}|||{RESET}     
"""

    frames = [frame1, frame2, frame3]

    # Repetimos la animación varias veces
    for _ in range(6):
        for fr in frames:
            clear_console()
            print(fr)
            time.sleep(0.6)  # Ajusta el tiempo de parpadeo

    # Mensaje final
    clear_console()
    print(f"{YELLOW}¡Feliz Navidad y próspero{RESET}")
    print(f"{YELLOW}Año Nuevo!{RESET}")
    print(f"{GREEN}Que la magia de estas fiestas{RESET}")
    print(f"{GREEN}llene tu vida de alegría.{RESET}\n")
    time.sleep(3)

if __name__ == "__main__":
    main()
