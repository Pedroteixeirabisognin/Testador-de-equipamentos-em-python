#!/usr/bin/python
import socket
from subprocess import check_output
import sys

while True:

    num = input('Informe o número da loja!!')
    try:

       a=check_output('ping ' + socket.gethostbyname('loja'+ num), shell=True)
       b = str(a)

       print (socket.gethostbyname('loja'+num))
       b=(socket.gethostbyname('loja'+num))
    except: 
        print('Servidor fora do ar!!')
        sys.exit(0)
    if b.count('10.') == True:

        print('Ap:\n***************\n')
        try:
        
            a = check_output('ping ' + b + '61', shell=True)
            c = str(a)
            d = c.count('TTL')

            print(b + '61' + ' Funcionou!!')
        except :
            print(b + '61' + ' Não Funcionou!!')

        try:
        
            a = check_output('ping ' + b + '62', shell=True)
            c = str(a)
            d = c.count('TTL')

            print(b + '62' + ' Funcionou!!')
        except :
            print(b + '62' + ' Não Funcionou!!')

        print('Rádio Frequência:\n***************\n')
        try:
        
            a = check_output('ping ' + b + '66', shell=True)
            c = str(a)
            d = c.count('TTL')

            print(b + '66' + ' Funcionou!!')
        except :
            print(b + '66' + ' Não Funcionou!!')

        try:
        
            a = check_output('ping ' + b + '67', shell=True)
            c = str(a)
            d = c.count('TTL')

            print(b + '67' + ' Funcionou!!')
        except :
            print(b + '67' + ' Não Funcionou!!')

        print('Terminais de consulta:\n***************\n')
        try:
        
            a = check_output('ping ' + b + '76', shell=True)
            c = str(a)
            d = c.count('TTL')

            print(b + '76' + ' Funcionou!!')
        except :
            print(b + '76' + ' Não Funcionou!!')

        try:
            a = check_output('ping ' + b + '77', shell=True)
            c = str(a)
            d = c.count('TTL')
            print(b + '77' + ' Funcionou!!')
        except :
            print(b + '77' + ' Não Funcionou!!')

        try:
        
            a = check_output('ping ' + b + '78', shell=True)
            c = str(a)
            d = c.count('TTL')

            print(b + '78' + ' Funcionou!!')
        except :
            print(b + '78' + ' Não Funcionou!!')

        try:
            a = check_output('ping ' + b + '79', shell=True)
            c = str(a)
            d = c.count('TTL')
            print(b + '79' + ' Funcionou!!')
        except :
            print(b + '79' + ' Não Funcionou!!')

        try:
        
            a = check_output('ping ' + b + '80', shell=True)
            c = str(a)
            d = c.count('TTL')

            print(b + '80' + ' Funcionou!!')
        except :
            print(b + '80' + ' Não Funcionou!!')

        try:
            a = check_output('ping ' + b + '81', shell=True)
            c = str(a)
            d = c.count('TTL')
            print(b + '81' + ' Funcionou!!')
        except :
            print(b + '81' + ' Não Funcionou!!')
        
    else:
            a=list(b)

            print('Ap:\n***************\n')
            try:
                b=a
                b[-1]='85'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')
            try:
                b=a
                b[-1]='86'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')  


            print('Rádio Frequência:\n***************\n')
            try:
                b=a
                b[-1]='87'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')       
            try:
                b=a
                b[-1]='88'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')       
        
            print('Terminais de consulta:\n***************\n')
            try:
                b=a
                b[-1]='234'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')       

            try:
                b=a
                b[-1]='235'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')       

            try:
                b=a
                b[-1]='236'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')       

            try:
                b=a
                b[-1]='237'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')       
            try:
                b=a
                b[-1]='238'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')       
            try:
                b=a
                b[-1]='239'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')       
            try:
                b=a
                b[-1]='240'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')       
            try:
                b=a
                b[-1]='241'
                b = ''.join(str(y) for y in b)
                b=str(b)
                c = check_output('ping ' + b, shell=True)            
                c = str(c)
                d = c.count('TTL')
                
                print(b + ' funcionou\n')
            except :
                print(b + ' Não funcionou\n')       
