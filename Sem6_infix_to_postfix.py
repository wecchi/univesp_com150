class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[-1]

    def display(self):
        print(self.items)


def infix_to_postfix(infix):
    postfix = ""
    st = Stack()

    for symbol in infix:
        if symbol == ' ' or symbol == '\t':
            continue
        if symbol == '(':
            st.push(symbol)
        elif symbol == ')':
            next = st.pop()
            while next != '(':
                postfix = postfix + next
                next = st.pop()
        elif symbol in "+-*/%^":
            while not st.is_empty() and precedence(st.peek()) >= precedence(symbol):
                postfix = postfix + st.pop()
            st.push(symbol)
        else:
            postfix = postfix + symbol

    while not st.is_empty():
        postfix = postfix + st.pop()
    return postfix


def precedence(symbol):
    if symbol == '(':
        return 0
    elif symbol in '+-':
        return 1
    elif symbol in '*/%':
        return 2
    elif symbol == '^':
        return 3
    else:
        return 0

def evaluate_postfix(postfix):
    st = Stack()

    for symbol in postfix:
        if symbol.isdigit():
            st.push(int(symbol))
        else:
            x = st.pop()
            y = st.pop()

            if symbol == '+':
                st.push(y + x)
            elif symbol == '-':
                st.push(y - x)
            elif symbol == '*':
                st.push(y * x)
            elif symbol == '/':
                st.push(y / x)
            elif symbol == '^':
                st.push(y ** x)

    return st.pop()


#############
while True:
    print("Enter infix expression ( q to quit ) ", end='')

    expression = input()
    if expression == 'q':
        break
    postfix = infix_to_postfix(expression)
    print("Postfix expression is : ", postfix)
    #print("Value of expression : ", evaluate_postfix(postfix))
