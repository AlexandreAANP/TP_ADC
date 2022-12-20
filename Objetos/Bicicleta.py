import sys
import os
import random

class Bicicleta():
    
    #Falta fazer
    """
        Criamos 2 variaveis, uma NumeroSerie que vai começar no 1000 e outra contBici que vai começar no 0
        Também temos 2 listas, listMarcas onde mais à frente irá ser guardado todas as marcas das Bicicletas na lista listMarcas
        e localização onde posterioriamente  
    """
    NumeroSerie = 1000
    contBici = 0
    listMarcas = []
    localizacao = [ 'Boliqueime','Lisboa', 'Faro', 'Alvor', 'Lagoa', 'Lagos' ]

    def __init__(self, marca, modelo, cor, numeroSerie=None, dono=None):
        """
            No construtor, declaramos os atributos que achamos mais importantes
            @param marca: recebe uma String de marca
            @param modelo: recebe uma String de modelo
            @param cor: recebe uma String de cor
            @param numeroSerie: não recebe nada 
            @param dono: não recebe nada
            Seguidamente cada vez que um objeto bicicleta é criado vai ser adicionado mais 1 à variavel 
            contBici onde mais a baixo a través do metodo getBicicletas() irá ser apresentado o total de bicicletas.
        """
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        Bicicleta.contBici = Bicicleta.contBici+1 

        # CORRIGIR 
        # este codigo nao funciona
        #if not Bicicleta.listMarcas.__contains(self.__marca):
        #   Bicicleta.listMarcas.append(self.__marca)

        """
            Se não for introduzido nenhum numero de serie, vai ser adicionado +1 ao numero de serie que estava anteriormente.
            Se for introduzido um numero de serie, esse mesmo vai ser guardado na variavel numeroSerie
        """
        if numeroSerie is None:
            Bicicleta.NumeroSerie +=1
            self.__numeroSerie = Bicicleta.NumeroSerie
        else:
            self.__numeroSerie = numeroSerie
        
        """
            Se o atributo dono for diferente de None vai ser guardado a String introduzida 
        """
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
            Este metodo vai apresentar todas as marcas de bicicletas que temos
            @return: retorna todas as marcas de bicicletas 
        """    
        return Bicicleta.listMarcas

    @classmethod    
    def getLocalizacao(cls):
        """
            Este metodo vai apresentar a localização da bicicleta
            @return: retorna uma localização aleatoriamente da lista
        """
        return Bicicleta.localizacao[random.int(0,Bicicleta.localizacao.__len__()-1)]


    """
        Função para ir buscar o numero de serie da bicicleta
    """
    @property
    def numeroSerie(self):
        return self.__numeroSerie


    """
        Metodo para mostrar a marca de uma bicicleta
        @return: Marca de uma bicicleta
    """
    @property
    def marca(self):
        return self.__marca

    """ 
        Função para introduzir uma marca    
    """
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    
    """ 
        Função para retornar um modelo
        @return: Modelo de uma Bicicleta  
    """
    @property
    def modelo(self):
        return self.__modelo

    """ 
        Função para introduzir um modelo    
    """
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    """ 
        Função para retornar a cor
        @return: Cor de uma bicicleta   
    """
    @property
    def cor(self):
        return self.__cor

    """ 
        Função para introduzir uma cor    
    """
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    
    """
        Função que gera automaticamente os objetos do tipo bicicleta
        Primeiro vai ler o ficheiro txt e depois vai buscar uma linha do ficheiro
        @return: Uma instacia de bicicleta com valores random
    """
    @classmethod
    def get_random_bike(cls):
        with open('marcas.txt') as f:
            marcas = f.read().splitlines()
        with open('modelos.txt') as f:
            modelos = f.read().splitlines()
        with open('cores.txt') as f:
            cores = f.read().splitlines()
        return Bicicleta(random.choice(marcas), random.choice(modelos), random.choice(cores))


    """
        Metodo que vai apresentar a marca, modelo, cor e o numero de serie da bicicleta
        @return: Retorna uma instancia da bicicleta
    """
    def __repr__(self):
        return f'''Bicicleta(\n\n Marca-> {self.marca} \n Modelo-> {self.modelo} \n Cor-> {self.cor} \n Numero de Serie-> 
        {self.numeroSerie}\n)'''


    """
        Metodo para retornar o objeto da mesma maneira que é guardado no json
        @return: Retorna o objeto
    """
    def get_json_object(self):
        return {
            "marca" : self.marca,
            "modelo" : self.modelo,
            "cor" : self.cor,
            "numero serie" : self.numeroSerie
        }