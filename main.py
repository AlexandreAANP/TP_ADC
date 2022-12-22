import sys
import os
sys.path.append(os.getcwd())
from API.api_bicicletas import api_bicicleta
from API.api_aluguer import api_aluguer
from API.api_utilizador import api_utilizador
from Objetos.Aluguer import Aluguer
def menu():
    print("Menu-")
    api_aluguer.readFile()
    api_aluguer.add(Aluguer.create_aluguer())

if __name__ == "__main__":
    for i in api_utilizador.get_all():
        print(i)
    for i in api_aluguer.get_all():
        print(i)
    for i in api_bicicleta.get_all():
        print(i)
    menu()
