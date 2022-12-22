import sys
import os
 
from API.api_bicicletas import api_bicicleta
from API.api_aluguer import api_aluguer
from API.api_utilizador import api_utilizador
from Objetos.Aluguer import Aluguer
from Objetos.Bicicleta import Bicicleta


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
    choice = int(input())
    if choice == 1:
        Aluguer.create_aluguer()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        sys.exit(0)
    else:
        print("Insira uma opçao valida.")
        menu_principal()


def menu_bicicletas():

        # Escolher
        choice = int(input("Escolha uma opçao:"))
        # Inserir
        if choice == 1:
            marca = input("Insira a Marca: ")
            modelo = input("Insira o modelo: ")
            cor = input("Insira a cor: ")
            api_bicicleta.add(Bicicleta(marca,modelo,cor))
        #Eliminar
        elif choice == 2:
            num = int(input("Insira numero de serie da bicicleta:"))
            api_bicicleta.delete(api_bicicleta.get_by_numSerie(num))
        #Listar
        elif choice == 3:
            for i in api_bicicleta.get_all():
                print(i)
        elif choice == 4:
            menu_principal()
        else:
            print("Input invalido")
            menu_bicicletas()