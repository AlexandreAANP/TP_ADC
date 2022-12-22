import json
import sys
import os

sys.path.append(os.getcwd())

from Objetos.Aluguer import Aluguer, Utilizador, Bicicleta


class FileReader:
    def __init__(self, path :str, object_type :str):
        self.object_list = []
        self.__path = path
        try:
            with open(path, "r+") as f:
                if len(f.read())<2:
                    f.write(json.dumps({object_type:[]}, indent=3))
            #exception file not found
        except:
            with open(path, "w") as f:
                f.write(json.dumps({object_type:[]}, indent=3))
        finally:
            with open(path, "r") as f:
                self.data = json.loads(f.read())
                self.data_type = list(self.data.keys())[0]

        #depende do tipo
        if self.data_type == "Bicicleta":
            Bicicleta.FileReader = self
            self.readBicicleta()
            return
        if self.data_type == "Utilizador":
            Utilizador.FileReader = self
            self.readUtilizador()
            return
        if self.data_type == "Aluguer":
            Aluguer.fileReader = self
            self.readAluguer()
            

    def readUtilizador(self):
        for object_data in self.data[self.data_type]:
            object_data = list(object_data.values())
            Utilizador(
                object_data[0],
                object_data[1],
                object_data[2],
                writeFile=False
            )

    def readBicicleta(self):    
        for object_data in self.data[self.data_type]:
            object_data = list(object_data.values())
            Bicicleta(
                object_data[0],
                object_data[1],
                object_data[2],
                writeFile=False
            )

    def readAluguer(self):
        for object_data in self.data[self.data_type]:
            self.object_list.append(Aluguer(
                Bicicleta(
                    object_data['bicicleta'][0],
                    object_data['bicicleta'][1],
                    object_data['bicicleta'][2],
                    object_data['bicicleta'][3],
                    writeFile=False
                ),
                Utilizador(
                    object_data['utilizador'][0],
                    object_data['utilizador'][1],
                    object_data['utilizador'][2],
                    object_data['utilizador'][3],
                    writeFile=False
                ),
                writeFile=False
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
            #print(str(save))
            f.write(json.dumps(save, indent=3))

