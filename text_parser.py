
def get_text(page: int, identity: str) -> str:
    with open(f'{identity}_text.txt', 'r', encoding='utf-8') as file:
        line = str(file.read()).split('---\n')
    print(page, identity, '\n\n\n', type(line[page]))
    
    return line[page]

