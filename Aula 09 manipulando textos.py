print('\n=================== Manipulando textos (strings) =======================================================================================\n')

print('Para o Python, tudo é um objeto, basta apenas multiplicar um pelo outro ou definir um com o outro.\n')

frase = ('Curso em Vídeo Python') #Toda string começa a contagem com o 0, "Curso em Vídeo Python" tem 20 caracteres.

print(frase[9:13], '= Está "fatiando" a string, onde eu pedi apenas para mostrar o caracter 9 ao 13.\n')
print(frase[9], '= Está pegando apenas o caracter 9 da minha string.\n')
print(frase[9:13], '= Está fatiando do caractec 9 até o 12 da minha string,@@ por que o último caracter não conta!!!\n')
print(frase[9:21:2], '= Do 9 ao 21, pulando de 2 em 2.\n')
print(frase[:5], '= Do começo até o 4. Por que o último não aparece.\n')
print(frase[15:], '= Eu indiquei o início mas não indiquei o final, então ele vai do 15º caracter, até o último.\n')
print(frase[9::3], '= Vai começar no 9, até o final, pulando de 3 em 3.\n')

print('\n=================== Método de Análise =======================================================================================\n')

print(len(frase), '= Mostra quantos caracteres tem a sua frase, no total.\n')
print(frase.count('o'), '= Vai procurar quantas vezes o caracter "o" MINÚSCULO aparece na minha variável.\n')
print(frase.count('o', 0, 13), '= Vai contar quantas vezes o caracter "o" MINÚSCULO aparece na minha variável, entre os caracteres 0 até 13 (ignora último sempre).\n')
print(frase.find('deo'), '= Ele vai me indicar a posiçãio onde começa o caracter "deo".\n')
print(frase.find('Android'), '= Quando o valor retornado for -1, significa que não há o caracter nessa string/variável.\n')
print(('Curso' in frase),'= Existe o valor "Curso" na minha stirng? Retorna valor True ou False. Não é uma funcionalidade, é um operador. Também analisa.\n')

print('\n=================== Método de Transformação =======================================================================================\n'
'             Via de regra, uma string é "imutável"\n')

print(frase.replace('Python', 'Android'), '= Onde tiver Python, ele substitui por Android, mesmo se isso ultrapassa o total de caracteres inicial.\n'
                                          '         Substitui de forma temporária, apenas nessa linha de código, sem verdadeiramente alterar a frase original.\n')
frase3 = frase.replace('Python', 'Android'), 'Também podemos usar o replace para remover os espaços no caso .replace(" ", "")'
print(frase3,'= Essa é a única forma de "transformar" uma string, ou seja, definir ela de novo com o comando: frase3 = frase.replace("Python", "Android").\n')
print(frase.upper(), '= Transforma TODOS os caracteres da string em MAIÚSCULOS.\n')
print(frase.lower(), '= Transforma TODOS os caracteres da string em MINÚSCULOS.\n')
print(frase.capitalize(), '= Joga todos os caracteres para MINÚSCULO e coloca apenas o caracter 0 em MAIÚSCULO.\n')
print(frase.title(), '= Verifica quantas palavras tem nessa string, joga todos os caracteres para MINÚSCULO e o primeiro de cada palavra, transforma em MAIÚSCULO.\n'
                     '                             Utiliza dos espaços (também são caracteres) para diferenciar uma palavra da outra.\n')

frase2 = ('   Aprenda Python  ') #Perceba os espaços excedentes.
print(frase2)
print(frase2.strip(), '= Remove os espaços sobressalentes do início e do final da sua string.\n')
print(frase2.rstrip(), '= Uma variação "right" do comando STRIP, que remove apenas os espaços da direita (Right).\n')
print(frase2.lstrip(), '= Outra variação "right" do comando STRIP, que remova apenas os espaços da esquerda (Left)\n')

print('\n=================== Método de Divisão ========================================================================================\n')

print(frase.split(), '= Por padrão o comando SPLIT divide a sua string a partir dos espaços entre as palavras, criando assim menores "strings"\n'
               'com quantidade de caracteres prórprios em cada um.\n')
print('\n========== Uma junção =====\n')
('-'.join(frase)) #Não ficou claro pra mim.
