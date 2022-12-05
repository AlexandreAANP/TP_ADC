import os
import sys
sys.path.append(os.getcwd())
from FileReader import FileReader
from Objetos.Bicicleta import Bicicleta

class api_bicicleta:
    file_name = 'bicicleta.json'
    file = None


    #Lê o ficheiro apenas a primeira vez  retorna false se já foi lido o ficheiro
    @classmethod
    def readFile(cls):
        if cls.file is not None:
            return False
        cls.file = FileReader(os.getcwd()+"/Data/"+cls.file_name)
        return True
    #retorna uma lista com todas as bicicletas
    @classmethod
    def get_all(cls):
        cls.readFile()
        for value in cls.file.object_list:
            yield value

    #retorna uma lista com todas as bicicletas com a especifica marca não é case sensitive
    @classmethod
    def get_by_marca(cls,marca: str):
        res = []
        for value in cls.get_all():
            if value.marca.lower() == marca.lower():
                res.append(value)
        return res

    #retorna uma lista com todas as bicicletas com a especifica cor não é case sensitive
    @classmethod
    def get_by_cor(cls, cor: str):
        res = []
        for value in cls.get_all():
            if value.cor.lower() == cor.lower():
                res.append(value)
        return res
    
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
    def contains(cls, b: Bicicleta):
        for value in cls.get_all():
            if value == b:
                return value
        return None


    #replace, susbstitui na lista dado um objeto igual
    @classmethod
    def replace(cls, old: Bicicleta, new: Bicicleta):
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
    def add(cls, b: Bicicleta):
        if cls.file is None:
            cls.readFile()
        cls.file.object_list.append(b)
        cls.file.fileSave()


    #Remove uma bicicleta, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def delete(cls, b: Bicicleta):
        if cls.file is None:
            cls.readFile()
        cls.file.object_list.remove(b)
        cls.file.fileSave()

