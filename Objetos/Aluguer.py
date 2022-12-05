from Bicicleta import Bicicleta
from Utilizador import Utilizador

class Aluguer:
    ID = 100000
    Lista_Aluguers = []
    def __init__(self, bicicleta: Bicicleta, utilizador :Utilizador):
        Aluguer.ID +=1
        self.__id = Aluguer.ID
        self.__bicicleta = bicicleta
        self.__utilizador = utilizador
        Aluguer.Lista_Aluguers.append(self)

    def __repr__(self):
        return f'''Aluguer(\n\n {self.__bicicleta}, {self.__utilizador} )'''

    def get_json_object(self):
        return {
            "utilizador" : self.__utilizador,
            "bicicleta" : self.__bicicleta,
            "id" : self.__id,
        }

    #TO DO 
    # contains method, procura se um objeto de Aluguer esta na lista Aluguer.Lista_Aluguers
    # retorna true se encontrar, pode receber como parametro ID ou o objeto
    
    #TO DO
    #User Story 0008
    #method que retorna o numero de serie da bicicleta alugada
print(Aluguer.ID, Aluguer(Bicicleta("d","d","d"),Utilizador("d","e","ds")), Aluguer.ID)