from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')
try:
    if capitalize(None) is not None:
        raise Exception('Функция работает неверно!')
except:
    raise Exception('Функция работает неверно!')

if capitalize('1') != '1':
    raise Exception('Функция работает неверно!')

if capitalize('_') != '_':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
