def is_armstrong_number(number):
    str_number = str(number)
    accumulator = 0
    for digit in str_number:
        accumulator += (int(digit))**(len(str_number))
    return accumulator == number