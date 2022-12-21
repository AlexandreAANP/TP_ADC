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



def menu():
    """
        Esta função vai imprimir o menu Bicicletas
    """
    print("""

                        Bicicletas 
    ------------------------------------------------------
                1 - Inserir Bicicleta
                2 - Eliminar Bicicleta
                3 - Listar Bicicletas
                4 -
                5 - 
                6 - Guardar
                7 - Carregar tudo
                0 - Sair
    ------------------------------------------------------       0       
    """)


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
            Numero = input("Insira o numero : ")
            Serie = input("Insira a serie : ")
            Dono = input("Insira o Dono : ")

            api_bicicleta.add(Bicicleta(Marca,Modelo,Cor,Serie,Dono))
            

        #Eliminar
        elif choice == "2":
            print("dkjlad")
        
        #Listar
        elif choice == "3":
          
            print("dadwdd")

        elif choice =="0":
            break
        else :
            print("Invalid choise.Try again")

main()