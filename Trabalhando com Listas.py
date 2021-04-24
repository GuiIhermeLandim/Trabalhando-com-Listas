# Exercício 1 
list = []
for c in range(0, 5):
    list.append(int(input('Digite um número: ')))
print(f'Os valores selecionados na lista foram: {list}')
print(f'O maior valor selecionado foi: {max(list)} na posição {list.index(max(list))+1}')
print(f'O menor valor selecionado foi: {min(list)} na posição {list.index(min(list))+1}')

# Exercício 2
list = []
while True:
    n = int(input('Digite um número: '))
    if n not in list:
        list.append(n)
    else:
        print('Valor já encontrado. Não adicionado à lista.')
    r = str(input('Deseja adicionar mais um número? [S/N]')).strip().upper()
    while r not in 'SN':
        r = str(input('Deseja adicionar mais um número? [S/N]')).strip().upper()
    if r == 'N':
        print('Programa encerrado.')
        break
list.sort()
print(f'Os números adicionados foram: {list}')

# Exercício 3
geral = []
alunos = []
while True:
    alunos.append(str(input('Digite seu nome: ')).strip().capitalize())
    alunos.append(float(input('Digite a nota do 1° bimestre: ')))
    alunos.append(float(input('Digite a nota do 2° bimestre: ')))
    alunos.append(float(input('Digite a nota do 3° bimestre: ')))
    alunos.append(float(input('Digite a nota do 4° bimestre: ')))
    alunos.append((alunos[1]+alunos[2]+alunos[3]+alunos[4])/4)
    geral.append(alunos[:])
    alunos.clear()
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        print('Opção Inválida.')
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print('=-'*13)
print('{:^25}'.format(' MÉDIA DOS ALUNOS '))
print('-='*13)
print('{:<4}{}{:>20}'.format('Nº', 'Nome', 'Média'))
for c in range(0, len(geral)):
    print(f'{c:<2} {geral[c][0]:.<20} {geral[c][5]:.1f}')
print('=-'*13)
while True:
    opç = str(input('Deseja analisar a nota de algum aluno? [S/N] ')).strip().upper()
    while opç not in 'SN':
        print('Opção Inválida.')
        opç = str(input('Deseja analisar a nota de algum aluno? [S/N] ')).strip().upper()
    if opç == 'N':
        print('Programa Encerrado.')
        break
    n = int(input('Selecione o número correspondente ao aluno -> '))
    print(f'''{geral[n][0]}
Nota 1: {geral[n][1]}
Nota 2: {geral[n][2]}
Nota 3: {geral[n][3]}
Nota 4: {geral[n][4]}
Média final: {geral[n][3]:.1f}''')
