import os
import sys

from API.FileReader import FileReader
from Objetos.Utilizador import Utilizador

class api_utilizador:
    file_name = 'utilizador.json'
    file = None


    #Lê o ficheiro apenas a primeira vez  retorna false se já foi lido o ficheiro
    @classmethod
    def readFile(cls):
        """
        Instancia um objeto da class FileReader tendo como parametros:
        - api_utilziador.file_name = 'utilizador.json'
        - Nome da class a qualquer corresponde o tipo de dado -> 'Utilizador'
        Guarda na variável de class "file"
        @return: retorna true caso é possivel ler o ficheiro com sucesso
        @rtype: boolean
        """
        if cls.file is not None:
            return False
        cls.file = FileReader(os.getcwd()+"/Data/"+cls.file_name, "Utilizador")
        return True

    #retorna uma lista com todas os utilziadores
    @classmethod
    def get_all(cls):
        """
        Este metódo vai buscar todos os dados do ficheiro e retorna uma lista de objetos do tipo Utilizador
        @return: returna interator, como fosse uma lista
        @rtype: Interator
        """
        cls.readFile()
        for value in cls.file.object_list:
            yield value

    #retorna uma lista com todas os Utilizadores com o especifico nome, não é case sensitive
    @classmethod
    def get_by_nome(cls,nome: str):
        """
        Consoante o nome irá retornar uma lista de objetos Utilizador com o respetivo nome
        A comparação de nomes não case sensitive
        @param nome: recebe um nome como string
        @type nome: str
        @return: lista de Objetos utilizador
        @rtype: list
        """
        res = []
        for value in cls.get_all():
            if value.nome.lower() == nome.lower():
                res.append(value)
        return res

    #retorna uma lista com todos os utilizadores com a especifica morada, não é case sensitive
    @classmethod
    def get_by_morada(cls, morada: str):
        """
        Consoante uma morada irá retornar uma lista de objetos Utilizador com o respetiva morada
        A comparação de nomes não case sensitive
        @param morada: recebe uma morada como string
        @type morada: str
        @return: lista de Objetos utilizador
        @rtype: list
        """
        res = []
        for value in cls.get_all():
            if value.morada.lower() == morada.lower():
                res.append(value)
        return res
    
    #retorna um utilizador consoante o id
    @classmethod
    def get_by_id(cls, id):
        """
        Consoante o id irá retornar um objeto com o respetivo id
        @param id: recebe o id do Objeto Utilizador
        @type id: int
        @return: Objeto Utilizador
        @rtype: Utilizador or None
        """
        for value in cls.get_all():
            if value.id == id:
                return value
        return None

    #retorna por index
    @classmethod
    def get_by_index(cls, index: int):
        """
        Consoante o index irá retornar um objeto com respetivo index
        @param index: recebe um index referente a lista de Utilizadores
        @type index: int
        @return: Retorna um Objeto Utilizadores
        @rtype: Utilziador or None
        """
        counter = 0
        for value in cls.get_all():
            if counter == index:
                return value
            counter +=1
        return None

    #retorna o valor se o conter na lista
    @classmethod
    def contains(cls, user:Utilizador):
        """
        Caso encontre um objeto igual ao dado como parametro retorna o devolta caso contrário retorna None
        @param user: recebe um objeto de Utilizador
        @type suer: Utilizador
        @return: retorna um Objeto de Utilizador ou None
        @rtype: Utilziador or None
        """
        for value in cls.get_all():
            if value == user:
                return value
        return None


    #replace, susbstitui na lista dado um objeto igual
    @classmethod
    def replace(cls, old: Utilizador, new: Utilizador):
        """
        Através do Parametro old compara esse valor com dentro da lista
        caso encontre substitui pelo o paramtro new e retorna True.
        Caso Contrário retorna apenas False
        @param old: recebe um objeto de Utilizador
        @type old: Utilizador
        @param new: recebe um objeto de Utilizador
        @type new: Utilizador
        @return: retorna True caso seja Substituido com sucesso. Falso caso não foi possivel 
        @rtype: bool
        """
        counter = 0
        for value in cls.get_all():
            if value == old:
                try:
                    cls.file.object_list[counter] = new
                except:
                    return False
                cls.file.fileSave()
                return True
            counter+=1
        return False

    #Adiciona um Utilizador, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def add(cls, user: Utilizador):
        """
        Adiciona um Utilizador nos dados e na lista em memória através de Objeto Utilizador
        @param user: recebe um objeto de Utilizador
        @type user: Utilizador
        @return: retorna True caso seja adicionado um Utilizador com sucesso. Falso caso exista algum erro 
        @rtype: bool
        """
        if cls.file is None:
            cls.readFile()
        cls.file.object_list.append(user)
        cls.file.fileSave()


    #Remove um Utilizador, automaticamente atualiza o ficheiro com os dados
    @classmethod
    def delete(cls, user: Utilizador):
        """
        Remove um Utilizador através do parametro que recebe, ou seja caso sejam igual e atualiza o ficheiro
        @param user: recebe um objeto de Utilizador
        @type user: Utilizador
        @return: retorna True caso seja eliminado um Utilizador com sucesso. Falso caso exista algum erro 
        @rtype: bool
        """
        if cls.file is None:
            cls.readFile()
        cls.file.object_list.remove(user)
        cls.file.fileSave()