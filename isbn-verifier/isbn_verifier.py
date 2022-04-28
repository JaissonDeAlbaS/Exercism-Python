def is_valid(isbn):
    isbn = isbn.replace('-', '')
    count = 1
    acumulador = []
    if len(isbn) != 10:
        return False
    for numero in isbn:
        if count < 10:
            if not numero.isdigit():
                return False
            else:
                acumulador.append(int(numero))
        elif numero == "X":
                acumulador.append(10)
        elif numero.isdigit():
            acumulador.append(numero)
        else:
            return False
        count += 1
    t = 0
    total = 0
    for x in acumulador:
        total += int(x) * (10 - t)
        t += 1
    return total % 11 == 0