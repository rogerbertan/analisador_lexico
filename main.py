import re

arquivo = open('example1.txt', 'r')
string_code = arquivo.read()
arquivo.close()


string_result = re.sub(..., string_code)
print(string_result)