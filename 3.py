numero = int(input("Digite um numero: "))

contador = 0

for i in range(1, numero+1):
    if numero % i ==0:
        contador = contador + 1
        print(i, end=' ')

if contador > 2:
    print()
    print(f'o numero {numero} foi divisivel {contador} vezes')
    print(f'{numero} não é um numero primo')
else:
     print()
     print(f'o numero {numero} foi divisivel {contador} vezes')
     print(f'{numero} é um numero primo')
