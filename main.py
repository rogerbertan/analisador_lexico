#importa biblioteca RegEx
import re

#Transfere o texto do .txt para a string
arquivo = open('example.txt', 'r')
string_code = arquivo.read()
arquivo.close()

#Declara buffer dos identificadores
buffer_ident = list()

#Declara o dicionário
codigo = {'Cod 1': 'Program', 'Cod 2': 'Label', 'Cod 3': 'Const', 'Cod 4': 'Var', 'Cod 5': 'Procedure',
          'Cod 6': 'Begin', 'Cod 7': 'End', 'Cod 8': 'Integer', 'Cod 9': 'Array', 'Cod 10': 'Of', 
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

#Separa a string por caracteres e palavras em um array
array_code = string_code.split()
array_code.append(None)

#Remove comentários da analise
def check_comentarios():
    for i in range(len(array_code)):
        if array_code[i] == '(' and array_code[i + 1] == '*':
            inicio = i
            for j in range(len(array_code)):
                if array_code[j] == '*' and array_code[j + 1] == ')' and j > i:
                    fim = j + 1
                    while inicio <= fim:
                        array_code.pop(inicio)
                        inicio = inicio + 1

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

#Procura as palavras reservadas e atribui ao buffer
def busca_palavra_reservada():
    for i in range(len(array_code)):
        for j in range(len(codigo)):
            if array_code[i] == codigo['Cod ' + (str(j + 1))]:
                buffer_ident.append(array_code[i])


check_comentarios()

check_caracteres_especiais()

busca_palavra_reservada()

print(buffer_ident)


'''
um = str(1)

print(codigo[('Cod ' + um)])
'''