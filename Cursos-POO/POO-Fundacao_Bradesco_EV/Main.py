class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Kennedy", "99399-8428")
conta = Conta(c1.get_nome(), 6565)

conta.deposita(100)
conta.saque(50)
conta.extrato()

