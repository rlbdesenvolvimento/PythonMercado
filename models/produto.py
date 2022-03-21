from utils.helper import formata_float_str_moeda


class Produto:
    contador: int = 1

    def __init__(self, nome: str, preco: float):
        self.__codigo: int = self.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    def __str__(self) -> str:
        return f'Código: {self.codigo}\n Nome: {self.nome} \n Preço: {formata_float_str_moeda(self.preco)}'
