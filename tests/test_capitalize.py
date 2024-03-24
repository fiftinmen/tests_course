from capitalize import capitalize


assert capitalize('hello') == 'Hello', 'Функция работает неверно!'


assert capitalize(',') == ',', 'Функция работает неверно!'


try:
    assert capitalize(None) is None, 'Функция работает неверно!'
except:
    raise Exception('Функция работает неверно!')


assert capitalize('1') == '1', 'Функция работает неверно!'


assert capitalize('_') == '_', 'Функция работает неверно!'


print('Все тесты пройдены!')

