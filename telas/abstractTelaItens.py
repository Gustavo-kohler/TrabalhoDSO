from abc import ABC, abstractmethod


class AbstractTelaItens(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def imprime_operacoes(self):
        pass

    @abstractmethod
    def escolhe_operacao(self):
        pass

    @abstractmethod
    def mostra_itens(self):
        pass

    @abstractmethod
    def escolhe_codigo(self):
        pass

    @abstractmethod
    def escolhe_nome(self):
        pass
