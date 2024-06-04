# criar um progama que permita cadastra notas dos alunos
def cadastrarNotas(dic_alunos):
    aluno = input("Digite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f' Digite a {i+1}ª nota: '))
        notas.append(nota)
    dic_alunos[aluno] = notas

# Dicionário que vai receber os alunos
alunos = {}

# Menu
while True:
    print (f'1. Cadastra alunos e notas \n'
        f'2. Mostrar notas cadastradas \n'
        f'3. Sair do programa \n')
    
    opcao = int(input(' Digite uma das opções: '))
    
    if opcao == 1:
        cadastrarNotas(alunos)
    elif opcao == 2:
        print('Fazer função para mostrar as notas')
    elif opcao == 3:
        break
    else:
        print('Opção inválida')