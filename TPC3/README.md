# TPC3: Somador On/Off
**Autor: João Alexandre Antunes da Costa Barroso, A95195**

## Descrição Detalhada do Funcionamento
- O programa utiliza a biblioteca `re` (regex) para processar cada linha de entrada através de uma expressão regular que identifica os comandos 'on', 'off', '=', e números (dígitos).
- Os elementos capturados são inicialmente armazenados em uma lista de listas, que posteriormente é transformada em uma única lista contendo todos os elementos extraídos.
- Durante a iteração sobre os elementos da lista:
  - A ativação do comando 'on' habilita uma flag que permite a soma de números subsequentes.
  - O comando 'off' desativa essa flag, interrompendo a adição de novos números ao somatório.
  - A presença de um '=' resulta na impressão do somatório atual.
- O comportamento do flag garante que apenas os números capturados enquanto o 'on' está ativo sejam somados, permitindo um controle dinâmico sobre quais números são considerados para o cálculo do somatório.

