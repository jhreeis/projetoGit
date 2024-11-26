from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, sexo, idade):
        self.__nome = nome
        self.__sexo = sexo
        self.__idade = idade

    def getNome(self):
        return self.__nome
    def getSexo(self):
        return self.__sexo
    def getIdade(self):
        return self.__idade
    
    def setNome(self, nome):
        self.__nome = nome
    def setIdade(self, sexo):
        self.__idade = sexo
    def setIdade(self, idade):
        self.__idade = idade

    def mostrar(self):
        pass