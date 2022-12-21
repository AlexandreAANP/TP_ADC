from Objetos.Bicicleta import Bicicleta


def menu():

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
    ------------------------------------------------------              
    """)

def main():
    while True :
        menu()
        # Escolher
        choice = input("Escolha uma opçao): ")

        # Inserir
        if choice == "1":
            print("Escolha a marca") 
            b1 = Bicicleta('MARCA','MODELO','COR','NUMERO Serie','DONO')
            item = input("Insira o item que quer inserir : ")
            print("Item adicionado com sucesso!")

        elif choice=="0":
            break
        else :
            print("Invalid choise.Try again")

main()