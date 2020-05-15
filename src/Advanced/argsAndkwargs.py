# args = argumentos
# kwargs = argumento de palavras chave


def meu_metodo(arg1, arg2):
    return arg1 * arg2


print(meu_metodo(2,2))


def simplifica(*args):
    return sum(args)


print(simplifica(7, 7, 8, 10, 20, 2, 3))


def metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


metodo_kwargs(3, 'Oi', 'hã?', nome='Thiago', idade=22)