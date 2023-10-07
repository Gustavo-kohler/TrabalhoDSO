from abc import ABC, abstractmethod


class AbstractControladorItens(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def lista_operacoes(self):
        pass

    @abstractmethod
    def adiciona_item(self):
        pass

    @abstractmethod
    def remove_item(self):
        pass

    @abstractmethod
    def edita_item(self):
        pass

    @abstractmethod
    def lista_item(self):
        pass
