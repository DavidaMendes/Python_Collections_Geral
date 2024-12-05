from collections import defaultdict

txt = 'Davi gosta de Davi para Davi'
txt = txt.lower()
aparicoes = defaultdict(int)

for i in txt.split():
    aparicoes[i] += 1
print(aparicoes)

dic = {
    'nomeDavi' : 3,
    'para' : 0
}

print(dic.get('oi', 0)) # Retorna se tem ou não tem a chaves -- del --> tira uma chave
print('--------')
for i in dic.values():
    print(i)
for i, v in dic.items():
    print(f'{i} = {v}')

