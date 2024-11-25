from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, altura, peso, idade):
        self.__nome = nome
        self.__altura = altura
        self.__peso = peso
        self.__idade = idade

    def getNome(self):
        return self.__nome
    def getNome(self):
        return self.__altura
    def getNome(self):
        return self.__peso
    def getIdade(self):
        return self.__idade
    
    def setNome(self, nome):
        self.__nome = nome
    def setAltura(self, altura):
        self.__altura = altura
    def setPeso(self, peso):
        self.__peso = peso
    def setIdade(self, idade):
        self.__idade = idade

    def mostrar(self):
        pass