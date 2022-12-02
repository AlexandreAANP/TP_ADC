class Utilizador :
    Nome = Nome
    Idade = Idade

    def _init_ (self,nome,idade):
        self.Nome = nome
        self.Idade = idade

    @property
    def idade(self):
        return self.Idade
    @idade.setter
    def idade(self, idade):
        self.Idade = idade

    @property
    def nome(self):
        return self.Nome
    @Nome.setter
    def nome(self, nome):
        self.Nome = nome
    






