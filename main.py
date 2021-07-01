#importa biblioteca RegEx
from os import error, set_inheritable
import re


#Transfere o texto do .txt para a string
arquivo = open('example.txt', 'r')
string_code = arquivo.read()
arquivo.close()

#Declara buffers
buffer = list()
valor = list()
buffer_ident = list()
buffer_literal = list()

#Declara o dicionário
codigo = {'Cod 1': 'Program', 'Cod 2': 'Label', 'Cod 3': 'Const', 'Cod 4': 'Var', 'Cod 5': 'Procedure',
          'Cod 6': 'Begin', 'Cod 7': 'End', 'Cod 8': 'integer', 'Cod 9': 'Array', 'Cod 10': 'Of', 
          'Cod 11': 'Call', 'Cod 12': 'Goto', 'Cod 13': 'If', 'Cod 14': 'then', 'Cod 15': 'Else', 
          'Cod 16': 'While', 'Cod 17': 'Do', 'Cod 18': 'Repeat', 'Cod 19': 'Until', 'Cod 20': 'Readln', 
          'Cod 21': 'Writeln', 'Cod 22': 'Or', 'Cod 23': 'And', 'Cod 24': 'Not', 'Cod 25': 'Identificador', 
          'Cod 26': 'Inteiro', 'Cod 27': 'For', 'Cod 28': 'To', 'Cod 29': 'Case', 'Cod 30': '+', 'Cod 31': '-', 
          'Cod 32': '*', 'Cod 33': '/', 'Cod 34': '[', 'Cod 35': ']', 'Cod 36': '(', 'Cod 37': ')', 
          'Cod 38': ':=', 'Cod 39': ':', 'Cod 40': '=', 'Cod 41': '>', 'Cod 42': '>=', 'Cod 43': '<', 
          'Cod 44': '<=', 'Cod 45': '<>', 'Cod 46': ',', 'Cod 47': ';', 'Cod 48': 'literal', 'Cod 49': '.', 
          'Cod 50': '..', 'Cod 51': '$'}

#Cria espaços entre os caracteres especiais
string_code = re.sub(r'([^0-9A-Za-z\sç])', ' \\1 ', string_code)

#Atribui literal ao buffer
aux = re.search(r"(['])(?:(?=(\\?))\2.)*?\1", string_code)
buffer_literal.append(aux.group())
string_code = re.sub(r"(['])(?:(?=(\\?))\2.)*?\1", " ", string_code)

#Separa a string por caracteres e palavras em um array
array_code = string_code.split()
array_code.append(None)

#Remove comentários da analise
def check_comentarios():
    for i in range(len(array_code)):
        if i < len(array_code):
            if array_code[i] == '(' and array_code[i + 1] == '*':
                inicio = i
                for j in range(inicio, len(array_code)):
                    if j < len(array_code):
                        if array_code[j] == '*' and array_code[j + 1] == ')':
                            fim = j + 2
                            y = inicio
                            while y < fim:
                                array_code.pop(inicio)
                                y += 1

#Testa as palavras reservadas que são conjuntos de 2 carateres especiais
def check_caracteres_especiais():
    for i in range(len(array_code)):
        if array_code[i] == '>':
            if array_code[i + 1] == '=':
                array_code[i] = '>='
                array_code[i + 1] = None
        if array_code[i] == '<':
            if array_code[i + 1] == '=':
                array_code[i] = '<='
                array_code[i + 1] = None
            if array_code[i + 1] == '>':
                array_code[i] = '<>'
                array_code[i + 1] = None
        if array_code[i] == ':':
            if array_code[i + 1] == '=':
                array_code[i] = ':='
                array_code[i + 1] = None
        if array_code[i] == '.':
            if array_code[i + 1] == '.':
                array_code[i] = '..'
                array_code[i + 1] = None

#Remover espaços vazios do array
def pop_none():
    for i in range(len(array_code)-1, -1, -1):
        if array_code[i] == None:
            array_code.pop(i)

#Testa se é um valor inteiro
def isnumber(value):
    try:
        int(value)
    except ValueError:
        return False
    except TypeError:
        return False
    return True

def trylower(value):
    try:
        value = value.lower()
    except AttributeError:
        return False
    return True

#Atribui o próximo caractér a variável CAR
def pegacar(count):
    if count < len(array_code):
        car = array_code[count]
        return car

#Testa se é uma palavra reservada
def busca_palavra_reservada():
    count = 0
    while count <= len(array_code):
        car = pegacar(count)
        aux = False
        for i in range(len(codigo)):
            if car == codigo['Cod ' + (str(i + 1))]:
                buffer.append(car)
                aux = True
        if isnumber(car):
            car = int(car)
            if -32767 <= car <= 32767:
                valor.append(int(car))
                aux = True
        elif aux == False:
            buffer.append('Identificador')
            rep = False
            for i in range(len(buffer_ident)):
                if trylower(car):
                    if buffer_ident[i] == car.lower():
                        rep = True
            if not rep:
                if trylower(car):
                    buffer_ident.append(car.lower())
                else:
                    buffer_ident.append(car)
        count += 1
    buffer_ident.pop()
    buffer.pop()

op = 0

#Main
check_comentarios()
check_caracteres_especiais()
pop_none()
busca_palavra_reservada()

#Menu para seleçao de exibiçao dos buffers
while op != 5:
    op = int(input('\n1 - Mostrar buffer\n2 - Mostrar buffer literal\n3 - Mostrar buffer de identificadores\n4 - Mostrar buffer de valores\n5 - Sair\n\nEscolha uma opçao: '))
    if op == 1:
        print('\n')
        print(buffer)
    elif op == 2:
        print('\n')
        print(buffer_literal)
    elif op == 3:
        print('\n')
        print(buffer_ident)
    elif op == 4:
        print('\n')
        print(valor)
    elif op == 5:
        print('Saindo...')
    else:
        print('\nOpçao Inválida...')





