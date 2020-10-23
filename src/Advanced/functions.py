

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


# Functions

def percentage (number, percentage):
    return (number + (number * percentage / 100))

print(percentage(50, 25))

def fizzBuzz (n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 5 == 0:
        return "buzz"
    if n % 3 == 0:
        return "fizz"
    return n

print(fizzBuzz(100))
