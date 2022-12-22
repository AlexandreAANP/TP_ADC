import random

class Bicicleta():
    
    """
        Criamos 2 variaveis, uma NumeroSerie que vai começar no 1000 e outra contBici que vai começar no 0
        Também temos 2 listas, listMarcas onde mais à frente irá ser guardado todas as marcas das Bicicletas na lista listMarcas
        e localização onde posterioriamente uma das suas Strings irá ser usada
    """
    NumeroSerie = 1000
    contBici = 0
    listMarcas = []
    localizacao = [ 'Boliqueime','Lisboa', 'Faro', 'Alvor', 'Lagoa', 'Lagos' ]

    def __init__(self, marca, modelo, cor, numeroSerie=None):
        """
            No construtor, declaramos os atributos que definem o objeto
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

        """
           Se não existir a marca que o utilizador colocou na lista a mesma será adicionada,
           se existir essa será adicionada 
        """
        if not Bicicleta.listMarcas.__contains__(self.__marca):
           Bicicleta.listMarcas.append(self.__marca)

        """
            Se não for introduzido nenhum numero de serie, vai ser adicionado +1 ao numero de serie que estava anteriormente.
            Se for introduzido um numero de serie, esse mesmo vai ser guardado na variavel numeroSerie
        """
        if numeroSerie is None:
            Bicicleta.NumeroSerie +=1
            self.__numeroSerie = Bicicleta.NumeroSerie
        else:
            self.__numeroSerie = numeroSerie

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


    @property
    def numeroSerie(self):
        """
            Função para ir buscar o numero de serie da bicicleta
            @return: numeroSerie da uma bicicleta
        """
        return self.__numeroSerie


    @property
    def marca(self):
        """
            Metodo para mostrar a marca de uma bicicleta
            @return: Marca de uma bicicleta
        """
        return self.__marca

    @marca.setter
    def marca(self, marca):
        """ 
            Função para introduzir uma marca do tipo String
            @param marca: regista uma String de marca  
        """
        self.__marca = marca

    
    @property
    def modelo(self):
        """ 
            Metodo para mostrar um modelo de uma bicicleta
            @return: Modelo de uma Bicicleta  
        """
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        """ 
            Função para introduzir um modelo do tipo String
            @param modelo: regista uma String de marca    
        """
        self.__modelo = modelo

    @property
    def cor(self):
        """ 
            Função para mostrar uma cor de uma bicicleta
            @return: Cor de uma bicicleta   
        """
        return self.__cor

    @cor.setter
    def cor(self, cor):
        """ 
            Função para introduzir uma cor do tipo String
            @param cor: regista uma String de marca    
        """
        self.__cor = cor

    
    @classmethod
    def get_random_bike(cls):
        """
            Função que gera automaticamente os objetos do tipo bicicleta
            Primeiro vai ler o ficheiro txt e depois vai buscar uma linha do ficheiro
            @return: Uma instacia de bicicleta com valores random
        """
        with open('Objetos/datagen/marcas.txt') as f:
            marcas = f.read().splitlines()
        with open('Objetos/datagen/modelos.txt') as f:
            modelos = f.read().splitlines()
        with open('Objetos/datagen/cores.txt') as f:
            cores = f.read().splitlines()
        return Bicicleta(random.choice(marcas), random.choice(modelos), random.choice(cores))


    def __repr__(self):
        """
            Metodo que vai apresentar a marca, modelo, cor e o numero de serie da bicicleta
            @return: Retorna uma String que representa a bicicleta
        """
        return f'''Bicicleta(\n\n Marca-> {self.marca} \n Modelo-> {self.modelo} \n Cor-> {self.cor} \n Numero de Serie-> 
        {self.numeroSerie}\n)'''


    def get_json_object(self):
        """
            Metodo para retornar o objeto da mesma maneira que é guardado no json em formato dict
            @return: Retorna o objeto
        """
        return {
            "marca" : self.marca,
            "modelo" : self.modelo,
            "cor" : self.cor,
            "numero serie" : self.numeroSerie
        }