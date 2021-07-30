#Lista para armazenar os dados dos alunos
lista_dados = []  

#lista que irá armazenar as listas de alunos
banco_de_dados = []

nome = input('Digite seu nome: ')

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

    #Inputando lista em lista banco de dados
    banco_de_dados.append(lista_dados)

    #Esvaziando lisa de dados dos alunos, afim de receber outra lista
    lista_dados = []

    nome = input('Digite seu nome: ')

#Exibindo a lista dados de outro jeito
for alunos in (banco_de_dados):
    print('----------------------------------------')
    print('Nome: ',   alunos[0])
    print('E-mail: ', alunos[1])
    print('Nota-1: ', alunos[2])
    print('Nota-2: ', alunos[3])

#Econtrando um aluno na lista
achou = 'Não'

procuraAluno = input('Digite o nome de um aluno: ')

for aluno in (banco_de_dados):
    if procuraAluno == aluno[0]:
        print('Aluno encontrado')
        print(aluno)
        achou = 'sim'
    
if achou == 'não':
    print('Aluno não encontrado')
    
