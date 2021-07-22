'''lista_numeros = [] #Declarando a lista 

opc = "sim"

maior = 0

menor = 10000

while (opc == "sim"):
    numeros = int(input('Digite números inteiros: '))
    opc = str(input('Continuar, sim / nao: '))
    lista_numeros.append(numeros)
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor =  numeros
    if opc != "sim" and opc != "nao":
        print('opcao inválida')
    print('-----------------------------------------------')

print(f'Os valores digitados foram {lista_numeros}')
print(f'O maior valor foi {maior} se o menor foi {menor}')
'''
maior = 0
menor = 0

lista_numeros = []

qattdNum = int(input('Quantos números desja adicionar? '))

for num in range(qattdNum):
    num = int(input('Número: '))
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
print(f'O maior número se encontra no index  {lista_numeros.index(maior)} da lista')
    
