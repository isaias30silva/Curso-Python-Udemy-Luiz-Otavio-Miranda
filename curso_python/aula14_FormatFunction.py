# usando a funçao format para exibir valores das variaveis com parametros nomeados

a = 'A'
b = 'B'
c = 1.1

string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a,
    nome2=b,
    nome3=c
)

print(formato)