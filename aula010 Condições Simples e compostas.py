print('\nAula 10: Condições\n')

'''if condição(): # AND variável OR variável, para acrescentar "Excessões a regra.
    Bloco True
else:                   Nunca esqueça dos dois pontos " : ". Dois blocos nunca ocorrem simultaneamente.
    Bloco False'''

''' Todo comando que estiver colado ao lado esquerdo da tela, SEMPRE irá acontecer,
    Todo comendo que estiver ANINHADO/IDENTAÇÃO, ele pode ou não ser executado, a depender da situação.
    Duas condições não podem ocorrer ao mesmo tempo.'''

#tempo = int(input('Quantos anos tem o seu carro? '))

#if tempo <=3:
#    print('\nCarro novo')
#else:
#    print('\nCarro velho')
#print('\n--Fim--')

'''Condição em uma linha
print('Carro novo' if tempo<=3 else'Carro velho'). #Encurta as linhas porém é visualmente menos simples.'''
'''Se ele tem apenas o "IF" é uma condição simples, quando tem o "ELSE" também, é uma condicional composta.'''

#nome = str(input('Qual é o seu nome? '))
#if nome == 'Vitor':
#    print('Que nome lindo.')
#else:
#    print('Que nome normal.')
#print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('A sua média foi {:.01f}'.format(m))

if m >= 6.0:
    print('Você está acima da média! PARABÉNS')
else:
    print('Que pena, você está abaixo da média, ESTUDE MAIS!')


