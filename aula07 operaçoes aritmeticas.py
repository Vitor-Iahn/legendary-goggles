# Ordem de procedencia para operações aritméticas.
# 1ª ( ), parentesis sempre tem preferencia antes de qualquer coisa.
# 2ª **, potênciação é simbolizada por dois asteríscos.
# 3ª *, /, //, %, Multiplicação, divisão, divisão inteira, resto da divisão.
# 4ª +, -, Por último em ordem de procedência, vem o mais e menos.

# print(58 ** 24 + 1287//45 * (178 - 78 % 444444))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 - n2
x = n1 * n2                                                     # ":.3f" Significa; : é o atributo
d = n1 / n2                                                     # . É onde atribuir(depois do ponto)
di = n1 // n2                                                   # 3 É a quantidade de atributos depois do ponto
e = n1 ** n2                                                    # f Significa que o atributo é do tipo "float"
print('A soma é {}, \n a subtração é {} \n a multiplicação é {}, \n a divisão é {:.3f}, '
      '\n a divisão inteira é {}, \n a exponenciação é {}'
      . format(s, m, x,  d, di, e))
