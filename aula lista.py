n = int(input('Digite um numero: '))
resultados = [1,11]
for c in range(1, 11):
    print('{:2} x {} = {}'.format(n, c, (c * n)))