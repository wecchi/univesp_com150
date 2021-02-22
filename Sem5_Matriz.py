## Definição das classes

class a:
    """
    Element of matrix
    """

    def __init__(self, r, c, data):
        # Conversor dos índices dos elementos
        def conv_index(n):
            chr_uni = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
            i = ''
            for e in str(n):
                i += chr_uni[int(e)]
            return i

        self.a = {'{0}_{1}'.format(r, c): data}
        self.r = r
        self.c = c
        self.type = 'binary' if data in [0, 1] else type(data)
        self.value = data
        self.title = '𝒶{0}{1}'.format(conv_index(r), conv_index(c))

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return '{0} = {1}'.format(self.title, self.value)

    # Comparação entre elementos: lt(a, b) is equivalent to a < b
    def __lt__(self, other):
        if type(other) == a:
            return (self.title == other.title) and (self.value < other.value)
        else:
            return False

    # Comparação entre elementos: le(a, b) is equivalent to a <= b
    def __le__(self, other):
        if type(other) == a:
            return (self.title == other.title) and (self.value <= other.value)
        else:
            return False

    # Comparação entre elementos: eq(a, b) is equivalent to a == b
    def __eq__(self, other):
        if type(other) == a:
            return self.a == other.a
        else:
            return False

    # Comparação entre elementos: ne(a, b) is equivalent to a != b
    def __ne__(self, other):
        if type(other) == a:
            return (self.title == other.title) and (self.value != other.value)
        else:
            return False

    # Comparação entre elementos: gt(a, b) is equivalent to a > b
    def __gt__(self, other):
        if type(other) == a:
            return (self.title == other.title) and (self.value > other.value)
        else:
            return False

    # Comparação entre elementos: ge(a, b) is equivalent to a >= b
    def __ge__(self, other):
        if type(other) == a:
            return (self.title == other.title) and (self.value >= other.value)
        else:
            return False

    # operator.neg(obj) operator.__neg__(obj) Return obj negated (-obj).
    def __neg__(self):
        if self.type == 'binary':
            return not self.value
        elif self.type == int or self.type == float:
            return - self.value
        else:
            return None

    # operator.__mul__(a, b) Return a * b, for a and b numbers
    def __mul__(self, other):
        if type(other) == a:
            return self.value * other.value
        else:
            return self.value * other

    # operator.__add__(a, b) Return a + b, for a and b numbers.
    def __add__(self, other):
        if type(other) == a:
            if self.type == other.type == 'binary':
                return int(self.value or other.value)
            else:
                return self.value + other.value
        else:
            if (self.type == 'binary' or self.type == int or self.type == float) and \
                    (type(other) == int or type(other) == float):
                return self.value + other
            else:
                return None

    # operator.iadd(a, b) operator.__iadd__(a, b) a = iadd(a, b) is equivalent to a += b.
    def __iadd__(self, other):
        self.value = self.value + other.value
        return self.value

    # operator.sub(a, b) operator.__sub__(a, b) Return a - b
    def __sub__(self, other):
        if type(other) == a:
            if self.type == other.type == 'binary':
                return abs(self.value - other.value)
            else:
                return self.value - other.value
        else:
            if (self.type == 'binary' or self.type == int or self.type == float) and \
                    (type(other) == int or type(other) == float):
                return self.value - other
            else:
                return None

    def __index__(self):
        return id(self)

    # operator.floordiv(a, b) operator.__floordiv__(a, b) Return a // b.
    def __floordiv__(self, other):
        if type(other) == a:
            if self.type == other.type == 'binary':
                return int(self.value and other.value)
            elif (self.type == int or self.type == float) and (other.type == int or other.type == float):
                return self.value // other.value
            else:
                return None
        else:
            if (self.type == int or self.type == float) and (type(other) == int or type(other) == float):
                return self.value // other
            else:
                return None

    # operator.truediv(a, b) operator.__truediv__(a, b) Return a / b where 2/3 is .66 rather than 0.
    # This is also known as “true” division.
    def __truediv__(self, other):
        if type(other) == a:
            if self.type == other.type == 'binary':
                return int(self.value and other.value)
            elif (self.type == int or self.type == float) and (other.type == int or other.type == float):
                return self.value / other.value
            else:
                return None
        else:
            if (self.type == int or self.type == float) and (type(other) == int or type(other) == float):
                return self.value / other
            else:
                return None

    # operator.mod(a, b) operator.__mod__(a, b) Return a % b.
    def __mod__(self, other):
        if type(other) == a:
            if self.type == other.type == 'binary':
                return int(self.value and other.value)
            elif (self.type == int or self.type == float) and (other.type == int or other.type == float):
                return self.value % other.value
            else:
                return None
        else:
            if (self.type == int or self.type == float) and (type(other) == int or type(other) == float):
                return self.value % other
            else:
                return None

    # operator.or_(a, b) operator.__or__(a, b) Return the bitwise or of a and b.
    def __or__(self, other):
        if type(other) == a:
            return self.value or other.value
        else:
            return self.value or other

    # operator.and_(a, b) operator.__and__(a, b) Return the bitwise and of a and b.
    def __and__(self, other):
        if type(other) == a:
            return self.value and other.value
        else:
            return self.value and other

    # operator.inv(obj) operator.invert(obj) operator.__inv__(obj) operator.__invert__(obj)
    def __invert__(self):
        if self.type == 'binary':
            return not self.value
        elif self.type == int:
            return ~self.value
        else:
            return None

    # operator.pos(obj) operator.__pos__(obj) Return obj positive (+obj).
    def __pos__(self):
        if self.type == 'binary':
            return self.value
        elif (self.type == int) or (self.type == float):
            return abs(self.value)
        else:
            return None

    # operator.pow(a, b) operator.__pow__(a, b) Return a ** b, for a and b numbers.
    def __pow__(self, power, modulo=None):
        if self.type == 'binary' or self.type == int or self.type == float:
            return self.value ** power
        else:
            return None


class Matrix:
    """
    Definition the Matrix
    """
    def __init__(self, name, items, rows, cols=None):
        """
        Cria um objeto do tipo Matriz
        :param name: A letter or name of the Matrix
        :param items: list of the matrix elements
        :param rows: number of rows to create matrix
        :param cols: number of cols to create matrix
        """
        max_col = len(items) // rows if cols is None else cols
        self.name = ''
        self.type = ''
        self.title = ''
        self.rows = rows
        self.cols = max_col
        self.elements = {}
        self.set_name(name)

        max_col += 1
        rx = 0
        ix = 0
        while rx < rows:
            rx += 1
            for c in range(1, max_col):
                item = None if ix > (len(items) - 1) else items[ix]
                key = (rx, c)
                self.elements[key] = a(rx, c, item)
                if self.type != 'any':
                    if self.elements[key].type == 'binary':
                        t = 'binary'
                    else:
                        t = str(type(item))
                        t = t[t.rfind('.')+1:].replace("""'>""", '').replace("""<class '""", '')
                    self.type = t if (len(self.type) == 0 or self.type == t) else 'any'
                ix += 1

    def __repr__(self):
        return '{0} = {1}'.format(self.title, self.elements)

    def __str__(self):
        s = '{0} = '.format(self.title)
        spaces = len(s) - 1
        s += '│\t'
        rx = 1
        for e in self.elements.values():
            if e.r == rx:
                s += str(e.value) + '\t'
            else:
                s += '│\n' + ' '.ljust(spaces) + '│\t' \
                     + str(e.value) + '\t'
                rx += 1
        s += '│'
        return s

    # operator.__add__(a, b) Return a + b, for a and b numbers.
    def __add__(self, other):
        if type(other) == Matrix:
            res = Matrix('{0} + {1}'.format(self.title, other.name), [0], self.rows, self.cols)
            if (self.cols == other.cols) and (self.rows == other.rows):
                for k in self.elements.keys():
                    res.elements[k] = a(k[0], k[1], self.elements[k] + other.elements[k])
                return res
            else:
                return '∄ {0} + {1}'.format(self.title, other.title)
        else:
            if type(other) == int or type(other) == float:
                res = Matrix('⟨{0} + ({1})⟩'.format(self.name, other), [0], self.rows, self.cols)
                for k in self.elements.keys():
                    res.elements[k] = a(k[0], k[1], self.elements[k] + other)
                return res
            else:
                return '∄ ' + self.title + ' + ' + str(other)

    # operator.sub(a, b) operator.__sub__(a, b) Return a - b
    def __sub__(self, other):
        if type(other) == Matrix:
            res = Matrix('{0} - {1}'.format(self.title, other.name), [0], self.rows, self.cols)
            if (self.cols == other.cols) and (self.rows == other.rows):
                for k in self.elements.keys():
                    res.elements[k] = self.elements[k] - other.elements[k]
                return res
            else:
                return '∄ {0} - {1}'.format(self.title, other.title)
        else:
            if type(other) == int or type(other) == float:
                res = Matrix('⟨{0} - ({1})⟩'.format(self.name, other), [0], self.rows, self.cols)
                for k in self.elements.keys():
                    res.elements[k] = self.elements[k] - other
                return res
            else:
                return '∄ ' + self.title + ' - ' + str(other)

    # operator.__mul__(a, b) Return a * b, for a and b numbers
    def __mul__(self, other):
        if type(other) == Matrix:
            # Crio uma matriz só com ZEROS para acomodar os números que serão usados
            res = Matrix('⟨{0} × {1}⟩'.format(self.title, other.title),
                         [0 for x in range(self.rows*other.cols)],
                         self.rows,
                         other.cols)
            if self.cols == other.rows:
                for i in range(1, self.rows + 1):
                    for j in range(1, other.cols + 1):
                        value = 0
                        for m in range(1, self.cols + 1):
                            if self.type == 'binary':
                                value = value | (self.elements[(i, m)] * other.elements[(m, j)])
                            else:
                                value += self.elements[(i, m)] * other.elements[(m, j)]
                        res.elements[(i, j)] = a(i, j, value)
                return res
            else:
                return '∄ {0} × {1}'.format(self.title, other.title)
        else:
            if type(other) == int or type(other) == float:
                res = Matrix('⟨{0} × ({1})⟩'.format(self.name, other), [0], self.rows, self.cols)
                for k in self.elements.keys():
                    res.elements[k] = self.elements[k] * other
                return res
            else:
                return '∄ ' + self.title + ' * ' + str(other)

    def __pow__(self, power, modulo=None):
        """
        Obtém a multiplicação booleana da matriz
        """
        # Calcula no máximo a potência de tamanho rows
        exp = min(self.rows, power)

        # Conversor dos índices de elevação da matriz
        def superscript(n):
            chr_uni = ['º', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
            i = ''
            for e in str(n):
                i += chr_uni[int(e)]
            return '⁽' + i + '⁾'

        if self.type == 'binary':
            newname = self.name + superscript(exp)
            # Cria a 2ª potência da matriz
            res = self.__mul__(self)
            # Se tiver elevação, realiza
            for x in range(3, exp+1):
                res = res.__mul__(self)
            res.set_name(newname)
            return res
        else:
            return None

    def set_name(self, name):
        """
        Altera o nome interno da matriz (exibido quando impresso)
        :param name: especifica o novo nome (interno) da matriz
        """
        # Conversor dos índices dos elementos
        def conv_index(n):
            chr_uni = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
            i = ''
            for e in str(n):
                i += chr_uni[int(e)]
            return i

        self.name = str(name).upper().replace(" ", "")
        self.title = '{0}{1}ₓ{2}'.format(self.name, conv_index(self.rows), conv_index(self.cols))

    def __delitem__(self, key):
        pass

    def get_diag_p(self):
        """
        Obtêm a diagonal principal da matriz (caso seja quadrada)
        :return diagonal principal
        """
        if self.rows == self.cols:
            res = []
            for i in range(1, self.rows + 1):
                res.append(self.elements[(i, i)].value)
            return res
        else:
            return '∄ diagonal principal para ' + self.title

    def get_diag_s(self):
        """
        Obtêm a diagonal secundária da matriz (caso seja quadrada)
        :return diagonal principal
        """
        if self.rows == self.cols:
            res = []
            c = 1
            for i in range(self.rows, 0, -1):
                res.append(self.elements[(i, c)])
                c += 1
            return res
        else:
            return '∄ diagonal secundária para ' + self.title

    def sum_all_elements(self):
        """
        Calcula a soma de todos os itens da matriz
        :return: valor da somatória ou texto do erro
        """
        if (self.type == "int") or (self.type == "float"):
            res = 0
            for e in self.elements.values():
                res += e
            return res
        else:
            return '∄ ∑({0})'.format(self.type)

    def get_characteristics(self):
        """
        Retorna as características da matriz
        :return: text
        """

        # Verifica se é uma matriz nula
        is_null = True
        for i in self.elements.values():
            is_null = (is_null and i == 0)
            if not is_null:
                break

        # Verifica propriedades das diagonais
        is_diagonal = bool(self.rows == self.cols)
        is_triangular_sup = is_triangular_inf = is_diagonal
        is_identidade = bool((self.type == "int") or (self.type == "float"))
        if is_diagonal:
            # Verifica se é uma matriz identidade? (1 para todos os itens a diagonal principal e os demais zero)
            if is_identidade:
                sum_of_diag_p = sum(self.get_diag_p())
                sum_of_all = self.sum_all_elements()
                is_identidade = bool(sum_of_all == self.rows == sum_of_diag_p)
                # Verifica se é uma matriz diagonal (ou seja só existem valores na diagonal principal)
                if not is_identidade:
                    is_diagonal = (sum_of_all == sum_of_diag_p)

                # Verifica as propriedades de triangular superior
                sum_of_sup = sum_of_inf = 0
                for i in range(1, self.rows):
                    c = i
                    while c <= self.cols:
                        sum_of_sup += self.elements[(i, c)].value
                        c += 1
                is_triangular_sup = bool(sum_of_all == sum_of_sup)

                # Verifica as propriedades de triangular inferior
                for i in range(self.rows, 0, -1):
                    c = 1
                    while c <= i:
                        sum_of_inf += self.elements[(i, c)].value
                        c += 1
                is_triangular_inf = bool(sum_of_all == sum_of_inf)

        # Ccomposição dos textos resumo a serem apresentados ao usuário
        res = "Características da Matriz {0}:\n".format(self.title)
        res += "\t↪ Contém {0} elementos do tipo {1}\n".format(self.rows*self.cols, self.type)
        if self.rows == 1:
            res += "\t↪ é uma matriz LINHA DE ORDEM {0}\n".format(self.rows)
        if self.cols == 1:
            res += "\t↪ é uma matriz COLUNA DE ORDEM {0}\n".format(self.cols)
        if self.rows == self.rows == 1:
            res += "\t↪ é uma matriz UNITÁRIA\n"
        if self.rows == self.cols:
            res += "\t↪ é uma matriz QUADRADA DE ORDEM {0}\n".format(self.rows)
        else:
            res += "\t↪ é uma matriz RETANGULAR DE ORDEM {0}×{1}\n".format(self.rows, self.cols)
        # Verifica demais características da matriz com base no valor de seus elementos
        if is_null:
            res += "\t↪ é uma matriz NULA\n"
        if is_diagonal:
            res += "\t↪ é uma matriz DIAGONAL\n"
        if is_identidade:
            res += "\t↪ é uma matriz IDENTIDADE\n"
        if is_triangular_sup:
            res += "\t↪ é uma matriz TRIANGULAR SUPERIOR\n"
        if is_triangular_inf:
            res += "\t↪ é uma matriz TRIANGULAR INFERIOR\n"
        return print(res)


## Calculadora de produto booleano
def calcula_acessibilidade(m0):
    # Transformando a matriz acima numa lista linear
    numnode = len(m0)
    if numnode > 1:
        mlist = []
        for m in m0:
            mlist.extend(m)
        # Obtendo a matriz de adjacência
        a1 = Matrix('a', mlist, numnode)
        # limpando a lista
        mlist.clear()
        # Adicionando as matrizes na lista (para facilitar a saída impressa)
        for i in range(1, numnode+1):
            if i == 1:
                mlist.append(a1)
            else:
                mlist.append(a1**i)
        # Imprimindo as matrizes:
        print('\n', str('>>> Impressão das Matrizes multiplicadas <<<').center(80, '-'))
        for m in mlist:
            print(m)
            a1 += m
            print('\n', str('').center(80,'-'))
        # Calculando e imprimindo a matriz de acessibilidade
        a1.set_name('R')
        print(str('>>> Matriz de ACESSIBILIDADE <<<').center(80, '-'),
              '\n', str('').center(80,'-'), '\n', a1)
        # Limpando a memória
        del mlist
        del a1


#Dado de entrada - matriz booleana de adjacência
m0 = [[0,1,0,0,0],
      [0,0,1,0,0],
      [1,0,0,1,0],
      [0,0,0,0,0],
      [1,0,1,0,0]]
calcula_acessibilidade(m0)

