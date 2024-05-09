# TPC4: Analisador de Tokens para SQL Utilizando PLY
**Autor: João Alexandre Antunes da Costa Barroso, A95195**

## Descrição do Projeto
Este projeto envolve o desenvolvimento de um analisador léxico para SQL, utilizando a biblioteca `ply` do Python. O objetivo principal é interpretar código SQL entregue via _standard input_ (STDIN), categorizando cada token identificado para facilitar a análise e compreensão da consulta SQL.

### Funcionalidade
- O programa é capaz de ler consultas SQL a partir da entrada padrão.
- Utiliza a ferramenta `ply` para construir um léxico que identifica e categoriza tokens de SQL.
- A saída do programa detalha cada token reconhecido, juntamente com sua categoria, proporcionando clareza sobre a estrutura do código SQL processado.

### Exemplo de Uso
Supondo que o arquivo `test.txt` contenha múltiplas consultas SQL para testar diferentes aspectos do lexer, o resultado esperado ao executar o programa seria como segue:

```sh
> cat test.txt | python3 tokenizer.py
LexToken(SELECT,'SELECT',1,0)
LexToken(IDENTIFIER,'nome',1,7)
LexToken(IDENTIFIER,'idade',1,13)
LexToken(FROM,'FROM',1,19)
LexToken(IDENTIFIER,'funcionarios',1,24)
LexToken(WHERE,'WHERE',1,37)
LexToken(IDENTIFIER,'idade',1,43)
LexToken(OP_GE,'>=',1,49)
LexToken(NUMBER_LITERAL,30,1,52)
LexToken(AND,'AND',1,55)
LexToken(IDENTIFIER,'salario',1,59)
LexToken(OP_LE,'<=',1,67)
LexToken(NUMBER_LITERAL,5000,1,70)
LexToken(SELECT,'SELECT',2,0)
LexToken(IDENTIFIER,'*',2,7)
LexToken(FROM,'FROM',2,9)
LexToken(IDENTIFIER,'vendas',2,14)
LexToken(WHERE,'WHERE',2,21)
LexToken(IDENTIFIER,'data_venda',2,27)
LexToken(BETWEEN,'BETWEEN',2,38)
LexToken(STRING,'2024-01-01',2,46)
LexToken(AND,'AND',2,58)
LexToken(STRING,'2024-03-01',2,62)
LexToken(SELECT,'SELECT',3,0)
LexToken(IDENTIFIER,'departamento',3,7)
LexToken(IDENTIFIER,'COUNT(*)',3,21)
LexToken(FROM,'FROM',3,30)
LexToken(IDENTIFIER,'funcionarios',3,35)
LexToken(GROUP_BY,'GROUP BY',3,49)
LexToken(IDENTIFIER,'departamento',3,58)
LexToken(HAVING,'HAVING',3,71)
LexToken(IDENTIFIER,'COUNT(*)',3,78)
LexToken(OP_GT,'>',3,88)
LexToken(NUMBER_LITERAL,10,3,90)























