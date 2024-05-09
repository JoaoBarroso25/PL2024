import sys
import re

# Converte títulos Markdown para HTML
def convert_title(match):
    title, content = match[1], match[2]
    tag = f'h{len(title)}'
    return f'<{tag}>{content}</{tag}>'

# Processa a conversão de títulos
def process_titles(text):
    return re.sub(r'^(#{1,3}) (.*)', convert_title, text, flags=re.MULTILINE)

# Converte formatações em negrito ou itálico
def process_text_formatting(bold, text):
    delim = r'[^\* \n]'
    content = r'[^\*\n]'
    asterisks = r'\**'
    tag = 'b' if bold else 'i'
    mark = 2 if bold else 1
    pattern = rf'(\*{{{mark}}})({asterisks}{delim}{content}+?{delim}{asterisks})\1'
    formatted_text = re.sub(pattern, rf'<{tag}>\2</{tag}>', text)

    if formatted_text != text:
        formatted_text = process_text_formatting(bold, formatted_text)

    return formatted_text

# Converte linhas em HTML
def convert_lines(text):
    return re.sub(r'^([\-*_])\1{2,}$', r'<hr>', text, flags=re.MULTILINE)

# Converte imagens Markdown para HTML
def convert_image(match):
    return f'<img src="{match[2]}" alt="{match[1]}"/>'

# Converte links Markdown para HTML
def convert_link(match):
    return f'<a href="{match[2]}">{match[1]}</a>'

# Processa links ou imagens
def process_links_or_images(image, text):
    pattern = rf'{"!" if image else ""}\[(.+?)\]\(([^ ]+?)\)'
    conversion = convert_image if image else convert_link
    return re.sub(pattern, conversion, text)

# Converte listas ordenadas Markdown para HTML
def convert_ordered_list(match):
    items = re.sub(r'\d+\. (.*)\n*', r'   <li>\1</li>\n', match[0])
    return f'<ol>\n{items}</ol>\n'

# Converte listas não ordenadas Markdown para HTML
def convert_unordered_list(match):
    items = re.sub(r'\- (.*)\n*', r'   <li>\1</li>\n', match[0])
    return f'<ul>\n{items}</ul>\n'

# Processa listas
def process_lists(ordered, text):
    start = r'\d+\.' if ordered else r'\-'
    translate = convert_ordered_list if ordered else convert_unordered_list
    regex = fr'{start} .*\n*'
    return re.sub(fr'^{regex}(?:{regex})+', translate, text, flags=re.MULTILINE)

# Conversão total de Markdown para HTML
def markdown_to_html(text):
    text = process_titles(text)
    text = process_text_formatting(True, text)
    text = process_text_formatting(False, text)
    text = convert_lines(text)
    text = process_links_or_images(True, text)
    text = process_links_or_images(False, text)
    text = process_lists(False, text)
    text = process_lists(True, text)
    return text

# Processa o arquivo Markdown para converter em HTML
def process_file(inp):
    if len(inp) == 2:
        with open(inp[1], 'r') as file:
            final = markdown_to_html(file.read())
        with open(f'{inp[1]}.html', 'x') as html:
            html.write(final)
    else:
        print("Argumentos inválidos!")

if __name__ == "__main__":
    process_file(sys.argv)
