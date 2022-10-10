print('\nA grande diferença entre os LAÇOS de repetição WHILE ou FOR é que quando usamos o \nLAÇO(FOR) sabemos o ponto final. '
      'tudo é estático, pré definido. \nLAÇO(WHILE) é usado quando não sabemos o final do algorítmo, ou seja, não há um range estabelecido\n')
#Definir o N como = 1 foi uma gambiarra para o programa poder começar.
n = 1
continuar = 's'
#Precisamos definir a variável antes do LAÇO(WHILE), para então o LAÇO(WHILE) atribuir valores se necessário
par = 0
impar = 0
while n != 0: #ENQUANTO n for diferente de ZERO:
    n = int(input('Digite um valor: ')) #Será feito a pergunta "Digite um valor: (...)"
    continuar = str(input('Você quer continuar [S/N]: ')).strip().lower() #Opção de sair e ver a resposta ou continuar tentando.
    if n != 0: #Se a gente continuar "jogando" ou seja, n é diferente de ZERO:
        if n % 2 == 0: #Verifica-se se ele é um número PAR, se for , adicione +1 ao contador PAR
            par += 1
        else: #Se ele não for um número PAR, adiciona +1 ao contador de números IMPAR, porque se não é um, só pode ser o outro!
            impar += 1
        if continuar == 'n': #Se o usuário decidir não continuar, o N será igual  ZERO e o jogo termina, mostrando o resultado.
            n = 0
print('Você digitou {} números pares e {} números impares.'.format(par, impar))
