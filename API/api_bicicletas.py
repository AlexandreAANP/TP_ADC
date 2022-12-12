import os
import sys

from API.FileReader import FileReader
from Objetos.Bicicleta import Bicicleta

class api_bicicleta:
    file_name = 'bicicleta.json'
    file = None


    #Lê o ficheiro apenas a primeira vez  retorna false se já foi lido o ficheiro
    @classmethod
    def readFile(cls):
        """
        Instancia um objeto da class FileReader tendo como parametros:
        - api_bicicleta.file_name = 'bicicleta.json'
        - Nome da class a qualquer corresponde o tipo de dado -> 'Bicicleta'
        Guarda na variável de class "file"
        @return: retorna true caso é possivel ler o ficheiro com sucesso
        @rtype: boolean
        """
        if cls.file is not None:
            return False
        cls.file = FileReader(os.getcwd()+"/Data/"+cls.file_name, "Bicicleta")
        return True
    #retorna uma lista com todas as bicicletas
    @classmethod
    def get_all(cls):
        """
        Este metódo vai buscar todos os dados do ficheiro e retorna uma lista de objetos do tipo Bicicleta
        @return: returna interator, como fosse uma lista
        @rtype: Interator
        """
        cls.readFile()
        for value in cls.file.object_list:
            yield value


    #retorna uma bicicleta consoante o numeroserie
    @classmethod
    def get_by_numSerie(cls, numSerie):
        """
        Consoante o numSerie irá retornar um objeto com o respetivo id
        @param numSerie: recebe o id do Objeto Bicicleta
        @type numSerie: int
        @return: Objeto Aluguer
        @rtype: Aluguer or None
        """
        for value in cls.get_all():
            if value.numeroSerie == numSerie:
                return value
        return None



    #retorna uma lista com todas as bicicletas com a especifica marca não é case sensitive
    @classmethod
    def get_by_marca(cls,marca: str):
        """
        Consoante a marca irá retornar um objeto com o respetiva marca
        @param marca: recebe uma marca do Objeto Bicicleta
        @type marca: str
        @return: Retorna uma lista de Objetos Bicicletas
        @rtype: list
        """
        res = []
        for value in cls.get_all():
            if value.marca.lower() == marca.lower():
                res.append(value)
        return res

    #retorna uma lista com todas as bicicletas com a especifica cor não é case sensitive
    @classmethod
    def get_by_cor(cls, cor: str):
        """
        Consoante a marca irá retornar um objeto com o respetiva cor
        @param cor: recebe uma cor do Objeto Bicicleta
        @type cor: str
        @return: Retorna uma lista de Objetos Bicicletas
        @rtype: list
        """
        res = []
        for value in cls.get_all():
            if value.cor.lower() == cor.lower():
                res.append(value)
        return res
    
    #retorna por index
    @classmethod
    def get_by_index(cls, index: int):
        """
        Consoante o index irá retornar um objeto com respetivo index
        @param index: recebe um index referente a lista de Bicicleta
        @type index: int
        @return: Retorna um Objeto Bicicleta
        @rtype: Bicicleta or None
        """
        counter = 0
        for value in cls.get_all():
            if counter == index:
                return value
            counter +=1
        return None

    #retorna o valor se o conter na lista
    @classmethod
    def contains(cls, bike: Bicicleta):
        """
        Caso encontre um objeto igual ao dado como parametro retorna o devolta, caso contrário retorna None
        @param bike: recebe um objeto de Bicicleta
        @type bike: Bicicleta
        @return: retorna um Objeto de Bicicleta ou None
        @rtype: Bicicleta or None
        """
        for value in cls.get_all():
            if value == bike:
                return value
        return None


    #replace, susbstitui na lista dado um objeto igual
    @classmethod
    def replace(cls, old: Bicicleta, new: Bicicleta):
        """
        Através do Parametro old compara esse valor com dentro da lista
        caso encontre substitui pelo o paramtro new e retorna True.
        Caso Contrário retorna apenas False
        @param old: recebe um objeto de Bicicleta
        @type old: Bicicleta
        @param new: recebe um objeto de Bicicleta
        @type new: Bicicleta
        @return: retorna True caso seja Substituidp com sucesso. Falso caso não foi possivel 
        @rtype: bool
        """
        counter = 0
        for value in cls.get_all():
            if value == old:
                try:
                    cls.file.object_list[counter] = new
                except:
                    return False
                cls.file.fileSave()
                return True
            counter+=1
        return False

    #Adiciona uma bicicleta, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def add(cls, bike: Bicicleta):
        """
        Adiciona uma Bicicleta nos dados e na lista em memória através de Objeto Bicicleta
        @param bike: recebe um objeto de Bicicleta
        @type bike: Bicicleta
        @return: retorna True caso seja adicionado um Aluguer com sucesso. Falso caso exista algum erro 
        @rtype: bool
        """
        try:
            if cls.file is None:
                cls.readFile()
            cls.file.object_list.append(bike)
            cls.file.fileSave()
            return True
        except:
            return False


    #Remove uma bicicleta, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def delete(cls, bike: Bicicleta):
        """
        Remove um Bicicleta através do parametro que recebe, ou seja caso sejam igual e atualiza o ficheiro
        @param bike: recebe um objeto de Bicicleta
        @type bike: Bicicleta
        @return: retorna True caso seja eliminado uma Bicicleta com sucesso. Falso caso exista algum erro 
        @rtype: bool

        """
        try:
            if cls.file is None:
                cls.readFile()
            cls.file.object_list.remove(bike)
            cls.file.fileSave()
            return True
        except:
            return False
