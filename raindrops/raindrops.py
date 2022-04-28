def convert(number):
    number = int(number)
    if((number % 3 == 0) or (number % 5 == 0) or (number % 7 == 0)):
        resp = ""
        if((number % 3) == 0):
            resp += 'Pling'
        if((number % 5) == 0):
            resp += 'Plang'
        if((number % 7) == 0):
            resp += 'Plong'
        return resp
    else:
        return str(number)