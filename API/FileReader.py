
import json
import sys
import os

sys.path.append(os.getcwd())
from Objetos.Bicicleta import Bicicleta, Utilizador


class FileReader:
    data = None
    data_type = None
    object_list = []
    def __init__(self, path :str):
        self.data = json.loads(open(path).read())
        self.data_type = list(self.data.keys())[0]
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
