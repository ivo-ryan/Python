class Conta:
    taxa = 0.50

    @staticmethod
    def retornarCodigoBanco():
        return '345'

    
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.titular = titular
        self._saldo = saldo

    
    def extrato(self):
        print(f"Saldo: R${self.__saldo}")

    
    def depositar(self, valor):
        self.__saldo += valor
    

    def sacar(self, valor ):
        self.__saldo -= valor

    
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    


conta1 = Conta('123', 'Ryan', 20000)
conta2 = Conta('598', 'Lucas', 3000)

conta1.transferir(9400, conta2)

conta1.extrato()
conta2.extrato()