class Aluger:

    def __init__(self, bicicleta, utilizador):
        self.bicicleta = bicicleta
        self.utilizador = utilizador

    def __repr__(self):
        return f'''Aluger(\n\n {self.bicicleta}, {self.utilizador} )'''
