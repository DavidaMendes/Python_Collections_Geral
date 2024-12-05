from classe import ContaCorrente

# Utilização de tuplas
conta_da_dani = ('Daniela', 19, 2000)
conta_do_davi = ('Davi', 15, 1000)

def deposita_tupla(conta): # Programação funcional, ão orientada a objeto
    novo_saldo = conta[2] + 100
    codigo = conta[1]
    return (codigo, novo_saldo)

conta_nova_do_davi = deposita_tupla(conta_do_davi)
print(conta_nova_do_davi) # Retorna o original imutavel, para printar a nova alteração é preciso reatribuir

# Lista de Tuplas
usuarios = [conta_do_davi, conta_da_dani]

usuarios.append(('Paulo', 33, 1500))

print(usuarios[0][0])

# Tupla de Listas
conta_do_jose = ContaCorrente(77)
conta_do_jose.deposita(900)
conta_da_yas = ContaCorrente(89)
conta_da_yas.deposita(400)

contas = (conta_da_yas, conta_do_jose)

contas[0].deposita(300)
for i in contas:
    print(i)



