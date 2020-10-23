

def funcao():
    print("Hello world")


funcao()

def my_second_function(msg):
    return msg + "My function!"


print(my_second_function("Essa é "))

def saudacao (msg="Oi", nome="usuário"):
    return "{}, {}".format(msg, nome)

print(saudacao(nome="Thiago"))


def function_somatoria (*args):
    return sum(args)

print(function_somatoria(2, 4, 6, 7))
