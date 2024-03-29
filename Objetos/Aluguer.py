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

    fileReader = None

    def __init__(self, bicicleta: Bicicleta, utilizador :Utilizador, id = None, writeFile = True):
        """
            Bicicleta
            No construtor, declaramos os atributos que definem o objeto

            :param Bicicleta: recebe bicicleta
            :type Bicicleta: bicicleta

            :param Utilizador: recebe utilizador 
            :type Utilizador: utilizador

            :param id: recebe id
            :type int: id

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
        if not self.fileReader.object_list.__contains__(self):
            self.fileReader.object_list.append(self)
        if writeFile == True:

            self.fileReader.fileSave()


    @property
    def id(self):
        """
            Metodo para ir buscar o id do aluger
            
            :return: id
            :rtype: Aluguer or none
        """
        return self.__id

    @property
    def utilizador(self):
        """
            Metodo para apresentar o objeto Utilizador
            
            :return: utilizador
            :rtype: utilizador
        """
        return self.__utilizador

    @property
    def bicicleta(self):
        """
            Metodo para apresentar o objeto Bicicletas
            ´
            :return: bicicleta
            :rtype: bicicleta
        """
        return self.__bicicleta

    def __repr__(self):
        """
            Metodo que vai imprimir um Aluguer apresentando a bicicleta e o utilizador 
            
            :return: Retorna uma String que apresenta quem fez o aluguer
            :rtype: Aluguer

        """
        return f'''Aluguer(\n\n{self.__id}, {self.__bicicleta}, {self.__utilizador} )'''

    def get_json_object(self):
        """
            Metodo para retornar o objeto da mesma maneira que é guardado no json em formato dict
            
            :return: utilizador, bicicleta, id 
            :rtype: dict
        """
        return {
            "utilizador" : [
                self.__utilizador.nome,
                self.__utilizador.idade,
                self.__utilizador.morada,
                self.__utilizador.id
            ],
            "bicicleta" : [
                self.__bicicleta.marca,
                self.__bicicleta.modelo,
                self.__bicicleta.cor,
                self.__bicicleta.numeroSerie
                           ],
            "id" : self.__id,
        }


    @classmethod
    def contains(cls, parameter):
        """
            Este metodo vai verificar se o parametro existe la lista

            :return: retorna um aluger 
            :rtype Aluger:
        """
        return cls.Lista_Aluguers.__contains__(parameter)


    def get_aluguer_id(self):
        """
            Este metodo vai apresentar o id do objeto Aluguer
            :return: id
            :rtype int: 
        """
        return self.id

    @classmethod
    def random_create_aluguer(cls):
        """
            Metodo para criar um aluguer com valores aleatórios

            :return: id,bicicleta,utilizador
            :rtype Aluguer:

        """
        aluguer = Aluguer(Bicicleta.get_random_bike(), Utilizador.get_random_user())
        print(f"Aluguer {aluguer.id}: {aluguer.utilizador.nome} alugou {aluguer.bicicleta.modelo}")
        return aluguer


    @classmethod
    def random_delete_aluguer(cls):
        """
            Metodo para eliminar um aluguer 
        """
        aluguer = random.choice(Aluguer.Lista_Aluguers)
        print(f"Acabou o aluguer com o ID {aluguer.id} de {aluguer.utilizador.nome}. Durou {random.randint(0, 24)} horas.")
        Aluguer.Lista_Aluguers.remove(aluguer)
        del aluguer
