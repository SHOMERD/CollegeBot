
def get_text(page, identity):
    with open(f'{identity}_text.txt', 'r', encoding='utf-8') as file:
        line = str(file.read()).split('---\n')
    print(page, identity, '\n\n\n', line[page])
    
    return line[page]

