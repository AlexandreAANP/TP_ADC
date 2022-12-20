import random


class Utilizador:

    ID = 1000

    def __init__ (self,nome,idade,morada, id=None):
        self.__nome = nome
        self.__idade = idade
        self.__morada = morada

        if id is None:
            Utilizador.ID +=1
            self.__id = Utilizador.ID
        else:
            self.__id = id



    # Função para buscar o id do Utilizador
    @property
    def id(self):
        return self.__id

    # Função para introduzir a idade do Utilizador
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    # Função para introduzir o nome do Utilizador
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # Função para introduzir a morada do Utilizador
    @property
    def morada(self):
        return self.__morada
    @morada.setter
    def morada(self, morada):
        self.__morada = morada

    @classmethod
    def get_random_user(cls):
        with open('datagen/nomes.txt') as f:
            nomes = f.read().splitlines()
            idade = random.randint(16, 99)
        with open('datagen/moradas.txt') as f:
            moradas = f.read().splitlines()
        return Utilizador(random.choice(nomes), idade, random.choice(moradas))

    def __repr__(self):
        return f'''Utilizador(\n\n Nome-> {self.__nome} \n Idade-> {self.__idade} \n Morada-> {self.__morada}'''

    def get_json_object(self):
        return {
            "nome" : self.__nome,
            "idade" : self.__idade,
            "morada" : self.__morada,
            "id" : self.id
        }