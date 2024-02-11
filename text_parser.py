
def get_text_student(page):
    with open('student_text.txt', 'r', encoding='utf-8') as file:
        line = str(file.read()).split('---')
    return line[page]