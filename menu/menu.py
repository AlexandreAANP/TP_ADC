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
        """
            Menu das bicicletas
        """
        choice = int(input(
            
        """ 

        Escolha uma opçao: 
        1 - Inserir Bicicletas
        2 - Eliminar Bicicletas pelo o Numero de Série
        3 - Listar todas as Bicicletas
        4 - Menu principal

        """))

        if choice == 1:
            """
                Inserir uma bicicleta
            """
            marca = input("Insira a Marca: ")
            modelo = input("Insira o modelo: ")
            cor = input("Insira a cor: ")
            print("\n Bicicleta adicicionada ", Bicicleta(marca,modelo,cor))
            menu_bicicletas()

        elif choice == 2:
            """
                Eliminar uma bicicleta
            """
            num = int(input("Insira o numero de serie para eliminar uma bicicleta:"))
            print("Bicicleta Eliminada", api_bicicleta.delete(api_bicicleta.get_by_numSerie(num)))
            menu_bicicletas()

        elif choice == 3:
            """
                Imprime a lista de utilizadores
            """
            for i in api_bicicleta.get_all():
                print(i)
            menu_bicicletas()
        
        elif choice == 4:
            menu_principal()
        else:
            """
                Caso o input seja invalido
            """
            print("Input invalido")
            menu_bicicletas()

def menu_utilizadores():

        """
            Menu dos utilizadores
        """
        choice = int(input(
            
        """ 
        Utilizadores
        Escolha uma opçao: 
        1 - Inserir Utilizador
        2 - Eliminar Utilizador pelo o id
        3 - Listar todas os Utilizadores
        4 - Menu principal
        """))
        
        if choice == 1:
            """
                Inserir um utilizador, o id é gerado aleatóriamente
            """
            nome = input("Insira um nome: ")
            idade = input("Insira a sua idade: ")
            morada = input("Insira uma morada: ")
                
            Utilizador(nome,idade,morada)
            menu_utilizadores()
        
        elif choice == 2:
            """
                Elimina  um utilizador pelo o id
            """
            num = int(input("Insira o id do para eliminar um utilizador"))
            print("Utilizador Eliminada", api_utilizador.delete(api_utilizador.get_by_id(num)))
            menu_utilizadores()
        
        elif choice == 3:
            """
                Imprime a lista de utilizadores
            """
            for i in api_utilizador.get_all():
                print(i)
            menu_utilizadores()

        elif choice == 4:
            """
                Apresenta a lista de alugueres
            """
            menu_principal()

        else:
            """
                Caso o input seja invalido 
            """
            print("Input invalido")
            menu_utilizadores()

def menu_alugueres():
        """
            Menu dos alugueres
        """
        choice = int(input(
            
        """ 
        Aluguer
        Escolha uma opçao: 
        1 - Inserir Aluguer manualmente
        2 - Inserir Aluguer aleatóriamente 
        3 - Eliminar Aluguer pelo o id 
        4 - Listar todas as Aluguer
        5 - Menu principal
        """))


        if choice == 1:
            """
                Introduzir aluguer manualmente
            """
            numBici = int(input("Introduza o numero de serie da bicicleta: "))
            numUti = int(input("Introduza o id do utilizador")) 
            aluguer = Aluguer(api_bicicleta.get_by_numSerie(numBici),api_utilizador.get_by_id(numUti)) 
            print("Aluguer", aluguer)
            menu_alugueres()

        elif choice == 2:
            """
                Cria alugueres aleatóriamente
            """
            Aluguer.random_create_aluguer()
            menu_alugueres()
        
        elif choice == 3:
            """
                Eliminar pelo o id
            """
            num = int(input("Insira o id do alguer para eliminar"))
            api_aluguer.delete(api_aluguer.get_by_id(num))
            menu_alugueres()

        elif choice == 4:
            """
                Apresenta a lista de alugueres
            """
            for i in api_aluguer.get_all():
                print(i)
            menu_alugueres()

        elif choice == 5:
            """
                Vai para o meu principal
            """
            menu_principal()

        else:
            """
                Caso o input seja invalido 
            """
            print("Input invalido")
            menu_alugueres()        

if __name__== "__main__":
    """
        Executa o menu principal
    """
    menu_principal()