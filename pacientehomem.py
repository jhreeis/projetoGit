from pessoa import Pessoa

class PacienteH(Pessoa):
    def __init__(self, nome, idade, temperatura, pressao, peso):
        super().__init__(nome, idade, )
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

    def mostrar(self):
        return (f"Homem que se chama {self.getNome()}, com {self.getIdade()} anos, pesando {self.getPeso()}Kg, com temperatura de {self.getTemperatura()}°C, e pressão {self.getPressao()}.")