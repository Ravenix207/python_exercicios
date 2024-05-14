# Calculo de grandezas
print(f'Calcule de grandezas eletricas\n')
print(f'1. Tensão(em Volt)\n'
      f'2. Resistencia(em Ohm)\n' 
      f'3.  Corrente(em Ampére)\n')
opcao = int(input(' Digite a opção: '))
if opcao == 1:
    R = float(input('Digite a resistencia: '))
    i = float(input('Digite a corrente: '))
    U=R*i
    print(f'tensão = {U}V')
elif opcao == 2:
    U = float(input(' Digite a Tensão: '))
    i = float(input(' Digite a corrente: '))
    R=U/i
    print(f'Resistencia = {R}')
elif opcao == 3:
    U = float(input(' Digite a Tensão: '))
    R = float(input(' Digite a resistencia: '))
    i=U/R
    print(f'Corrente = {i}')
else:
    print(f'opção invalida')