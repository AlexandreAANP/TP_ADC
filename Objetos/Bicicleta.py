import sys
import os
import random

class Bicicleta():
    #Id Bicicleta
    NumeroSerie = 1000
    contBici = 0
    listMarcas = []
    localizacao = [ 'Boliqueime','Lisboa', 'Faro', 'Alvor', 'Lagoa', 'Lagos' ]

    def __init__(self, marca, modelo, cor, numeroSerie=None, dono=None):
        """
        
        """
        self.marca = marca
        self.modelo = modelo
        self.cor = cor 
        Bicicleta.contBici = Bicicleta.contBici+1 
        
        if(not Bicicleta.listMarcas.__contains(marca)):
           Bicicleta.listMarcas.append(marca)
            
        if numeroSerie is None:
            Bicicleta.NumeroSerie +=1
            self.__numeroSerie = Bicicleta.NumeroSerie
        else:
            self.__numeroSerie = numeroSerie

        if dono != None:
            self.dono = dono

    @classmethod
    def getBicicletas():
        """
        Este metodo vai apresentar quantas bicicletas temos
        @return: retorna o numero total de bicicletas
        """
        return Bicicleta.contBici
    
    @classmethod
    def getMarcasBici():
        """
        
        """    
        return Bicicleta.listMarcas

    @classmethod    
    def getLocalizacao():
        """
        
        """
        return Bicicleta.localizacao[random.int(0,Bicicleta.localizacao.__len__()-1)]


    # Função para buscar o id do Utilizador
    @property
    def numeroSerie(self):
        return self.__numeroSerie

    # Função para retornar o valor das variaveis
    @property
    def marca(self):
        return self.marca

    # Função para introduzir um valor
    def marca(self, marca):
        self.marca = marca

    # Função para retornar o valor das variaveis
    @property
    def modelo(self):
        return self.modelo

    # Função para introduzir um valor
    def modelo(self, modelo):
        self.modelo = modelo

    # Função para retornar o valor das variaveis
    @property
    def cor(self):
        return self.cor

    # Função para introduzir um valor
    def cor(self, cor):
        self.cor = cor

    def __repr__(self):
        return f'''Bicicleta(\n\n Marca-> {self.marca} \n Modelo-> {self.modelo} \n Cor-> {self.cor} \n Numero de Serie-> 
        {self.numeroSerie}\n)'''

    #metodo para retorna o objecto da mesma maneira que vai ser guardado no json
    def get_json_object(self):
        return {
            "marca" : self.marca,
            "modelo" : self.modelo,
            "cor" : self.cor,
            "numero serie" : self.numeroSerie
        }


