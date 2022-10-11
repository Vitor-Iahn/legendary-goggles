print('\nImportação & Módulos '
      '\n#Para importação de módulos externos, visite www.Pycharm.org.')

print('\nimport math #Esse comando é para importar TODA a biblioteca de matemática.')
print('Quando importamos a biblioteca como um todo, para utilizar algum comando específico, devemos digitar "math.comando".')


print('\nfrom math import sqrt, ceil, floor #Este comando é para importar apenas o requisitado. Reduzindo a carga do módulo no programa. (RAM)')
print('Quando importamos apenas o necessário, podemos chamar o comando apenas com o nome, sem a necessidade de "math.comando" sendo apenas "comando".')

import random #Doc, instalação "interna".
num = random.randint(1, 5)
print('\nSeu número: {}'.format(num))

import emoji #Pypi, Instalação "externa"

print(emoji.emojize('Meu signo é :Aquarius:'))
