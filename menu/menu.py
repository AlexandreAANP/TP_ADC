import sys
import os
sys.path.append(os.getcwd())

from API.api_bicicletas import api_bicicleta
from API.api_aluguer import api_aluguer
from API.api_utilizador import api_utilizador

from Objetos.Aluguer import Aluguer
from Objetos.Utilizador import Utilizador
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
        menu_bicicletas()
        #Aluguer.create_aluguer()
    elif choice == 2:
        menu_utilizadores()
    elif choice == 3:
        menu_alugueres()
    elif choice == 4:
        sys.exit(0)
    else:
        print("Insira uma opçao valida.")
        menu_principal()


def menu_bicicletas():

        # Escolher
        choice = int(input(
            
        """ 
        Bicicletas
        Escolha uma opçao: 
        1 - Inserir Bicicletas
        2 - Eliminar Bicicletas pelo o Numero de Série
        3 - Listar todas as Bicicletas
        4 - Menu principal

        """))
        # Inserir
        if choice == 1:
            marca = input("Insira a Marca: ")
            modelo = input("Insira o modelo: ")
            cor = input("Insira a cor: ")
            numeroSerie = int(input("Insira um numero de serie: "))
            print("Bicicleta adicionada", Bicicleta(marca,modelo,cor,numeroSerie))
            menu_bicicletas()

        #Eliminar
        elif choice == 2:
            num = int(input("Insira o numero de serie para eliminar uma bicicleta:"))
            print("Bicicleta Eliminada", api_bicicleta.delete(api_bicicleta.get_by_numSerie(num)))
            menu_bicicletas()

        #Listar
        elif choice == 3:
            print("Lista de Bicicletas")
            for i in api_bicicleta.get_all():
                print(i)
            menu_bicicletas()
        
        elif choice == 4:
            menu_principal()
        else:
            print("Input invalido")
            menu_bicicletas()

def menu_utilizadores():

        # Escolher
        choice = int(input(
            
        """ 
        Utilizadores
        Escolha uma opçao: 
        1 - Inserir Utilizador
        2 - Eliminar Utilizador pelo o Numero de Série
        3 - Listar todas os Utilizadores
        4 - Menu principal
        """))
        # Inserir
        if choice == 1:
            nome = input("Insira um nome: ")
            idade = input("Insira a sua idade: ")
            morada = input("Insira uma morada: ")
            try:
                id = int(input("Insira um id: "))
            except(ValueError):
                id = None
                
            Utilizador(nome,idade,morada,id)
            menu_utilizadores()
        
        #Eliminar
        elif choice == 2:
            num = int(input("Insira o id do utilizador"))
            print("Bicicleta Eliminada", api_utilizador.delete(api_utilizador.get_by_id(num)))
            menu_utilizadores()
        
        #Listar
        elif choice == 3:
            print("Lista de Utilizadores")
            for i in api_utilizador.get_all():
                print(i)
            menu_utilizadores()

        elif choice == 4:
            menu_principal()

        else:
            print("Input invalido")
            menu_utilizadores()

def menu_alugueres():
        # Escolher
        choice = int(input(
            
        """ 
        Aluguer
        Escolha uma opçao: 
        1 - Inserir Aluguer
        2 - Eliminar Aluguer pelo o Numero de Série
        3 - Listar todas as Aluguer
        4 - Menu principal
        """))
        # Inserir
        if choice == 1:
            nome = input("Insira um nome: ")
            idade = input("Insira a sua idade: ")
            morada = input("Insira uma morada: ")
            id = int(input("Insira um id: "))
            Utilizador(nome,idade,morada,id)
            menu_alugueres()
        #Eliminar
        elif choice == 2:
            num = int(input("Insira o id do utilizador"))
            api_aluguer.delete(api_utilizador.get_by_id(num))
            menu_alugueres()
        #Listar
        elif choice == 3:
            print("Lista de Utilizadores")
            for i in api_utilizador.get_all():
                print(i)
            menu_alugueres()

        elif choice == 4:
            menu_principal()

        else:
            print("Input invalido")
            menu_alugueres()        

if __name__== "__main__":
    menu_principal()