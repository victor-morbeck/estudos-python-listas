listatabuadas = []
num = int(input('Coloque um número e veja sua tabuada: '))
cont = 0
for vezes in range(11):
    mult = num * cont
    cont += 1
    listatabuadas.append(mult)
print(listatabuadas)