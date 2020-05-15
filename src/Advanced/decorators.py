import functools


def meu_decorador(funcao):
    @functools.wraps(funcao)
    def funcao_func():
        print('********Encapsulando**********')
        funcao()
        print("********************")
    return funcao_func()


@meu_decorador
def minha_funcao():
    print("Eu sou uma função")

