import re

from ply import lex


#Exercício1
def trocaData(texto):
    data = re.compile(r"0[1-9]|[12] [0-9]|3[01]\/")



#Exercíco2
def validaNome(lista):
    resultado={}
    nome = re.compile(r"([/w.-]+)\.([a-zA-Z]+)")
    for n in lista:
        match = re.match(nome, n)
        if match:
            extensao = match.group()

#Exercicio5 - Matrículas

def matricula_valida(matricula):

    padrao = re.compile(
        #r'^([A-Z]{2}-[A-Z]{2}-\d{2}|\d{2}-[A-Z]{2}-[A-Z]{2}|[A-Z]{2} \d{2} \d{2}|\d{2} [A-Z]{2} \d{2}|\d{2} [A-Z]{2} [A-Z]{2}|[A-Z]{2}-\d{2}-[A-Z]{2})$')
        #r'^([A-Z]{2}-[A-Z]{2}-\d{2}|[A-Z]{2}-\d{2}-\d{2}|[A-Z]{2} [A-Z]{2} \d{2}|[A-Z]{2} \d{2} \d{2})$')
        #r'^\W{2}([ |-])\W{2}\1\d{2}|\W{2}\1\d{2}\1\W{2}|\d{2}\1\W{2}\1\W{2}$')
        r'^([A-Z0-9]{2}([ |-])[A-Z]{2}\2\d{2}|[A-Z]{2}\2\d{2}\2[A-Z0-9]{2}|\d{2}\2[A-Z0-9]{2}\2[A-Z]{2})$')



    if padrao.match(matricula):
        separadores = re.findall(r'[^A-Z0-9]+', matricula)
        if len(set(separadores)) == 1:
            return True
    return False

matriculas = [
    "AA-13 15",  # inválida
    "AA-AA-AA",  # inválida
    "LR-RB-32",  # válida
    "1234LX",    # inválida
    "PL 22 23",  # válida
    "22 23 PL",  # válida
    "ZZ-99-ZZ",  # válida
    "13-AA-15",  # válida
    "54-tb-34",  # inválida
    "12 34 56",  # inválida
    "42-HA BQ"   # válida, mas inválida com o requisito extra
]

for matricula in matriculas:
    if matricula_valida(matricula):
        print(f'A matrícula "{matricula}" é válida.')
    else:
        print(f'A matrícula "{matricula}" é inválida.')

#Exercicio 6 - Mat Libs

# def preencher_mad_libs(texto):
#     palavras_substituir = ["ESTAÇÃO DO ANO", "NOME DE PESSOA", "EXPRESSÃO DE PARENTESCO MASCULINA",
#                            "NOME DE LOCAL FEMININO", "OBJETO MASCULINO", "ADJETIVO MASCULINO",
#                            "VERBO INFINITIVO", "NOME DE PESSOA FAMOSA", "NOME DE LOCAL MASCULINO",
#                            "NOME PLURAL MASCULINO"]
#
#     palavras_preenchidas = {}
#
#     for palavra in palavras_substituir:
#         palavras_preenchidas[palavra] = input(f"Digite uma palavra para '{palavra}': ")
#
#     texto_preenchido = texto
#
#     for palavra, valor in palavras_preenchidas.items():
#         texto_preenchido = texto_preenchido.replace(f"[{palavra}]", valor)
#
#     print("\nTexto completo:\n")
#     print(texto_preenchido)
#
# if __name__ == "__main__":
#     texto_mad_libs = """Num lindo dia de [ESTAÇÃO DO ANO], [NOME DE PESSOA] foi passear com o seu [EXPRESSÃO DE PARENTESCO MASCULINA].
#     Quando chegaram à [NOME DE LOCAL FEMININO], encontraram um [OBJETO MASCULINO] muito [ADJETIVO MASCULINO].
#     Ficaram muito confusos, pois não conseguiam identificar a função daquilo.
#     Seria para [VERBO INFINITIVO]? Tentaram perguntar a [NOME DE PESSOA FAMOSA], que também não sabia.
#     Desanimados, pegaram no objeto e deixaram-no no [NOME DE LOCAL MASCULINO] mais próximo.
#     Talvez os [NOME PLURAL MASCULINO] de lá conseguissem encontrar alguma utilidade para aquilo."""
#
#     preencher_mad_libs(texto_mad_libs)
#
#
#
# def replace(match):
#     return input(f"Por Favor, indique um/uma {match.group(1)}: ")

#res = re.sub([],replace,res)

# # List of token names
# tokens = [
#     'AT', 'LBRACE', 'RBRACE', 'COMMA', 'EQUALS',
#     'IDENTIFIER', 'TEXT', 'NUMBER'
# ]
#
# # Regular expression rules for simple tokens
# t_AT = r'@'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
# t_COMMA = r','
# t_EQUALS = r'='
#
# def t_IDENTIFIER(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     return t
#
# def t_TEXT(t):
#     r'\"[^\"]*\"'
#     return t
#
# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t
#
# # Ignored characters (spaces and tabs)
# t_ignore = ' \t'
#
# # Error handling rule
# def t_error(t):
#     print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
#     t.lexer.skip(1)
#
# # Build the lexer
# lexer = lex.lex()
#
# # Example LaTeX bibliographic entry
# latex_input = """
# @techreport{Camila,
#   author ={{projecto Camila}},
#   editor ={L.S. Barbosa and J.J. Almeida and J.N. Oliveira and Luís Neves},
#   title = "\\textsc{Camila} - A Platform for Software Mathematical Development",
#   url="http://camila.di.uminho.pt",
#   type="(Páginas do projecto)",
#   institution = umdi,
#   year=1998,
#   keyword = "FS",
# }
# """
#
# # Feed the lexer with the input
# lexer.input(latex_input)
#
# # Tokenize and print the tokens
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
#

#exercício 3:

# Lista de nomes de tokens
tokens = [
    'LBRACE', 'RBRACE', 'LSQUARE', 'RSQUARE', 'COMMA', 'COLON',
    'STRING', 'NUMBER', 'BOOL', 'NULL', 'IDENTIFIER'
]

# Regras de expressão regular para tokens simples
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_COMMA = r','
t_COLON = r':'

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Remover as aspas
    return t

def t_NUMBER(t):
    r'-?\d+(\.\d+)?([eE][-+]?\d+)?'
    if '.' in t.value or 'e' in t.value or 'E' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_BOOL(t):
    r'true|false'
    t.value = (t.value == 'true')
    return t

def t_NULL(t):
    r'null'
    t.value = None
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Ignorar espaços em branco e quebras de linha
t_ignore = ' \t\n'

# Função de tratamento de erro
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' na linha {t.lineno}, posição {t.lexpos}")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Exemplo de uso
json_input = """
{
  "name": "John Doe",
  "age": 21,
  "gender": "male",
  "height": 1.68,
  "address": {
    "street": "123 Main Street",
    "city": "New York",
    "country": "USA",
    "zip": "10001"
  },
  "married": false,
  "hobbies": [
    {
      "name": "reading",
      "books": [
        {
          "title": "Heartstopper: Volume 1",
          "author": "Alice Oseman",
          "genres": ["Graphic Novels", "Romance", "Queer"]
        },
        {
          "title": "1984",
          "author": "George Orwell",
          "genres": ["Science Fiction", "Dystopia", "Politics"]
        }
      ]
    },
    {
      "name": "gaming",
      "games": [
        {
          "title": "Portal 2",
          "platform": ["PC", "PlayStation 3", "Xbox 360"]
        },
        {
          "title": "Synth Riders",
          "platform": ["PSVR", "PSVR2", "PCVR", "Oculus Quest"]
        }
      ]
    }
  ]
}
"""

# Feed do lexer com a entrada
lexer.input(json_input)

# Loop para imprimir os tokens
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


