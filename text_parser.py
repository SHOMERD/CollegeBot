
def get_text(page, identity):
    with open(f'{identity}_text.txt', 'r', encoding='utf-8') as file:
        line = str(file.read()).split('---')
    return line[page]