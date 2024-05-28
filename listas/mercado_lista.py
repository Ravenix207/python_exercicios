lista_compras = []

num_itens = int(input('Digite a quantidade de itens: '))

for i in range(num_itens):
    produto = input('Digite o produto: ')
    quantidade = int(input('Digite a quantidade: '))
    lista_compras.append([produto, quantidade])

print('Lista de Compra')
for produto, quantidade in lista_compras:
    print(f"{produto} --> {quantidade}")

