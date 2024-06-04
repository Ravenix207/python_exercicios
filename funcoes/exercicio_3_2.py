#criar uma função


def calcularMedia(notas):
    copia = list(notas)
    copia.pop(0)
    media = sum(copia)/len(copia)
    return media

def statusFinal(media):
    if(media >=5 ):
        return 'Aprovado'
    else:
        return 'Reprovado' 
 
print(' Calculadora de Média')

aluno_notas = []
aluno_notas.append(input(' Digite o nome do aluno:'))
n = int(input(' Digite a quantidade de notas: '))
for i in range(4):
    nota = float(input(f' Digite a {i+1}ª nota: '))
    aluno_notas.append(nota)

m = calcularMedia(aluno_notas)
r = statusFinal(m)
print (f'{aluno_notas[0]} Sua média é {m}, você foi {r}')


    
