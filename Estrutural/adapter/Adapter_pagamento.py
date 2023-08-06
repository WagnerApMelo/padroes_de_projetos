# Classe de Pagamento com cartão
class PagamentoCartao:
    def realizar_pagamento_cartao(self, valor):
        print(f"Pagamento de R${valor:.2f} realizado com cartão de crédito.")

# Classe de Pagamento com boleto
class PagamentoBoleto:
    def realizar_pagamento_boleto(self, valor):
        print(f"Pagamento de R${valor:.2f} realizado com boleto bancário.")

# Classe Adapter que permite usar ambas as classes de pagamento com uma interface unificada
class PagamentoAdapter:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento

    def realizar_pagamento(self, valor):
        if isinstance(self.metodo_pagamento, PagamentoCartao):
            self.metodo_pagamento.realizar_pagamento_cartao(valor)
        elif isinstance(self.metodo_pagamento, PagamentoBoleto):
            self.metodo_pagamento.realizar_pagamento_boleto(valor)
        else:
            print("Método de pagamento não suportado.")

# Exemplo de uso do Adapter
if __name__ == "__main__":
    # Usando a classe PagamentoCartao diretamente
    pagamento_cartao = PagamentoCartao()
    pagamento_cartao.realizar_pagamento_cartao(100.0)

    # Usando a classe PagamentoBoleto diretamente
    pagamento_boleto = PagamentoBoleto()
    pagamento_boleto.realizar_pagamento_boleto(50.0)

    # Usando a classe PagamentoAdapter com ambas as classes de pagamento
    pagamento_adapter_cartao = PagamentoAdapter(PagamentoCartao())
    pagamento_adapter_cartao.realizar_pagamento(75.0)

    pagamento_adapter_boleto = PagamentoAdapter(PagamentoBoleto())
    pagamento_adapter_boleto.realizar_pagamento(30.0)
