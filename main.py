"""
import sys
import os
sys.path.append(os.getcwd())
from API.api_bicicletas import api_bicicleta
from API.api_aluguer import api_aluguer
from API.api_utilizador import api_utilizador
from Objetos.Aluguer import Aluguer
from menu import menu

def menus():
    menu.menu_principal()


    for i in api_utilizador.get_all():
       print("lldld0"+str(i))
    for i in api_utilizador.get_all():
       print("lldld0"+str(i))
    for i in api_aluguer.get_all():
      print(i)
    menus()
"""