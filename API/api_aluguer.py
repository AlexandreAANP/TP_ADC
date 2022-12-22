import os
import sys

from API.FileReader import FileReader
from Objetos.Aluguer import Bicicleta, Utilizador, Aluguer


class api_aluguer:
    
    file_name = 'aluguer.json'
    file = None


    #Lê o ficheiro apenas a primeira vez retorna false se já foi lido o ficheiro
    @classmethod
    def readFile(cls):
        """
        Instancia um objeto da class FileReader tendo como parametros:
        - api_aluguer.file_name = 'aluguer.json'
        - Nome da class a qualquer corresponde o tipo de dado -> 'Aluguer'
        Guarda na variável de class "file"
        @return: retorna true caso é possivel ler o ficheiro com sucesso
        @rtype: boolean
        """

        if cls.file is not None:
            return False
        cls.file = FileReader(os.getcwd()+"/Data/"+cls.file_name, "Aluguer")
        return True
    #retorna uma lista com todas as bicicletas
    @classmethod
    def get_all(cls):
        """
        Este metódo vai buscar todos os dados do ficheiro e retorna uma lista de objetos do tipo Aluguer
        @return: returna interator, como fosse uma lista
        @rtype: Interator
        """

        cls.readFile()
        for value in cls.file.object_list:
            yield value


    #retorna um Aluguer consoante o id
    @classmethod
    def get_by_id(cls, id):
        """
        Consoante o id irá retornar um objeto com o respetivo id
        @param id: recebe o id do Objeto Aluguer
        @type id: int
        @return: Objeto Aluguer
        @rtype: Aluguer or None
        """

        for value in cls.get_all():
            if value.id == id:
                return value
        return None


    #retorna o valor se o conter na lista
    @classmethod
    def contains(cls, aluguer: Aluguer):
        """
        Caso encontre um objeto igual ao dado como parametro retorna o devolta caso contrário retorna None
        @param aluguer: recebe um objeto de Aluguer
        @type aluguer: Aluguer
        @return: retorna um Objeto de Aluguer ou None
        @rtype: Aluguer or None
        """

        for value in cls.get_all():
            if value == aluguer:
                return value
        return None


    #retorna uma lista de todos os aluguers que o utilizador tem
    @classmethod
    def get_by_utilizador(cls, user:Utilizador):
        """
        Através do Utilizador dado como parametro retorna uma lista que coicide os alugueres desse mesmo Utilizador
        @param user: Recebe um Objeto de Utilizador
        @type user: Utilizador
        @return: retorna uma lista de objetos utilizadores
        @rtype: list
        """

        res = []
        for value in cls.get_all():
            if value.utilizador == user:
                res.append(value)
        return res 

    #retorna o aluguer que esteja a alugar a bicicleta como parametro
    @classmethod
    def get_by_bicicleta(cls, bike:Bicicleta):
        """
        Este metodo vai buscar o aluguer que corresponde a bicicleta dada como parametro
        @param bike: Recebe como parametro um Objeto de bicicleta
        @type bike: Bicicleta
        @return: retorna um Objeto de Bicicleta
        @rtype: Bicicleta
        """

        for value in cls.get_all():
            if value.bicicleta == bike:
                return value
        return None


    #Adiciona um Aluguer, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def add(cls, user: Utilizador, bike: Bicicleta):
        """
        Adiciona um Aluguer nos dados e na lista em memória através dos Objetos Utilizador e Bicicleta
        @param user: recebe um objeto de Utilizador
        @type user: Utilizador
        @param bike: recebe um objeto de Bicicleta
        @type bike: Bicicleta
        @return: retorna True caso seja adicionado um Aluguer com sucesso. Falso caso exista algum erro 
        @rtype: bool
        """
        cls.add(Aluguer(user,bike))
        
    @classmethod
    def add(cls, aluguer: Aluguer):
        """
        Adiciona um Aluguer nos dados e na lista em memória através de Objeto Aluguer
        @param aluguer: recebe um objeto de Aluguer
        @type aluguer: Aluguer
        @return: retorna True caso seja adicionado um Aluguer com sucesso. Falso caso exista algum erro 
        @rtype: bool
        """
        try:
            if cls.file is None:
                print(cls.readFile())
            print(cls.file)
            cls.file.object_list.append(aluguer)
            cls.file.fileSave()
            return True
        except:
            return False


    #Remove um Aluguer, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def delete(cls, a: Aluguer):
        """
        Remove um Aluguer através do parametro que recebe, ou seja caso sejam igual e atualiza o ficheiro
        @param aluguer: recebe um objeto de Aluguer
        @type aluguer: Aluguer
        @return: retorna True caso seja eliminado um Aluguer com sucesso. Falso caso exista algum erro 
        @rtype: bool
        """
        try:
            if cls.file is None:
                cls.readFile()
            cls.file.object_list.remove(a)
            cls.file.fileSave()
            return True
        except:
            return False

