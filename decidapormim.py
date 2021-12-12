import random

class decidaporMim():
    def __init__(self):
        self.listaresp=[
        'Tem certeza que irá sair?', 
        'Hoje o dia está chuvoso', 
        'Ela não quer te ver'
        ]

    def iniciar(self):
        resposta=input("Qual sua pergunta? ")
        print(random.choice(self.listaresp))

decida=decidaporMim()
decida.iniciar()