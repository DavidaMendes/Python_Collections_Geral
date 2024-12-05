from collections import defaultdict, Counter

class Conta:
    def __init__(self):
        print('Criando uma conta')

contas = defaultdict(Conta)
contas[15]

txt = 'Davi gosta de Davi para Davi'
txt = txt.lower()
aparicoes = Counter(txt.split())
print(aparicoes)

