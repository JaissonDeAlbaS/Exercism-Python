def roman(number):
    numerosRomanos = [
	(1000, "M"),
	(900, "CM"),
	(500, "D"),
	(400, "CD"),
	(100, "C"),
	(90, "XC"),
	(50, "L"),
	(40, "XL"),
	(10, "X"),
	(9, "IX"),
	(5, "V"),
	(4, "IV"),
	(1, "I")
    ]
    
    resultado = list()
    while (number > 0):
        for numero, romano in numerosRomanos:
            for _ in range(number//numero):
                resultado.append(romano)
            number %= numero
    return "".join(resultado)