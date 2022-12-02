from Aluger import Aluger


class Bicicleta():

    def __init__(self, marca, modelo, cor, numeroSerie=None, dono=None):
        self.numeroSerie = numeroSerie
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

        if dono != None:
            self.dono = dono

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


if __name__ == "__main__":
    b1 = Aluger(Bicicleta("trek", "super", "amarelo", None,))
    print(b1)
