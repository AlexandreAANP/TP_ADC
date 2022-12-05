import os
import sys
sys.path.append(os.getcwd())
from FileReader import FileReader
from Objetos.Utilizador import Utilizador

class api_utilizador:
    file_name = 'utilizador.json'
    file = None


    #Lê o ficheiro apenas a primeira vez  retorna false se já foi lido o ficheiro
    @classmethod
    def readFile(cls):
        if cls.file is not None:
            return False
        cls.file = FileReader(os.getcwd()+"/Data/"+cls.file_name)
        return True
    #retorna uma lista com todas os utilziadores
    @classmethod
    def get_all(cls):
        cls.readFile()
        for value in cls.file.object_list:
            yield value

    #retorna uma lista com todas os Utilizadores com o especifico nome, não é case sensitive
    @classmethod
    def get_by_nome(cls,nome: str):
        res = []
        for value in cls.get_all():
            if value.nome.lower() == nome.lower():
                res.append(value)
        return res

    #retorna uma lista com todos os utilizadores com a especifica morada, não é case sensitive
    @classmethod
    def get_by_morada(cls, morada: str):
        res = []
        for value in cls.get_all():
            if value.morada.lower() == morada.lower():
                res.append(value)
        return res
    
    #retorna um utilizador consoante o id
    @classmethod
    def get_by_id(cls, id):
        for value in cls.get_all():
            if value.id == id:
                return value
        return None

    #retorna por index
    @classmethod
    def get_by_index(cls, index: int):
        counter = 0
        for value in cls.get_all():
            if counter == index:
                return value
            counter +=1
        return None

    #retorna o valor se o conter na lista
    @classmethod
    def contains(cls, u:Utilizador):
        for value in cls.get_all():
            if value == u:
                return value
        return None


    #replace, susbstitui na lista dado um objeto igual
    @classmethod
    def replace(cls, old: Utilizador, new: Utilizador):
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

    #Adiciona um Utilizador, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def add(cls, u: Utilizador):
        if cls.file is None:
            cls.readFile()
        cls.file.object_list.append(u)
        cls.file.fileSave()


    #Remove um Utilizador, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def delete(cls, u: Utilizador):
        if cls.file is None:
            cls.readFile()
        cls.file.object_list.remove(u)
        cls.file.fileSave()