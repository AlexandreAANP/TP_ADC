import sys
import os
sys.path.append(os.getcwd())
from API.api_bicicletas import api_bicicleta
from API.api_aluguer import api_aluguer
from API.api_utilizador import api_utilizador
def menu():
    print("Menu")


if __name__ == "__main__":
    for i in api_utilizador.get_all():
        print(i)
    for i in api_aluguer.get_all():
        print(i)
    for i in api_bicicleta.get_all():
        print(i)
    menu()
