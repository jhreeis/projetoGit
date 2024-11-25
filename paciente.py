from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, altura, peso, idade, sexo, temperatura):
        super().__init__(nome, altura, peso, idade)