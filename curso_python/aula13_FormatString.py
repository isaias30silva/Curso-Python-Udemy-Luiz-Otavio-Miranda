# fstrings
# adicionando f'{} é possível envolver nas chaves uma string que é uma variável

nome = 'Luis Otávio'
altura = 1.80
peso = 95
imc = peso / (altura * altura)

# guardando uma string formatada em uma variável
# assim, basta imprimir essa variável formatada para exibir a string, sem precisar de concatenação
# em numeros de ponto flutuante, inserir :.2f, que significa o número de casas decimais a ser exibida
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
print(nome, "tem", altura, "de altura" + "\npesa", peso, "quilos e seu IMC é",imc)