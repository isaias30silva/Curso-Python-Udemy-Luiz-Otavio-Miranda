# conversao de tipos, coercao, type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos: str, int, float, bool

# para fazer a conversao, coloca-se o tipo desejado antes, abre parenteses e dentro insere o valor original
print(int('1'), type(int('1'))) # str sendo convertida para int
print(type(float('1') + 1)) # exibindo o tipo do dado
print(bool(' ')) # convertendo uma str vazia para boolean
print(str(11) + 'b') # converte o inteiro 11 para str, concatenando o resultado com a letra b