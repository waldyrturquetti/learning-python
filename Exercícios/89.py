alunos = []
dados = []
notas = []


while True:
    nome = str(input('Digite o nome:')).title().strip()
    dados.append(nome)
    notas.append(int(input('Digite a nota 1:')))
    notas.append(int(input('Digite a nota 2:')))
    dados.append(notas[:])
    alunos.append(dados[:])
    print(dados)
    print(alunos)
    notas.clear()
    dados.clear()

    while True:
        op = str(input('Você deseja continuar [S/N]:')).upper().strip()[0]
        if op == 'N' or op == 'S':
            break
    
    if op == 'N' and op != 'S':
        break

print('=='*20)
print(f'{"No":<4}{"Nome":<10}{"Média":>8}')
for c in range(len(alunos)):
    print(f'{c:<4}{alunos[c][0]: <10}{sum(alunos[c][1])/2: >8.1f}')
print('=='*20)

while True:
    aluno = int(input('Mostrar as notas de qual aluno (999 para interromper):'))
    if aluno == 999:
        break

    if aluno == len(alunos) - 1:
        print(f'Notas de {alunos[aluno][0]} são {alunos[aluno][1]}')
        print('=='*20)

print('Programa Encerrado...')

