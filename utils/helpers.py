whitespace = ' \t\n\r\v\f'
cyrillic_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cyrillic_uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
cyrillic_letters = cyrillic_lowercase + cyrillic_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"№;%:?*()_+.,-=«»„“—…́"""
printable = digits + cyrillic_letters + punctuation + whitespace
