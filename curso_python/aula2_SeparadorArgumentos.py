# sep = separador, pode ser usado para separar argumentos
# end = define o que será exibido no fim da linha, por padrão, \r\n quebra a linha

print(12, 34, 1001, sep="-", end="\r\n") # vai quebrar a linha
print(56, 78, sep='-', end="##") # nao vai quebrar a linha e vai imprimir ## após 78
print(9, 10, sep='-', end="\n") # vai quebrar a linha