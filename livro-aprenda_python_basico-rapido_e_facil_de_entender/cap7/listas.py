alunos1 = ['José', 'Daniel', 'João']
alunos2 = ['Carlos', 'Augusto', 'Denis']
alunos3 = ['Augusto', 'Denis', 'Carlos', 'Maria', 'Joana']

print(alunos1 + alunos2)
alunos1.remove('José')
print(alunos1)

alunos2.pop(1)
print(alunos2)

while 'Carlos' in alunos3:
  alunos3.remove('Carlos')

print(alunos3)

print(alunos3)
print(alunos3[0:2]) 
print(alunos3[2:4]) 
print(alunos3[2:5])
print(alunos3[:3])
print(alunos3[3:])
print(alunos3[3:-2]) 
print(alunos3[2:-2])