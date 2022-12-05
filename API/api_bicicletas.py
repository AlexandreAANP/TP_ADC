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

    #retorna o valor se o conter na lista
    @classmethod
    def contains(cls, b: Bicicleta):
        for value in cls.get_all():
            if value == b:
                return value
        return None


for i in api_bicicleta.get_by_marca("Queijolop"):
    print(i)
#print(api_bicicleta.get_all())