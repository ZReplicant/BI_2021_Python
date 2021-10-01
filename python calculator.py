a = int(input('Type the first number'))
oper = input('Choose the operation\n+, -, *, / or :, //, %')
b = int(input('Type the second number'))
if b == 0 and (oper == '/' or oper == ':' or oper == '//' or oper == '%'):
    print('I hate zero division, type something else')
elif oper == '+':
    res = a + b
elif oper == '-':
    res = a - b
elif oper == '*':
    res = a * b
elif oper == '/' or oper == ':':
    res = a / b
elif oper == '//':
    res = a // b
elif oper == '%':
    res = a % b
print(res)
