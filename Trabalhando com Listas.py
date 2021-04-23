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
