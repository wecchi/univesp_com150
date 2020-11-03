"""
    GERSTING. Fundamentos Matemáticos para a Ciência da Computação. São Paulo: Grupo GEN, 2016. 9788521633303.
    Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788521633303/. Acesso em: 02 Nov 2020

    EXERCÍCIOS 3.1
    Para os Exercícios 1 a 12, escreva os cinco primeiros valores da sequência.
"""
## 1. S(1) = 10
#     S(n) = S(n – 1) + 10 para n ≥ 2
def ex311(n):
    if n == 1:
        return 10
    else:
        return ex311(n - 1) + 10


print('\n', str('>>> Início do programa 3.1.1 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex311({0}) = {1}'.format(i, ex311(i)))
print(str('>>> Fim do programa 3.1.1 <<<').center(80, '-'))


## 2. C(1) = 5
#     C(n) = 2C(n – 1) + 5 para n ≥ 2
def ex312(n):
    if n == 1:
        return 5
    else:
        return 2 * ex312(n - 1) + 5


print('\n', str('>>> Início do programa 3.1.2 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex312({0}) = {1}'.format(i, ex312(i)))
print(str('>>> Fim do programa 3.1.2 <<<').center(80, '-'))


## 3. A(1) = 2
#     A(n) = 1/A(n-1) ; para n ≥ 2
def ex313(n):
    if n == 1:
        return 2
    else:
        return 1/ex313(n - 1)


print('\n', str('>>> Início do programa 3.1.3 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex313({0}) = {1}'.format(i, ex313(i)))
print(str('>>> Fim do programa 3.1.3 <<<').center(80, '-'))


##4. B(1) = 1
#    B(n) = B(n – 1) + n2 para n ≥ 2
def ex314(n):
    if n == 1:
        return 1
    else:
        return ex314(n - 1) + n ** 2


print('\n', str('>>> Início do programa 3.1.4 <<<').center(80, '-'))
for i in range(1,6):
    print('ex314({0}) = {1}'.format(i, ex314(i)))
print('\n', str('>>> Fim do programa 3.1.4 <<<').center(80, '-'))


##5. S(1) = 1
#    S(n) = S(n-1) + 1/n para n ≥ 2
def ex315(n):
    if n == 1:
        return 1
    else:
        return ex315(n - 1) + 1/n


print('\n', str('>>> Início do programa 3.1.5 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex315({0}) = {1}'.format(i, ex315(i)))
print(str('>>> Fim do programa 3.1.5 <<<').center(80, '-'))


##6. T(1) = 1
#    T(n) = nT(n – 1) para n ≥ 2
def ex316(n):
    if n == 1:
        return 1
    else:
        return n * ex316(n - 1)


print('\n', str('>>> Início do programa 3.1.6 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex316({0}) = {1}'.format(i, ex316(i)))
print(str('>>> Fim do programa 3.1.6 <<<').center(80, '-'))


##7. P(1) = 1
#    P(n) = n2 P(n – 1) + (n – 1) para n ≥ 2
def ex317(n):
    if n == 1:
        return 1
    else:
        return n ** 2 * ex317(n - 1) + (n - 1)


print('\n', str('>>> Início do programa 3.1.7 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex317({0}) = {1}'.format(i, ex317(i)))
print(str('>>> Fim do programa 3.1.7 <<<').center(80, '-'))


##8. A(1) = 2
#    A(n) = nA(n – 1) + n para n ≥ 2
def ex318(n):
    if n == 1:
        return 2
    else:
        return n * ex318(n - 1) + n


print('\n', str('>>> Início do programa 3.1.8 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex318({0}) = {1}'.format(i, ex318(i)))
print(str('>>> Fim do programa 3.1.8 <<<').center(80, '-'))


##9. M(1) = 2
#    M(2) = 2
#    M(n) = 2M(n – 1) + M(n – 2) para n > 2
def ex319(n):
    if n in range(1,3):
        return 2
    else:
        return 2 * ex319(n - 1) + ex319(n - 2)


print('\n', str('>>> Início do programa 3.1.9 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex319({0}) = {1}'.format(i, ex319(i)))
print(str('>>> Fim do programa 3.1.9 <<<').center(80, '-'))


##10. D(1) = 3
#     D(2) = 5
#     D(n) = (n – 1)D(n – 1) + (n – 2)D(n – 2) para n > 2
def ex3110(n):
    if n in range(1,3):
        return 2 * n + 1
    else:
        return (n - 1) * ex3110(n - 1) + (n - 2) * ex3110(n - 2)


print('\n', str('>>> Início do programa 3.1.10 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex3110({0}) = {1}'.format(i, ex3110(i)))
print(str('>>> Fim do programa 3.1.10 <<<').center(80, '-'))


##11. W(1) = 2
#     W(2) = 3
#     W(n) = W(n – 1)W(n – 2) para n > 2
def ex3111(n):
    if n in range(1,3):
        return 1 + n
    else:
        return ex3111(n - 1) * ex3111(n - 2)


print('\n', str('>>> Início do programa 3.1.11 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex3111({0}) = {1}'.format(i, ex3111(i)))
print(str('>>> Fim do programa 3.1.11 <<<').center(80, '-'))


##12. T(1) = 1
#     T(2) = 2
#     T(3) = 3
#     T(n) = T(n – 1) + 2T(n – 2) + 3T(n – 3) para n > 3
def ex3112(n):
    if n in range (1,4):
        return n
    else:
        return ex3112(n - 1) + 2 * ex3112(n - 2) + 3 * ex3112(n - 3)


print('\n', str('>>> Início do programa 3.1.12 <<<').center(80, '-'), sep='')
for i in range(1,6):
    print('ex3112({0}) = {1}'.format(i, ex3112(i)))
print(str('>>> Fim do programa 3.1.12 <<<').center(80, '-'))