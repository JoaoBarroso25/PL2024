import sys
import ply.lex as lex

# Keywords do SQL armazenadas para identificação
keywords = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
    'like': 'LIKE',
    'inner': 'INNER',
    'outer': 'OUTER',
}

# Lista de tokens reconhecidos pelo lexer
tokens = [
             'IDENTIFIER',
             'KEYWORD',
             'SEPARATOR',
             'TERMINATOR',
             'NUMBER_LITERAL',
             'OP_PLUS',
             'OP_MINUS',
             'OP_MULTIPLY',
             'OP_DIVIDE',
             'OP_GE',
             'OP_LE',
             'OP_GT',
             'OP_LT',
         ] + list(keywords.values())

# Definição de operadores simples
t_OP_PLUS = r'\+'
t_OP_MINUS = r'\-'
t_OP_MULTIPLY = r'\*'
t_OP_DIVIDE = r'/'
t_OP_GE = r'>='
t_OP_LE = r'<='
t_OP_GT = r'>'
t_OP_LT = r'<'


def t_KEYWORD(t):
    r'\b[a-zA-Z]+\b'
    t.value = t.value.lower()
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t


def t_NUMBER_LITERAL(t):
    r'\d+[.]?\d*'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t,;'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()


def process_input(stdin):
    lexer = lex.lex()

    for line in stdin:
        lexer.input(line)
        while True:
            token = lexer.token()
            if not token:
                break
            print(token)


if __name__ == "__main__":
    process_input(sys.stdin)
