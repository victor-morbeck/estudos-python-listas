
lista = []#Definindo a lista
listaImpares = []#Armazenar os números ímpares
lista_maior_dezoito = []#Armazenar valores que excedem 18

#Escopo de variáveis

resposta = 'Ss'
num = maior = menor = 0
qttdElementos = 0
qtddPares = 0
soma = 0
dezoito = 18

while resposta in "Ss":
    
    num = int(input('Digite um número: '))
    
    lista.append(num)

    #Definindo os números ímpares 
    if (num % 2) != 0:
        listaImpares.append(num)
    else:
        qtddPares += 1
    
    #Definindo maior e menor
    qttdElementos += 1
    soma += num
    
    if qttdElementos == 1:
        maior = menor = num
        
    else:

        if num > maior:
            maior = num
        if num < menor:
            menor = num
        
        #Calculando a média
        media = (soma/qttdElementos)

        #Números maiores que 18
        if num > dezoito:
            lista_maior_dezoito.append(num)

      

    resposta = input('Continuar ? S - sim / N - não : ')[0]

print('------------------------------------------------------------------------------------')
print(f'Os valores adicionados foram {lista}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor} ')
print(f'A soma dos valores é {soma}')
print(f'Os valores ímpares adicionados foram {listaImpares}' f'\nA quantidade de números pares é {qtddPares}')
print(f'Os valores maiors que 18 foram {lista_maior_dezoito}')
print(f'A média dos valores é {media}')
print('------------------------------------------------------------------------------------')