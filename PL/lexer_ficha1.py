import json
import sys
import ply.lex as lex

# Define os tokens
tokens = [
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'COLON',
    'COMMA',
    'STRING',
    'NUMBER',
    'BOOLEAN',
    'NULL',
]

# Define os estados
states = (
    ('string', 'exclusive'),
    ('array', 'exclusive'),
)

# Regras de token
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_COLON = r':'
t_COMMA = r','

def t_STRING(t):
    r'"'
    t.lexer.begin('string')

def t_string_STRING(t):
    r'[^"]+'
    t.value = t.value
    t.lexer.begin('INITIAL')
    t.type = 'STRING'
    return t

def t_string_error(t):
    t.lexer.skip(1)

def t_array_LEFT_BRACKET(t):
    r'\['
    t.lexer.begin('array')
    return t

def t_array_RIGHT_BRACKET(t):
    r'\]'
    t.lexer.begin('INITIAL')
    return t

def t_array_COMMA(t):
    r','
    return t

t_array_ignore = ' \t\n'
t_string_ignore = ' \t\n'

def t_array_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

def t_NUMBER(t):
    r'-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][-+]?[0-9]+)?'
    return t

def t_BOOLEAN(t):
    r'true|false'
    return t

def t_NULL(t):
    r'null'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def tokenize(data):
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value))
    return tokens

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        json_data = file.read()
    return json_data

def main():
    file_path = "teste.json"
    json_data = read_json_file(file_path)
    tokens = tokenize(json_data)
    print(tokens)

if __name__ == "__main__":
    main()