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
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        Bicicleta.contBici = Bicicleta.contBici+1 

        # este codigo nao funciona
        #if not Bicicleta.listMarcas.__contains(self.__marca):
        #   Bicicleta.listMarcas.append(self.__marca)
            
        if numeroSerie is None:
            Bicicleta.NumeroSerie +=1
            self.__numeroSerie = Bicicleta.NumeroSerie
        else:
            self.__numeroSerie = numeroSerie

        if dono != None:
            self.dono = dono

    @classmethod
    def getBicicletas(cls):
        """
        Este metodo vai apresentar quantas bicicletas temos
        @return: retorna o numero total de bicicletas
        """
        return Bicicleta.contBici
    
    @classmethod
    def getMarcasBici(cls):
        """
        
        """    
        return Bicicleta.listMarcas

    @classmethod    
    def getLocalizacao(cls):
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
        return self.__marca

    # Função para introduzir um valor
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    # Função para retornar o valor das variaveis
    @property
    def modelo(self):
        return self.__modelo

    # Função para introduzir um valor
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    # Função para retornar o valor das variaveis
    @property
    def cor(self):
        return self.__cor

    # Função para introduzir um valor
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @classmethod
    def get_random_bike(cls):
        with open('marcas.txt') as f:
            marcas = f.read().splitlines()
        with open('modelos.txt') as f:
            modelos = f.read().splitlines()
        with open('cores.txt') as f:
            cores = f.read().splitlines()
        return Bicicleta(random.choice(marcas), random.choice(modelos), random.choice(cores))

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