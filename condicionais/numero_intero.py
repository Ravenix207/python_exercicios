# Informar um número inteiro e positivo
n = int(input(" Digite quantos números deseja calcular a média: "))
soma = 0
iteracao = 1
while iteracao <= n:
    num = int(input(f" Digite o {iteracao}º numero:"))
    soma += num
    iteracao += 1
print(f" A média é {soma/n}")    


