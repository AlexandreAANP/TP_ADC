import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from Objetos.Bicicleta import Bicicleta
from API.api_bicicletas import api_bicicleta



def menu_principal():
    """
        Esta função vai imprimir o menu Bicicletas
    """
    print("""

                        Menu 
    ------------------------------------------------------
                1 - Gerir Bicicletas
                2 - Gerir Utilizadores
                3 - Gerir Alugueres
                4 - Sair
    ------------------------------------------------------       
    """)
    choice = input()
    if input == 1:
        pass
    elif input == 2:
        pass
    elif input == 3:
        pass
    elif input == 4:
        quit
    else:
        print("Insira uma opçao valida.")
        menu_principal()


def main():
    while True :
        menu()
        # Escolher
        choice = input("Escolha uma opçao): ")

        # Inserir
        if choice == "1":
            Marca = input("Insira a Marca : ")
            Modelo = input("Insira o modelo : ")
            Cor = input("Insira a cor : ")
            

            api_bicicleta.add(Bicicleta(Marca,Modelo,Cor))
            

        #Eliminar
        elif choice == "2":
            print("mi")
        
        #Listar
        elif choice == "3":
            for i in api_bicicleta.get_all():
                print(i) 

        elif choice =="0":
            break
        else :
            print("Invalid choise.Try again")

main()