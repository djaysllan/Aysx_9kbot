class PagamentoGestor:
    def __init__(self) -> None:
        if(asaas):
            self.base = Asaas()
        elif(mercadoPago):
            self.base = Mercado()
        
        self.criar_qrcode = self.base.criar_qrcode
        self.status_pagamento = self.base.status_pagamento