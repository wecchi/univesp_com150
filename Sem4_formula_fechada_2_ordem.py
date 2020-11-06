## Exercício da video aula  href="https://youtu.be/DupEWPyM9PQ?t=1042

def T(n):
    if n == 1:
        return 3
    else:
        return 2 * T(n / 2) + 2 * n


print(str('Início dos testes').center(80, '-'))
numberToBynary = [2 ** x for x in range(1, 21)]
for i in numberToBynary:
    print('T({0}) = {1:}'.format(i, int(T(i))))


## Criando uma seguência com 4 casos básicos:
def wsY(n):
    if n in [1, 2, 3, 4]:
        return n + 3 - (n ** 2 + 1)
    else:
        return 2 * wsY(n - 1) + 3 * wsY(n - 2) + wsY(n - 3) // n - 5 * wsY(n - 4) + 3 * n ** 2


print(str('Início dos testes').center(80, '-'))
for i in range(1, 21):
    print('wsY({0}) = {1:}'.format(i, wsY(i)))


## Exemplo 18, seção 3.2
# GERSTING. Fundamentos Matemáticos para a Ciência da Computação. São Paulo: Grupo GEN, 2016. 9788521633303.
# Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788521633303/. Acesso em: 04 Nov 2020


def T(n):
    if n == 1:
        return 2
    else:
        return T(n - 1) + (n + 1)


print(str('  >>>  Exemplo 18, seção 3.2  <<<  ').center(80, '-'))
for i in range(1, 11):
    print("T({0}) = {1:}".format(i, T(i)))
