class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self,valor):
        self.saldo += valor

    def __str__(self):
        return f'[>>>> Codigo {self.codigo} Saldo {self.saldo} <<<<]'
    
    
    
contas = []

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
contas.append(conta_do_gui)

conta_da_dani = ContaCorrente(19)
conta_da_dani.deposita(1000)
contas.append(conta_da_dani)

def depositar_em_todas_as_contas(contas):
    for conta in contas:
        conta.deposita(100)
depositar_em_todas_as_contas(contas)

# for i in contas:
#     print(i)


