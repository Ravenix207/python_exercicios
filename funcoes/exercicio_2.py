#criar uma função
def calcularMedia(n1,n2,n3,n4):
    media = (n1+n2+n3+n4)/4
    return media

def statusFinal(media):
    if(media >=5 ):
        return 'Aprovado'
    else:
        return 'Reprovado'

print(' Calculadora de Média')
n1 = float(input(' Digite a 1ª nota: '))
n2 = float(input(' Digite a 2ª nota: '))
n3 = float(input(' Digite a 3ª nota: '))
n4 = float(input(' Digite a 4ª nota: '))
m = calcularMedia(n1,n2,n3,n4)
r = statusFinal(m)
print (f' Sua média é {m}, você foi {r}')


    
