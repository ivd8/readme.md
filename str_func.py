def text_upper(text):
    """Функция преврашает все введенные буквы в ЗАГЛВНЫЕ"""
    return f'{text.upper()}'

text = input('Введите слово: ')
print(f'Результат: {text_upper(text)}')