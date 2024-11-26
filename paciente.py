from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, idade, sexo, temperatura, pressao, peso):
        super().__init__(nome, sexo, idade)
        self.__temperatura = temperatura
        self.__pressao = pressao
        self.__peso = peso

    def getTemperatura(self):
        return self.__temperatura
    def getPressao(self):
        return self.__pressao
    def getPeso(self):
        return self.__peso
    
    def setTemperatura(self, temperatura):
        self.__temperatura = temperatura
    def setTemperatura(self, pressao):
        self.__pressao = pressao
    def setPeso(self, peso):
        self.__peso = peso