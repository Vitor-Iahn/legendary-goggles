print('Aula011: Cores no terminal')

#Existe um módulo prórpio para cores "Colorize", válida a pesquisa.

print('\033[1;30;41mOlá mundo!\033[m') #Forma "Bagunçada" de usar as cores.

nome = 'vitor'

print('Você terminou o Mundo 1 no Python {}{}{}!'.format('\033[33;40m', nome, '\033[m'))  #Utilizando o ".format" para deixar o print visualmente
                                                                                          # mais bonito, perceba que eu utilizei um comando para
                                                                                          #Deixar colorido e depois eu "limpei" a coloração
#Há também o formato de "Dicionário",
#Utilizado quando o programa é extenso, pois deixa bonito e organizado.

cores = {'Azul':'\033[3;34m',
         'Vermelho':'\033[2;31m',
         'Limpa':'\033[m'}

print('{} {} {}!!!{}'.format(cores['Azul'], 'Olá mundo', cores['Vermelho'], cores['Limpa']))