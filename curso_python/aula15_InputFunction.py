# input = pede dados ao usuário

nome = input('Qual o seu nome?')

numero_1 = input('Digite o primeiro número:')
numero_2 = input('Digite o segundo número:')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'O seu nome é {nome}')
print(f'A soma dos números é: {int_numero_1 + int_numero_2}')