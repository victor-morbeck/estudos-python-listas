#Lista para armazenar os dados dos alunos
lista_dados = []  

#lista que irá armazenar as listas de alunos
banco_de_dados = []

nome = input('Digite seu nome: ').lower

#Coletando os dados
while nome != 'fim':

   
    email = input('Digite o email: ')

    n1 = float(input('Nota 1: '))

    n2 = float(input('Nota 2: '))


#Imputando os dados na lista

    lista_dados.append(nome)
    lista_dados.append(email)
    lista_dados.append(n1)
    lista_dados.append(n2)

    #Inputando dados em lisa banco de dados
    banco_de_dados.append(lista_dados)

    #Esvaziando lisa de dados dos alunos, afim de receber outra lista
    lista_dados = []

    nome = input('Digite seu nome: ')

#Exibindo a lista dados
print(banco_de_dados)