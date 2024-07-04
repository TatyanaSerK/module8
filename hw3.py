def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:  # сумма чисел в numbers путём перебора
        try:
            if isinstance(i, int):  # увеличивать переменную result
                result += i
            else:  # Если при переборе встречается тип отличного от числового, то обработать исключение TypeError
                raise TypeError(print(f'Некорректный тип данных для подсчёта суммы - {i}'))
        except TypeError as ty:  # обработать исключение TypeError, увеличив счётчик incorrect_data на 1
            incorrect_data += 1
    return (result, incorrect_data)  # возвращает кортеж из двух значений


def calculate_average(numbers):
    try: # если в numbers записана не коллекция
        if len(numbers) > 1:
            per_sum = personal_sum(numbers)  # для подсчёта суммы используем функцию personal_sum
            try: # обработаем исключение ZeroDivisionError
                if per_sum[0] == 0: #если нет чисел в коллекции
                    raise ZeroDivisionError
            except:
                return 0 # при делении на 0 и верните 0
            sred = per_sum[0] / (len(numbers) - per_sum[1]) # счмтаем среднее
            return sred # возвращанм
        else: #
            raise TypeError #
    except TypeError:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
