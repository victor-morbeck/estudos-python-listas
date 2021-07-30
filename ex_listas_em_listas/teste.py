#Criar uma tabuada do número que eu desejar
num = int(input('Digite um número e veja sua tabuada: '))
contador = 0
for repeticoes in range(1, 11):
    mul = num * repeticoes
    contador += 1
    print(f'{num} x {contador} = {mul}')