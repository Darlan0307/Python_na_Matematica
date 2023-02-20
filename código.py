# atribuindo variáveis

a, b, c = 2, 4, -6

# encontrando o delta

delta = b**2 - 4 * a * c

# achando as raízes com concições

if delta > 0:
    x1 = round((-b + delta**(1/2))/2*a, 2)
    x2 = round((-b - delta**(1/2))/2*a, 2)
    print('as raizes são {} e {}'.format(x1, x2))
elif delta == 0:
    x = round(-b / 2*a, 2)
    print('a solução é {}'.format(x))
else:
    print('não existe solução real para essa expressão')

# definindo a função Bhaskara


def Bhaskara(a, b, c):
    delta = b**2 - 4 * a * c

    if delta > 0:
        x1 = round((-b + delta**(1/2))/2*a, 2)
        x2 = round((-b - delta**(1/2))/2*a, 2)
        print('as raizes são {} e {}'.format(x1, x2))
    elif delta == 0:
        x = round(-b / 2*a, 2)
        print('a solução é {}'.format(x))
    else:
        print('não existe solução real para essa expressão')


Bhaskara(a=2, b=3, c=1)
