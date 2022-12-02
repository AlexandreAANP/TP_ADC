class Utilizador :


    def _init_ (self,nome,idade,morada):
        self.nome = nome
        self.idade = idade
        self.morada = morada
        

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
    






