class Pagamento_cu:
    def __init__(self, lista) -> None:
        self.paymentId = lista[0]
        self.valor = float(lista[1])
        self.status = lista[2]
        self.dataCriacao = lista[3]
        self.timeInit = float(lista[4])
        self.idUsuario = lista[5]