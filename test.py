#importa biblioteca RegEx
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

#Cria espaços entre os caracteres especiais
string_code = re.sub(r'([^0-9A-Za-z\sç])', ' \\1 ', string_code)
aux = re.search(r"(['])(?:(?=(\\?))\2.)*?\1", string_code)
buffer_literal.append(aux.group())
print(buffer_literal)