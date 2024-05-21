#criar uma senha 
nome = 'Maria'
senha = 123456
tentativa = 3
while tentativa >0:
    entrada = ' Olá, seja bem-vindo ao Banco do Brasil'
    senha_digitada = int(input(" digite sua senha:   "))
    if senha_digitada == senha:
        print(f' {entrada} {nome}.')
        break
    else:
        tentativa-=1
        if  tentativa ==0:
             print(f'{nome}, sua conta foi bloqueada! Dírija-se a um de nossos caixas{tentativa}')
             break
        print(f' {nome}, sua senha está incorreta, você tem {tentativa} ')

        