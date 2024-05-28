produtos = {}

# O usuário deve informar os produtos aqui...
num_itens = int(input('Digite a quantidade de itens: '))

for i in range(num_itens):
    produto = input('Digite o produto: ')
    valor = float(input('Digite o valor do produto: '))
    quantidade = int(input('Digite a quantidade: '))
    produtos.update({i : [produto,valor,quantidade]})    

total = 0

print(50 * '-')
print(' Carrinho de Compras')
print(50 * '-')

for cod, prod in produtos.items():
    subtotal = prod[1] * prod[2]
    print(f'{prod[0]} - R$ {prod[1]:.2f} - {prod[2]} un - R$ {subtotal:.2f}')
    total += subtotal

print(50 * '-')
print(f'Total da compra: R$ {total:.2f}')
print(50 * '-')    