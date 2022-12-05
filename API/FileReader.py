import json
import sys
import os

sys.path.append(os.getcwd())
#from Objetos.Bicicleta import Bicicleta
#from Objetos.Utilizador import Utilizador
from Objetos.Aluguer import Aluguer, Utilizador, Bicicleta


class FileReader:
    def __init__(self, path :str):
        self.object_list = []
        self.__path = path
        with open(path) as f:
            self.data = json.loads(f.read())
        self.data_type = list(self.data.keys())[0]

        #depende do tipo
        if self.data_type == "Bicicleta":
            self.readBicicleta()
            return
        if self.data_type == "Utilizador":
            self.readUtilizador()
            

    def readUtilizador(self):
        for object_data in self.data[self.data_type]:
            object_data = list(object_data.values())
            self.object_list.append(Utilizador(
                object_data[0],
                object_data[1],
                object_data[2]
            ))

    def readBicicleta(self):    
        for object_data in self.data[self.data_type]:
            object_data = list(object_data.values())
            self.object_list.append(Bicicleta(
                object_data[0],
                object_data[1],
                object_data[2]
            ))

    def readAluguer(self):
        for object_data in self.data[self.data_type]:
            object_data = list(object_data.values())
            self.object_list.append(Aluguer(

            ))


    #consoante a lista de objetos em object_data retorna uma lista com jsons atraves do metodo get_json_object()
    def list_json_object(self):
        res = []
        for object in self.object_list:
            res.append(object.get_json_object())
        return res

    #salva a lista de objetos em formato de json no ficheiro 
    def fileSave(self):
        save = { 
            self.data_type : self.list_json_object() 
        }
        with open (self.__path, "w") as f:
            print(str(save))
            f.write(json.dumps(save, indent=3))

