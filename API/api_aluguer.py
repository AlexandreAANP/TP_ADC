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
        if cls.file is not None:
            return False
        cls.file = FileReader(os.getcwd()+"/Data/"+cls.file_name, "Aluguer")
        return True
    #retorna uma lista com todas as bicicletas
    @classmethod
    def get_all(cls):
        cls.readFile()
        for value in cls.file.object_list:
            yield value


    #retorna um Aluguer consoante o id
    @classmethod
    def get_by_id(cls, id):
        for value in cls.get_all():
            if value.id == id:
                return value
        return None

    #retorna um Utilizador consoante o id do Aluguer
    @classmethod
    def get_utilizador_by_id(cls, id):
        for value in cls.get_all():
            if value.id == id:
                return value.utilizador
        return None

    #retorna uma bicicleta consoante o id do Aluguer
    @classmethod
    def get_bicicleta_by_id(cls, id):
        for value in cls.get_all():
            if value.id == id:
                return value.bicicleta
        return None


    #retorna o valor se o conter na lista
    @classmethod
    def contains(cls, a: Aluguer):
        for value in cls.get_all():
            if value == a:
                return value
        return None


    #retorna uma lista de todos os aluguers que o utilizador tem
    @classmethod
    def get_by_utilizador(cls, user:Utilizador):
        res = []
        for value in cls.get_all():
            if value.utilizador == user:
                res.append(value)
        return res 

    #retorna o aluguer que esteja a alugar a bicicleta como parametro
    @classmethod
    def get_by_bicicleta(cls, b:Bicicleta):
        for value in cls.get_all():
            if value.bicicleta == b:
                return value
        return None


    #Adiciona um Aluguer, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def add(cls, user: Utilizador, bike: Bicicleta):
        if cls.file is None:
            cls.readFile()
        cls.file.object_list.append(Aluguer(user,bike))
        cls.file.fileSave()
    @classmethod
    def add(cls, a: Aluguer):
        if cls.file is None:
            cls.readFile()
        cls.file.object_list.append(a)
        cls.file.fileSave()


    #Remove um Utilizador, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def delete(cls, a: Aluguer):
        if cls.file is None:
            cls.readFile()
        cls.file.object_list.remove(a)
        cls.file.fileSave()

api_aluguer.add(Aluguer(Bicicleta("1","1","1"),Utilizador("das","aa","dad")))

for i in api_aluguer.get_all():
    print(i)
print(api_aluguer.get_all())