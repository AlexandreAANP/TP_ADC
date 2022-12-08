import sys
import os
sys.path.append(os.getcwd())
from Objetos.Bicicleta import Bicicleta
from Objetos.Utilizador import Utilizador

class Aluguer:
    ID = 100000
    Lista_Aluguers = []
    def __init__(self, bicicleta: Bicicleta, utilizador :Utilizador, id = None):
        
        if id is None:
            Aluguer.ID +=1
            self.__id = Aluguer.ID
        else:
            self.__id = id

        self.__bicicleta = bicicleta
        self.__utilizador = utilizador
        Aluguer.Lista_Aluguers.append(self)


    @property
    def id(self):
        return self.__id

    @property
    def utilizador(self):
        return self.__utilizador

    @property
    def bicicleta(self):
        return self.__bicicleta

    def __repr__(self):
        return f'''Aluguer(\n\n {self.__bicicleta}, {self.__utilizador} )'''

    def get_json_object(self):
        return {
            "utilizador" : self.__utilizador.id,
            "bicicleta" : self.__bicicleta.numeroSerie,
            "id" : self.__id,
        }

    #TO DO 
    # contains method, procura se um objeto de Aluguer esta na lista Aluguer.Lista_Aluguers
    # retorna true se encontrar, pode receber como parametro ID ou o objeto
    
    #TO DO
    #User Story 0008
    #method que retorna o numero de serie da bicicleta alugada
