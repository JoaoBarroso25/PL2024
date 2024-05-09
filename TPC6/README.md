# TPC6: Gramática Livre de Contexto LL(1)
**Autor: João Alexandre Antunes da Costa Barroso, A95195**

## Descrição do Projeto
Este projeto descreve a implementação de uma gramática livre de contexto LL(1) para uma linguagem de programação simples. O foco principal é garantir que a gramática seja projetada para ser analisada usando um analisador LL(1), o que implica que cada decisão de análise sintática pode ser feita com um olhar apenas para o próximo símbolo (lookahead).

### Componentes da Gramática
- **Terminais**: Incluem números (`0, 1, 2, ...`), variáveis (`a, b, c, ...`), operadores aritméticos (`+, -, *, /`), parênteses (`(, )`), o símbolo de igual (`=`) e símbolos de leitura e impressão (`?, !`).
- **Não-Terminais**: Compreendem os elementos estruturais da linguagem como Programa (`P`), Declaração (`D`), Expressão (`E`), Termo (`T`) e Fator (`F`).

### Produções e Conjuntos Lookahead
A gramática inclui várias regras de produção que definem como os tokens são combinados para formar instruções válidas:
1. `P -> D P | ε`
2. `D -> ? var | var = E | ! E`
3. `E -> E + T | E - T | T`
4. `T -> T * F | T / F | F`
5. `F -> ( E ) | num | var`

Os conjuntos de lookahead especificados para cada produção garantem que não haja ambiguidade na análise, permitindo que cada símbolo de entrada tenha uma única produção aplicável. Isso é crucial para a análise LL(1) e garante que a gramática possa ser usada com um analisador sintático que siga esse método.

### Prioridades de Operadores
A gramática respeita a prioridade dos operadores, com multiplicação e divisão tendo prioridade sobre adição e subtração. Isso é importante para garantir que as expressões sejam avaliadas corretamente de acordo com as convenções matemáticas.

### Considerações Finais
A estrutura desta gramática LL(1) não só facilita a análise sintática automática mas também ajuda na construção de compiladores e interpretadores que requerem uma abordagem determinística para a análise sintática. A definição clara dos conjuntos lookahead ajuda a evitar conflitos durante a análise, tornando-a uma ferramenta poderosa para desenvolvedores de linguagens de programação.

