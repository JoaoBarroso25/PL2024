# Conversor Simples de Markdown para HTML
**Autor: João Alexandre Antunes da Costa Barroso, A95195**

## Visão Geral do Processamento
- O conversor funciona por meio de funções dedicadas a cada tipo de elemento do Markdown, utilizando expressões regulares para identificar e converter os elementos para HTML.
- **Títulos** são capturados através de uma única expressão regular, determinando o tipo de título (`h1`, `h2`, `h3`) com base no número de cardinais presentes.
- **Formatações de texto** (*itálico* e **negrito**) são tratadas de maneira recursiva, permitindo conteúdo com ambas as formatações. A substituição começa com duplos asteriscos convertidos para `<b></b>`, seguida pela conversão de asteriscos singulares para `<i></i>`.
- **Linhas horizontais** são identificadas quando três ou mais travessões, asteriscos ou sublinhados consecutivos aparecem em uma linha única, sendo substituídos pela tag `<hr>`.
- **Imagens e links** são processados utilizando grupos de captura para diferenciar o URL do texto do link. As imagens são processadas antes dos links para evitar conversões incorretas, devido à semelhança estrutural entre ambos.
- **Listas** são processadas como um bloco único; os elementos individuais são envolvidos em tags `<li>`, e a lista completa é embrulhada em uma tag `<ul>` para listas não ordenadas ou `<ol>` para listas ordenadas.
- O conversor aceita como entrada o caminho do arquivo Markdown e gera um arquivo HTML no mesmo local, com o mesmo nome do arquivo original, mas com a extensão alterada para `.html`, refletindo a conversão realizada.
