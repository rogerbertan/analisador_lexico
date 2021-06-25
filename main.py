import re

arquivo = open('example1.txt', 'r')
string_code = arquivo.read()
arquivo.close()

buffer_ident = list()

codigo = {'Program': 'Cod 1', 'Label': 'Cod 2', 'Const': 'Cod 3', 'Var': 'Cod 4', 'Procedure': 'Cod 5',
          'Begin': 'Cod 6', 'End': 'Cod 7', 'Integer': 'Cod 8', 'Array': 'Cod 9', 'Of': 'Cod 10', 'Call': 'Cod 11',
          'Goto': 'Cod 12', 'If': 'Cod 13', 'Then': 'Cod 14', 'Else': 'Cod 15', 'While': 'Cod 16', 'Do': 'Cod 17',
          'Repeat': 'Cod 18', 'Until': 'Cod 19', 'Readln': 'Cod 20', 'Writeln': 'Cod 21', 'Or': 'Cod 22',
          'And': 'Cod 23', 'Not': 'Cod 24', 'Identificador': 'Cod 25', 'Inteiro': 'Cod 26', 'For': 'Cod 27',
          'To': 'Cod 28', 'Case': 'Cod 29', '+': 'Cod 30', '-': 'Cod 31', '*': 'Cod 32', '/': 'Cod 33', '[': 'Cod 34',
          ']': 'Cod 35', '(': 'Cod 36', ')': 'Cod 37', ':=': 'Cod 38', ':': 'Cod 39', '=': 'Cod 40', '>': 'Cod 41',
          '>=': 'Cod 42', '<': 'Cod 43', '<=': 'Cod 44', '<>': 'Cod 45', ',': 'Cod 46', ';': 'Cod 47',
          'literal': 'Cod 48', '.': 'Cod 49', '..': 'Cod 50', '$': 'Cod 51'}

array_code = string_code.split()

def busca_palavra_reservada():
    for i in range(len(array_code)):
        for j in range(len(codigo)):
            if array_code[i] == codigo[j]:
                print(codigo[j])

busca_palavra_reservada()
'''
#print(codigo[5])

print(codigo['='])
'''
