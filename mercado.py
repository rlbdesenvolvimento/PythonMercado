from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main():
    menu()


def menu():
    print('##############################')
    print('######## Bem vindo(a) ########')
    print('######## Python Shop  ########')
    print('##############################')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadatrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos(True)
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


def cadastrar_produto():
    print('Cadastro de Produto')
    print('###################')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'Produto {produto.nome} cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos(volta_menu: bool):
    if len(produtos) == 0:
        print('Nenhum produto cadastrado!')
    else:
        print('Listagem de produtos')
        print('####################')
        for produto in produtos:
            print(produto)
            print('------------')
            sleep(1)

    sleep(2)
    if volta_menu:
        menu()


def comprar_produto():
    print('Compar produto')
    print('##############')

    listar_produtos(False)

    codigo: int = int(input('Digite o código do produto: '))
    quantidade: int = int(input('Digite a quantidade: '))

    produto: Produto = pega_produto_por_codigo(codigo)

    if produto:
        item_no_carrinho: bool = False
        for item in carrinho:
            q: int = item.get(produto)
            if q:
                item[produto] = q + quantidade
                item_no_carrinho = True

        if not item_no_carrinho:
            carrinho.append({produto: quantidade})

        print(f'Produto {produto.nome} adicionado ao carrinho')

    sleep(2)
    menu()


def visualizar_carrinho():
    if len(carrinho) == 0:
        print('Nenhum produto adicionado no carrinho!')
    else:
        imprime_carrinho()

    sleep(1)
    menu()


def imprime_carrinho():
    valor_total: float = 0

    print('Produtos no Carrinho')
    for item in carrinho:
        for dados in item.items():
            valor_item: int = dados[1] * dados[0].preco
            print(dados[0])
            print(f'    {dados[1]} x {formata_float_str_moeda(dados[0].preco)} '
                  f'= {formata_float_str_moeda(valor_item)} ')

            valor_total += valor_item

    print(f'\n    Valor total: {formata_float_str_moeda(valor_total)}')


def fechar_pedido():
    if len(carrinho) == 0:
        print('Nenhum produto adicionado no carrinho!')
    else:
        imprime_carrinho()
        carrinho.clear()

    sleep(1)
    menu()


def pega_produto_por_codigo(cogido: int) -> Produto:
    for produto in produtos:
        if produto.codigo == cogido:
            return produto

    print('Nenhum produto encontrado!')


if __name__ == '__main__':
    main()
