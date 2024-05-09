import sys
import ply.lex as lex
import json

from dataclasses import dataclass
from typing import Final, List, Optional


@dataclass
class Produto:
    codigo: str
    nome: str
    quantidade: int
    preco: float


moedas: Final[List[float]] = [
    2.00,
    1.00,
    0.50,
    0.20,
    0.10,
    0.05,
    0.02,
    0.01
]


def calcularTroco(montante: float) -> List[int]:
    moedas_usadas = []
    for moeda in moedas:
        moedas_usadas.append(int(montante // moeda))
        montante %= moeda

    return moedas_usadas


def exibirTroco(moedas_troco: List[int]) -> None:
    for i, moeda in enumerate(moedas):
        if moedas_troco[i] > 0:
            print(f"{moedas_troco[i]} moedas de {moeda:.2f}€")


class VendingMachine:
    tokens = (
        "LISTAR",
        "TERMINAR",
        "INSERIR",
        "SELECIONAR"
    )

    states = (
        ("MODO_INSERCAO", "exclusive"),
        ("MODO_SELECAO", "exclusive")
    )

    t_ANY_ignore = " \t\n"
    t_MODO_INSERCAO_ignore = ", \t\n"

    def __init__(self):
        self.lexer: Optional[lex.Lexer] = None
        self.terminar: bool = False

        self.credito: float = 0.0
        self.produtos: List[Produto] = []

    def iniciar(self, **kwargs) -> None:
        self.lexer = lex.lex(module=self, **kwargs)
        self.carregarProdutos()

    def carregarProdutos(self) -> None:
        with open("vending_products.json", encoding="utf-8") as arquivo:
            self.produtos = [Produto(**item) for item in json.load(arquivo)]

    def t_comecar_INSERIR(self, t):
        r"INSERIR"
        t.lexer.begin("MODO_INSERCAO")

    def t_MODO_INSERCAO_INSERIR(self, t):
        r"2e|1e|50c|20c|10c|5c|2c|1c"
        if t.value[-1] == "c":
            t.value = int(t.value[:-1]) / 100
        elif t.value[-1] == "e":
            t.value = int(t.value[:-1])

        self.credito += t.value
        return t

    def t_MODO_INSERCAO_TERMINAR(self, t):
        r"TERMINAR"
        print("Crédito atual: {:.2f}".format(self.credito))
        t.lexer.begin("INITIAL")

    def t_comecar_SELECIONAR(self, t):
        r"SELECIONAR"
        t.lexer.begin("MODO_SELECAO")

    def t_MODO_SELECAO_SELECIONAR(self, t):
        r"[0-9]{2}"
        t.lexer.begin("INITIAL")

        for produto in self.produtos:
            if produto.codigo == t.value:
                if produto.quantidade <= 0:
                    print("Produto esgotado")
                    return t

                if self.credito < produto.preco:
                    print("Crédito insuficiente")
                    return t

                self.credito -= produto.preco
                produto.quantidade -= 1
                print(f"Produto adquirido: {produto.nome}")
                print(f"Crédito restante: {self.credito:.2f}€")
                return t

        print("Produto não encontrado")
        return t

    def t_ANY_error(self, t):
        print(f"Caractere ilegal '{t.value[0]}'")
        t.lexer.skip(1)

    def t_LISTAR(self, t):
        r"LISTAR"
        for produto in self.produtos:
            print(f"{produto.codigo} - {produto.nome} - {produto.preco}€")

        return t

    def t_TERMINAR(self, t):
        r"TERMINAR"
        self.terminar = True

        troco = calcularTroco(self.credito)
        exibirTroco(troco)

        print("Obrigado por utilizar nossa máquina de vendas!")


def executar() -> None:
    maquina = VendingMachine()
    maquina.iniciar()

    while not maquina.terminar:
        comando = input(">>> ")
        maquina.lexer.input(comando)

        while True:
            token = maquina.lexer.token()
            if not token:
                break


if __name__ == "__main__":
    executar()
