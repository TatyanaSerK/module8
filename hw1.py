
def add_everything_up(n1, n2):
    try:
        sum = n1 + n2

    except:
        a = str(n1)
        b = str(n2)
        sum = str(a+b)

    finally:
        return sum


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


