print('Aqui ele vai contar de 0 até 6 (Exclui o último, então, ele conta até 5')
for c in range(0, 6):
    print('Oi')
print('Fim')

print('Aqui ele vai contar o C que é a minha variável, o valor dela é de 0 até 6')
for c in range(0, 6):
    print(c)
print('Fim')

print('Assim ele não faz nada, mesmo eu mandando ele contar de 6 até 0. O ponto é, ele não conta decrescente.'
      'Apenas se eu mandar -1, pois ele diminui 1 a cada laço/volta/"loop"/contagem')
for c in range(6, 0):
    print(c)
print('Fim')

print('Aqui ele conta efetivamente de forma decrescente.')
for c in range(6, 0, -1):
    print(c)
print('Fim')

print('Aqui ele conta de 0 até 6 pulando de 2 a cada  2.')
for c in range(0, 6, 2):
    print('c')
print('Outra forma de fazer o pula pula do for em cima:')
i = int(input('Início: '))
f = int(input('FIM: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

print('C de contador, não exatamente parte do processo.')
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')
