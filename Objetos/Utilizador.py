import random


class Utilizador:
    """
        Criamos 1 variavel chamada de ID que vai começar no 1000
    """
    ID = 1000
    FileReader = None
    def __init__ (self,nome,idade,morada, id=None, writeFile=True):
        """
            No construtor, declaramos os atributos que definem o objeto

            :param nome: recebe uma String de nome
            :type str: nome
            :param idade: recebe um valor inteiro de idade
            :type int: idade
            :param morada: recebe uma String de morada
            :type str: morada
            :param id: não recebe nada
            :type int: id
        """
        self.__nome = nome
        self.__idade = idade
        self.__morada = morada

        """
            Se não for introduzido nenhum id, vai ser adicionado +1 ao id que estava anteriormente.
            Se for introduzido um id, esse mesmo vai ser guardado na variavel id
        """
        if id is None:
            Utilizador.ID +=1
            self.__id = Utilizador.ID
        else:
            self.__id = id
        if writeFile == True:
            self.FileReader.object_list.append(self)
            self.FileReader.fileSave()

    @property
    def id(self):
        """
            Função para ir buscar o id de um utilizador

            :return: id de um bicicleta
            :rtype Bicicleta:
        """
        return self.__id
    
    @property
    def idade(self):
        """    
            Metodo para apresentar a idade de um utilizador
            
            :return: Idade de um utilizador
            :rtype Utilizador: 
        """
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        """
            Função para introduzir uma idade do tipo int

            :param marca: regista um valor inteiro de idade
            :type str: marca
        """
        self.__idade = idade

    @property
    def nome(self):
        """
            Metodo para apresentar o nome de um utilizador

            :return: Nome de um utilizador
            :rtype str:
        """
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        """
            Função para introduzir um nome do tipo String

            :param marca: regista uma String de nome
            :type str: nome
        """
        self.__nome = nome

    @property
    def morada(self):
        """
            Metodo para apresentar a morada de um utilizador

            :return: Morada de um utilizador
            :rtype str: morada
        """
        return self.__morada
    
    @morada.setter
    def morada(self, morada):
        """
            Função para introduzir uma morada do tipo String

            :param marca: regista uma String de morada
            :type str: marca
        """
        self.__morada = morada

    @classmethod
    def get_random_user(cls):
        """
            Função que gera automaticamente os objetos do tipo Utilizador
            Primeiro vai ler o ficheiro txt e depois vai buscar uma linha do ficheiro

            :return: Uma instacia de Utilizador com valores random
            :rtype Utilizador:
        """
        with open('Objetos/datagen/nomes.txt') as f:
            nomes = f.read().splitlines()
            idade = random.randint(16, 99)
        with open('Objetos/datagen/moradas.txt') as f:
            moradas = f.read().splitlines()
        return Utilizador(random.choice(nomes), idade, random.choice(moradas))

    def __repr__(self):
        """
            Metodo que vai apresentar o nome, idade, morada

            :return: Retorna uma String que representa o utilizador
            :rtype str:
        """
        return f'''Utilizador(\n\n Nome-> {self.__nome} \n Idade-> {self.__idade} \n Morada-> {self.__morada}'''

    
    def get_json_object(self):
        """
            Metodo para retornar o objeto da mesma maneira que é guardado no json em formato dict
            
            :return: Retorna o objeto
            :rtype dict:
        """
        return {
            "nome" : self.__nome,
            "idade" : self.__idade,
            "morada" : self.__morada,
            "id" : self.__id
        }