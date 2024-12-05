idades = [13,14,70,90]

def correcao_de_erro_de_lista(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)
    # Utilização de None para à mutabilidade da lista

def list_idades():
    for i in idades:
        print(i)
    
def question_in_number(number):
    return number in idades

def idades_mais_um_ano():
    idades_mais_1 = [(i+1) for i in idades]
    print(idades_mais_1)

def seletor_de_idades():
    print([(i) for i in idades if i > 21])

def main():
    idades.insert(0, 20)
    idades.extend([28,29])

    if question_in_number(13) == True:
        idades.remove(13)
        print(idades)

    question_in_number(16)

    correcao_de_erro_de_lista()
    correcao_de_erro_de_lista()

    

if __name__ == '__main__':
  main()
