from abc import ABC, abstractmethod
import PySimpleGui as sg


class AbstractTelaItens(ABC):
    @abstractmethod
    def __init__(self):
        self.__window = None
        self.init_components()

    @abstractmethod
    def init_components(self):
        pass

    @abstractmethod
    def open(self):
        button, values = self.__window.Read()
        return button, values

    @abstractmethod
    def close(self):
        self.__window.Close()

    @abstractmethod
    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
