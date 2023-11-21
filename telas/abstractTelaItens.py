from abc import ABC, abstractmethod


class AbstractTelaItens(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def init_components(self):
        pass

    @abstractmethod
    def run_view(self, layout):
        pass
