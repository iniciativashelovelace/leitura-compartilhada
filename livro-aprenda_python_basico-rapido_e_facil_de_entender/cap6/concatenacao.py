nome = 'Iniciativa'
sobrenome = 'Livre'
idade = 10
valor = 10.50991

print('Olá ' + nome + ' ' + sobrenome)

# Concatenando string com número, utilizando a função str() para converter o número em string
print('Olá ' + nome + ' ' + sobrenome + ' você tem ' + str(idade) + ' anos')

# Concatenando string com número, utilizando a função format() para converter o número em string
print('O valor é ' + format(valor))
# Concatenando string com número, utilizando a função format() para converter o número em string e definindo a quantidade de casas decimais (.2f)
print("O valor é " + format(valor, ".2f"))
