import re
import sys

def toRpn(infixStr):
    # divide string into tokens, and reverse so I can get them in order with pop()
    tokens = re.split(r' *([\+\-\*\^/]) *', infixStr)
    tokens = [t for t in reversed(tokens) if t!='']
    precs = {'+':0 , '-':0, '/':1, '*':1, '^':2}

    #convert infix expression tokens to RPN, processing only
    #operators above a given precedence
    def toRpn2(tokens, minprec):
        rpn = tokens.pop
        while len(tokens)>0:
            prec = precs[tokens[-1]]
            if prec<minprec:
                break
            op=tokens.pop

            # get the argument on the operator's right
            # this will go to the end, or stop at an operator
            # with precedence <= prec
            arg2 = toRpn2(tokens,prec+1)
            rpn += " " + arg2 + " " +op
        return rpn

    return toRpn2(tokens,0)

print (toRpn("5+3*4^2+1"))
print (toRpn("3/4+(2-y)"))

#prints: 5 3 4 2 ^ * + 1 +
