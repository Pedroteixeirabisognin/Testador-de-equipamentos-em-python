#!/usr/bin/python
import socket
from subprocess import check_output

num = input('Informe o número da loja!!')
a=check_output('ping ' + socket.gethostbyname('loja'+num), shell=True)
b = str(a)

print (socket.gethostbyname('loja'+num))
b=(socket.gethostbyname('loja'+num))


if b.count('10.') == True:
    
    try:
    
        a = check_output('ping ' + b + '76', shell=True)
        c = str(a)
        d = c.count('TTL')
        print(d)

        print(b + '76' + ' Funcionou!!')
    except :
        print(b + '76' + ' Não Funcionou!!')

    try:
        a = check_output('ping ' + b + '77', shell=True)
        c = str(a)
        d = c.count('TTL')
        print(d)
        print(b + '77' + ' Funcionou!!')
    except :
        print(b + '77' + ' Não Funcionou!!')

    try:
    
        a = check_output('ping ' + b + '78', shell=True)
        c = str(a)
        d = c.count('TTL')
        print(d)

        print(b + '78' + ' Funcionou!!')
    except :
        print(b + '78' + ' Não Funcionou!!')

    try:
        a = check_output('ping ' + b + '79', shell=True)
        c = str(a)
        d = c.count('TTL')
        print(d)
        print(b + '79' + ' Funcionou!!')
    except :
        print(b + '79' + ' Não Funcionou!!')

    try:
    
        a = check_output('ping ' + b + '80', shell=True)
        c = str(a)
        d = c.count('TTL')
        print(d)

        print(b + '80' + ' Funcionou!!')
    except :
        print(b + '80' + ' Não Funcionou!!')

    try:
        a = check_output('ping ' + b + '81', shell=True)
        c = str(a)
        d = c.count('TTL')
        print(d)
        print(b + '81' + ' Funcionou!!')
    except :
        print(b + '81' + ' Não Funcionou!!')
    
else:
    print('Outro ip')
