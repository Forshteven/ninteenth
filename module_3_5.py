def get_multiplied_digits(number):
    while number % 10 == 0:
        number //= 10
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(402030000)
print(result)
