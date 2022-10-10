print(('-=-'*20), 'Aula012: Condições Aninhadas.', ('-=-'*20))

'''if carro.esquerda():
    Bloco1
elif: carro.direita():        #Significa estrutura aninhanda, não somente True/False, permite uma terceira opção
    blco2
elif: carro.frente():          #Você pode usar quanto ELIF quiser, já o ELSE, acontece apenas uma vez, ou nenhuma. o IF apenas 1 vez sempre ocorre.
    bloco3
else:                       #Carro.ré por exemplo.
    bloco4'''

nome = str(input('Qual é o seu nome? ')).strip().capitalize() #Perguntamos um nome. Condições aninhadas
if nome =='Vitor': #Se o nome for Tal, print.
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': #Forma de dizer um ou o outro, útil com poucos valores.
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana': #Outra forma de fazer a mesma coisa, uma forma mais suscitna é criar uma lista de nomes; Lista = [nomes]
    print('Seu nome é bem normal.') #Else é Opcional, sempre no fim quando ocorrer.
print('Tenha um bom dia, {}!'.format(nome))