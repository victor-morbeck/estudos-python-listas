
maior = 0
menor = 0

lista_numeros = []

qattdNum = int(input('Quantos números desja adicionar? '))
for num in range(qattdNum):
    num = float(input('Número: '))
    lista_numeros.append(num)
    maior = lista_numeros[0]
    menor = lista_numeros[0]

    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(lista_numeros)
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
print(f'O menor número se encontra no index  {lista_numeros.index(menor)} da lista')
    
