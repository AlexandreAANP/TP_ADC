#from Aluger import Aluger


class Bicicleta():

    def __init__(self, marca, modelo, cor, numeroSerie=None, dono=None):
        self.numeroSerie = numeroSerie
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

        if dono != None:
            self.dono = dono

    #TO DO
    #User Story 0001
    #Criar um contador de bicicletas


    #TO DO
    #User Story 0005
    #Criar um metodo para saber as marcas de bicicletas temos, 
    #ou seja no metodo init adicionar a marca da bicicleta a uma lista, não recebendo valores repetidos
    #PS: copnvém que a lista que vcs guardam seja da class/estática e method tbm
    # podem ver como na class Aluguer com o adicionei o ID 

    #TO DO 
    #User Story 0007
    #Criar um metodo que retorna a localização da bicicleta
    #não precisa ser nada sério pode ser algo ficticio, imaginem um objeto localização




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



