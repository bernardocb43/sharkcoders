

# solicitar ao ultlizador que insira um numero
numero = int(input("Digite um numero"))

# exibir todos os numeros que antecedem o número fornecido
print(f'Os numeros que antecedem {numero} são: ')

for i in range(numero):
    print(i)
