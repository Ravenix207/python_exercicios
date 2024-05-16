# Informar numeros pares e positivos
iteracao = 1
par = 0
impar = 0
while iteracao <= 5:
    n = int(input('Digite um numero: '))
    if (n % 2 == 0):
        print('O número digitado é PAR')
        par += 1
    else:
        print('O numero digitado é IMPAR')
        impar += 1
    iteracao+=1
print(f'Números par = {par}')
print(f'Número impar = {impar}')




