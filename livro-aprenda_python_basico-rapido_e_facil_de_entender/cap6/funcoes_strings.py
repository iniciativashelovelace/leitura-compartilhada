nome = ' Iniciativa She Lovelace '

print(nome.center(50, '*'))
print(nome.ljust(50, '*'))
print(nome.rjust(50, '*'))

print(25 * '*' + 'Teste' + 25 * "*")


# Função find() - Retorna a posição da primeira ocorrência de uma substring em uma string
print(nome.find('She'))
print(nome.find('Teste'))

# Função find() - Retorna a posição da primeira ocorrência de uma substring em uma string, com início e fim definidos
print(nome.find('vela', 15, 21))

string13 = "Felipe"
print(string13.isalnum()) 
print(string13.isalpha()) 
print(string13.isnumeric())

print(len(nome))
print(nome.replace('She', 'They'))

print(nome.strip())
print(nome.lstrip())
print(nome.rstrip())