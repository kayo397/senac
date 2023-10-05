def somarSequencia(number):
    if number is None or len(number) == 0:
        return 0

    sum = 0

    for i in range(len(number)):
        sum += number[i]
    
    return sum


sequencia = [6, 10, 4, 24, 70, 16, 31, 9]

print(somarSequencia(sequencia))
