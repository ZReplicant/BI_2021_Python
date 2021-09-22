a = int(input())
oper = str(input())
b = int(input())
if b == 0 and (oper == '/' or oper == ':' or oper == '//' or oper == '%'):
    print('I hate zero division, type something else')
elif oper == '+':
    print(a + b)
elif oper == '-':
    print(a - b)
elif oper == '*':
    print(a * b)
elif oper == '/' | oper == ':':
    print(a / b)
elif oper == '//':
    print(a // b)
elif oper == '%':
    print(a % b)
