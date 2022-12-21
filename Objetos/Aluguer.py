import random
import sys
import os
import time

sys.path.append(os.getcwd())
from Objetos.Bicicleta import Bicicleta
from Objetos.Utilizador import Utilizador

class Aluguer:
    """
        Criamos uma variavel chamada ID que vai começar no 1000
        Criamos uma lista chamada de Lista_Aluguers onde vamos guardar todos os alugueres 
    """
    ID = 1000
    Lista_Aluguers = []

    def __init__(self, bicicleta: Bicicleta, utilizador :Utilizador, id = None):
        """Bicicleta
            No construtor, declaramos os atributos que definem o objeto
            @param bicicleta: recebe uma bicicleta do tipo Bicicleta
            @param utilizador: recebe um utilizador do tipo Utilizador 
            @param id: não recebe nada
        """

        self.__bicicleta = bicicleta
        self.__utilizador = utilizador
        Aluguer.Lista_Aluguers.append(self)
        
        """
            Se não for introduzido nenhum id, vai ser adicionado +1 ao id que estava anteriormente.
            Se for introduzido um id, esse mesmo vai ser guardado na variavel id     
        """
        if id is None:
            Aluguer.ID +=1
            self.__id = Aluguer.ID
        else:
            self.__id = id



    @property
    def id(self):
        """
            Função para ir buscar o id do aluger
            @return: id do aluguer
        """
        return self.__id

    @property
    def utilizador(self):
        """
            Metodo para apresentar o objeto Utilizador
            @return: utilizador
        """
        return self.__utilizador

    @property
    def bicicleta(self):
        """
            Metodo para apresentar o objeto Bicicletas
            @return: Bicicleta
        """
        return self.__bicicleta

    def __repr__(self):
        """
            Metodo que vai imprimir um Aluguer apresentando a bicicleta e o utilizador 
            @return: Retorna uma String que representa a bicicleta
        """
        return f'''Aluguer(\n\n{self.__id}, {self.__bicicleta}, {self.__utilizador} )'''

    def get_json_object(self):
        """
            Metodo para retornar o objeto da mesma maneira que é guardado no json em formato dict
            @return: Retorna o dict
        """
        return {
            "utilizador" : self.__utilizador.id,
            "bicicleta" : self.__bicicleta.numeroSerie,
            "id" : self.__id,
        }


    @classmethod
    def contains(cls, parameter):
        """
            Caso encontre um input igual ao dado como parametro retorna-o e devolve-o 
            @param parameter: recebe um input(parameter)
            @return: o input    
        """

        return cls.Lista_Aluguers.__contains__(parameter)

    def get_bicicleta_id(self):
        """
            Metodo para apresentar o numero de serie da bicicleta
            @return: o numero de serie da bicicleta
        """
        return self.bicicleta.numeroSerie


    @classmethod
    def random_delete_aluguer(cls):
        """
            Metodo para eliminar um aluguer 
        """
        aluguer = random.choice(Aluguer.Lista_Aluguers)
        print("Deleted ", aluguer.id)
        Aluguer.Lista_Aluguers.remove(aluguer)
        del aluguer
        print(Aluguer.Lista_Aluguers)


    @classmethod
    def random_create_aluguer(cls):
        """
            Metodo para criar um aluguer com valores aleatóriosde 3 em 3 segundos
        """
        aluguer = Aluguer(Bicicleta.get_random_bike(), Utilizador.get_random_user())
        print(f"Aluguer {aluguer.id}: {aluguer.utilizador.nome} alugou {aluguer.bicicleta.modelo}")
        while True:
            time.sleep(3)
            aluguer = Aluguer(Bicicleta.get_random_bike(), Utilizador.get_random_user())
            print(f"Aluguer {aluguer.id}: {aluguer.utilizador.nome} alugou {aluguer.bicicleta.modelo}")
            if random.randint(0, 5) == 4:
                Aluguer.delete_aluguer()
