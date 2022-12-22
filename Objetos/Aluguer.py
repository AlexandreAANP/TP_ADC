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
        if not self.fileReader.object_list.__contains__(self):
            self.fileReader.object_list.append(self)
        if writeFile == True:

            self.fileReader.fileSave()


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
        return cls.Lista_Aluguers.__contains__(parameter)

    # Ver isto melhor
    def get_bicicleta_id(self):
        """
            @return: 
        """
        return self.bicicleta.numeroSerie

    @classmethod
    def create_aluguer(cls):
        """
        
        """
        aluguer = Aluguer(Bicicleta.get_random_bike(), Utilizador.get_random_user())
        print(f"Aluguer {aluguer.id}: {aluguer.utilizador.nome} alugou {aluguer.bicicleta.modelo}")
        return aluguer


    @classmethod
    def delete_aluguer(cls):
        """
        
        """
        aluguer = random.choice(Aluguer.Lista_Aluguers)
        print(f"Acabou o aluguer com o ID {aluguer.id} de {aluguer.utilizador.nome}. Durou {random.randint(0, 24)} horas.")
        Aluguer.Lista_Aluguers.remove(aluguer)
        del aluguer
