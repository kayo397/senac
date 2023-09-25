number = int(input("Insira um número: "))
soma = 0

for i in range(2, number+1, 2):
    if i % 2 == 0:
        soma += i

print(soma)
