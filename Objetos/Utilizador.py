class Utilizador :


    def _init_ (self,nome,idade):
        self.nome = nome
        self.idade = idade

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
    






