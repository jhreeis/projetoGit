from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, idade, sexo, temperatura, pressao, peso,):
        super().__init__(nome, sexo, idade)
        self.__temperatura = temperatura
        self.__pressao = pressao
        self.__peso = peso
        
