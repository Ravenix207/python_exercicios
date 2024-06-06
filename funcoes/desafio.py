# criar um progama que permita cadastra notas dos alunos
def cadastrarNotas(dic_alunos):
    aluno = input("Digite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f' Digite a {i+1}ª nota: '))
        notas.append(nota)
    dic_alunos[aluno] = notas

def calcularMedia(notas):
    media = sum(notas)/len(notas)
    return media

def statusFinal(media):
    if(media >=5 ):
        return 'Aprovado'
    else:
        return 'Reprovado' 
    
def mostrarNotas(dic_alunos):
    print(f"\nNOTAS CADASTRADAS")
    for nome_aluno, notas_aluno in dic_alunos.items():
        media = calcularMedia(notas_aluno) 
        print(f'Nome: {nome_aluno} - Notas: {notas_aluno} - Média: {media} - Status: {statusFinal(media)}')
    print('\n')

def alunosReprovados(dic_alunos):
    print(f"\nALUNOS REPROVADOS")
    for nome_aluno, notas_aluno in dic_alunos.items():
        media = calcularMedia(notas_aluno)
        if media < 5:
            print(f"Nome: {nome_aluno} - Média: {media}")
    print('\n')


# Dicionário que vai receber os alunos
alunos = {}

# Menu
while True:
    print (f'1. Cadastra alunos e notas \n'
        f'2. Mostrar notas cadastradas \n'
        f'3. Alunos Reprovados \n'
        f'0. Sair do programa \n')
    
    opcao = int(input(' Digite uma das opções: '))
    
    if opcao == 1:
        cadastrarNotas(alunos)
    elif opcao == 2:
        mostrarNotas(alunos)
    elif opcao == 3:
        alunosReprovados(alunos)
    elif opcao == 0:
        break
    else:
        print('Opção inválida')