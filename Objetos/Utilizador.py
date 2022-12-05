class Utilizador:

    ID = 1001

    def __init__ (self,nome,idade,morada, id=None):
        self.__nome = nome
        self.__idade = idade
        self.__morada = morada

        if id is None:
            Utilizador.ID +=1
            self.id = Utilizador.ID 
        else:
            self.id = id

    # Função para introduzir a idade do Utilizador
    @property
    def idade(self):
        return self.idade
    @idade.setter
    def idade(self, idade):
        self.idade = idade

    # Função para introduzir o nome do Utilizador
    @property
    def nome(self):
        return self.nome
    @nome.setter
    def nome(self, nome):
        self.nome = nome

    # Função para introduzir a morada do Utilizador
    @property
    def morada(self):
        return self.morada
    @nome.setter
    def morada(self, morada):
        self.morada = morada
    
    def __repr__(self):
        return f'''Utilizador(\n\n Nome-> {self.__nome} \n Idade-> {self.__idade} \n Morada-> {self.__morada}'''

    def get_json_object(self):
        return {
            "nome" : self.__nome,
            "idade" : self.__idade,
            "morada" : self.__morada,
            "id" : self.id
        }



