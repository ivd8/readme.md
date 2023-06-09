def str_func(string):
    """Функция делает заглавными первые буквы каждого слова в строке"""
    return f'Результат: {string.title()}'


text = input('Введите слово: ')
print(f"{str_func(text)}")