#!/usr/bin/python
import socket
from subprocess import check_output
import sys



def Verifica10(b):
            a=list(b)
            op= int(input("Informe o que você deseja verificar:\n1-AP\n2-RF\n3-Terminal\n4-Todos\n"))
            PingaTerm10(a,op)   
        
def Verifica52(b):
            a=list(b)
            op= int(input("Informe o que você deseja verificar:\n1-AP\n2-RF\n3-Terminal\n4-Todos\n"))
            PingaTerm52(a,op)

####Função para pingar terminais ip 52####
def PingaTerm52(a,op):
            i=0
            msgA=0
            msgR=0
            msgT=0
            if op == 1 or op == 4:
                i=0
                print('Ap:\n***************\n')
                while True and msgA != 3:
                    try:
                        b=a
                        b[-1]=str(86-i)
                        b = ''.join(str(y) for y in b)
                        b=str(b)
                        c = check_output('ping -w 1000 -n 2 ' + b, shell=True)            
                        c = str(c)
                        d = c.count('TTL')
                        print(b + ' funcionou\n')
                        msgA=0
                    except :
                        print(b + ' Não funcionou\n')
                        msgA=msgA+1
                    i=i+1

            if op == 2 or op == 4:
                i=0
                print('Rádio Frequência:\n***************\n')
                while True and msgR != 3:
                    try:
                        b=a
                        b[-1]=str(87+i)
                        b = ''.join(str(y) for y in b)
                        b=str(b)
                        c = check_output('ping -w 1000 -n 2 ' + b, shell=True)            
                        c = str(c)
                        d = c.count('TTL')
                        print(b + ' funcionou\n')
                        msgR=0
                    except :
                        print(b + ' Não funcionou\n')
                        msgR=msgR+1
                    i=i+1
            if op == 3 or op == 4:
                i=0
                print('Terminal de Consulta:\n***************\n')
                while True and msgT != 3:
                    try:
                        b=a
                        b[-1]=str(234+i)
                        b = ''.join(str(y) for y in b)
                        b=str(b)
                        c = check_output('ping -w 1000 -n 2 ' + b, shell=True)            
                        c = str(c)
                        d = c.count('TTL')
                        print(b + ' funcionou\n')
                        msgT=0
                    except :
                        print(b + ' Não funcionou\n')
                        msgT=msgT+1
                    i=i+1
####Função para pingar terminal ip 10
def PingaTerm10(a,op):
            i=0
            msgA=0
            msgR=0
            msgT=0
            
            if op == 1 or op == 4:
                i=0
                print('Ap:\n***************\n')
                while True and msgA != 3:
                    try:
                        b=a
                        b[-1]=str(161+i)
                        b = ''.join(str(y) for y in b)
                        b=str(b)
                        c = check_output('ping -w 1000 -n 2 ' + b, shell=True)            
                        c = str(c)
                        d = c.count('TTL')
                        print(b + ' funcionou\n')
                        msgA=0
                    except :
                        print(b + ' Não funcionou\n')
                        msgA=msgA+1
                    i=i+1

            if op == 2 or op == 4:
                i=0
                print('Rádio Frequência:\n***************\n')
                while True and msgR != 3:
                    try:
                        b=a
                        b[-1]=str(166+i)
                        b = ''.join(str(y) for y in b)
                        b=str(b)
                        c = check_output('ping -w 1000 -n 2 ' + b, shell=True)            
                        c = str(c)
                        d = c.count('TTL')
                        print(b + ' funcionou\n')
                        msgR=0
                    except :
                        print(b + ' Não funcionou\n')
                        msgR=msgR+1
                    i=i+1
            if op == 3 or op == 4:
                i=0                
                print('Terminal de Consulta:\n***************\n')
                while True and msgT != 3:
                    try:
                        b=a
                        b[-1]=str(176+i)
                        b = ''.join(str(y) for y in b)
                        b=str(b)
                        c = check_output('ping -w 1000 -n 2 ' + b, shell=True)            
                        c = str(c)
                        d = c.count('TTL')
                        print(b + ' funcionou\n')
                        msgT=0
                    except :
                        print(b + ' Não funcionou\n')
                        msgT=msgT+1
                    i=i+1

#### Faz o programa ficar em looping funcionando constantemente####

while True:

    #### Recebe o número da loja a ser verificado#### 

    num = input('Informe o número da loja!!')

    #### TRATA ERROS E EXCEÇÕES

    try:

       #### CHAMA O PROMPT ENTREGANDO OS VALORES PARA "a" EM UM OBJECT #### 
       
       a=check_output('ping ' + socket.gethostbyname('loja'+ num), shell=True)

       #### CONVERTO PARA STRING PRA VERIFICAÇÃO FUTURA EM UM COUNT ####

       b = str(a)

       #### PRINTA O IP DA REDE ####
        
       print (socket.gethostbyname('loja'+num))

       #### ARMAZENA O IP NA VARIÁVEL 'b' ####

       b=(socket.gethostbyname('loja'+num))

       #### SE A REDE ESTIVER FORA DO AR ELE CAI NO EXCEPTION INFORMANDO O ESTADO DA REDE ####
    except:
        
        print('Servidor fora do ar!!')
        b='0'

    #### VERIFICA SE A REDE É 10 ou 52 ####

    if b.count('10.') == True:
        Verifica10(b)
    elif b.count('52.') == True:
        Verifica52(b)
    else:
        print("Voltando...")


        
#############################################

