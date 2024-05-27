class InvalidDataException(Exception):   #
         # """ при срабатывании этого исключения открывается 'Traceback'"""

    def __init__(self, message):
        self.message = message


class ProcessingException(Exception):   #Исключение обработки
    # """ при срабатывании этого исключения программа не прерывается
    # но видно сообщение, что есть ошибка """
    pass


def my_exception(a, b):
    if a == b:
        raise InvalidDataException(f'Вы ввели одинаковые числа {a} и {b}')
    try:                                      # пишем возможную ошибку
        if b == 1:
            raise ProcessingException         #класс ошибки
    except ProcessingException as prex:       #если есть ошибка то сработает этот код
        print(f'ОЙ!! {type(prex)}. при делении на 1 получаем само число')

    else:                                     # если нет ошибки то этот код
        print(f'результат деления {a / b}')

    finally:                                  #этот код сработает в любом случае
        print(f'Вы ввели числа {a} и {b}')



a = int(input('a: '))
b = int(input('b: '))
my_exception(a, b)





