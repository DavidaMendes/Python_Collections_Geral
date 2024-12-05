from operator import attrgetter # Bibliotecas boas para ler depois
from functools import total_ordering

@total_ordering # FAz suportar o maior/menor e igual que
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo  == outro._saldo
            
    def __lt__(self,outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo
    
    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return f'[>>>> Codigo {self._codigo} Saldo {self._saldo} <<<<]'
    
conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

conta_do_gui = ContaSalario(1700)
conta_do_gui.deposita(500)

conta_da_dani = ContaSalario(3)
conta_da_dani.deposita(500)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_gui, conta_da_dani, conta_do_paulo]

# def extrai_saldo(conta):    ----Forma Errada
#     return conta._saldo

# contas.sort(key=extrai_saldo)

print(conta_do_gui < conta_da_dani)
print(conta2 == conta1)
print(isinstance(ContaSalario(99), ContaSalario)) # Identificar se um objeto é instancia de um tipo pai ou mae

# Key attrgetter também funciona

for i in sorted(contas):
    print(i)
