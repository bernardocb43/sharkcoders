nome_carro = input('Digite o nome de seu carro')
ano_fabricado = int(input("Qual o ano de fabricação do seu carro: "))

resultado = 2024 - ano_fabricado

if resultado <=10:
    print(f'O seu carro chamado {nome_carro} é SEMINOVO')
else:
    print(f'o seu carro chamado {nome_carro} é antigo')
