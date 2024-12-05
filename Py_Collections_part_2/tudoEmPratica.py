from collections import Counter
txt1 = '''
Em um mundo cada vez mais dinâmico e exigente, a gestão do tempo se tornou um componente essencial para o sucesso pessoal e profissional.

Com a constante pressão para cumprir prazos apertados e lidar com uma infinidade de responsabilidades, pessoas e organizações estão cada vez mais conscientes da necessidade de dominar essa habilidade fundamental.

No ambiente empresarial moderno, em que a competição é acirrada e as demandas são constantes, a capacidade de gerenciar eficazmente o tempo pode diferenciar pessoas bem-sucedidas de pessoas menos bem-sucedidas.

Além disso, a gestão do tempo transcende a mera organização de tarefas: ela envolve uma compreensão profunda de prioridades, objetivos e a habilidade de antecipar e adaptar-se a imprevistos.
'''

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia_de_letras(txt1)