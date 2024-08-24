'''
Este 
é 
um comnetário de N linhas.
'''

# CRIANDO UMA STRING GRANDE COM TABULAÇÃO
string_grande = '''\t Olá. Esta é uma string grande no Python.
\t Aqui você pode usar " ou '
\t Caracteres são escapados como se espera.
\t É a terceira forma de definir uma string, apesar de não ser tão usual.... \t testando o TAB para finalizar'''

print(string_grande)

# CRIAR UMA STRING COM ASPAS DUPLAS E SIMPLES NO MEIO DELA
string3 = "\nA cantora Sinnead O'Connor"
string4 = 'Alfredo disse "Corram aqui para ver isso!"'
print(string3)
print(string4)

# ESCAPANDO STRINGS
string5 = "\nAlfredo disse \"Corram aqui para ver isso!\"" 
string6 = 'Sinnead O\'Connor disse "Nothing compares 2 u"' 
print(string5) 
print(string6)

# ESCAPANDO STRINGS EXIBIR UMA CONTRABARRA
string7 = "Estou escapando uma \\" 
print(string7)