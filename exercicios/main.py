def main():
    

    medicos = []
    ponteiro = Menu()
    while ponteiro != 5:
        if ponteiro == 1:
            print('Menu Médicos')
            subponteiro = MenuMedicos()
            while subponteiro != 6:
                if subponteiro == 1:
                    print('Listar Todos os Médicos')
                    ListarMedicos()
                elif subponteiro == 2:
                    print('Pesquisar Médico Específico')
                    ListarMedicoEspecifico()
                elif subponteiro == 3:
                    print('Cadastrar Médico')
                    CadastroMedico()


                elif subponteiro == 4:
                    print('Alterar Cadastro')
                    AlterarCadastroMedico()
                elif subponteiro == 5:
                    print('Excluir Cadastro')
                    ExcluirCadastroMedico()

                else:
                    print('Opcão Inválida')

                subponteiro = MenuMedicos()

        if ponteiro == 2:
            print('Menu de Pacientes')
            subponteiro = MenuPacientes()
            while subponteiro != 6:
                if subponteiro == 1:
                    print('Listar Todos os Pacientes')
                    ListarPacientes()
                elif subponteiro == 2:
                    print('Pesquisar Médico Paciente Específico')
                    ListarPacienteEspecifico()
                elif subponteiro == 3:
                    print('Cadastrar Paciente')
                    CadastroPaciente()
                elif subponteiro == 4:
                    print('Alterar Cadastro')
                    AlterarCadastroPaciente()
                elif subponteiro == 5:
                    print('Excluir Cadastro')
                    ExcluirCadastroPaciente()

                else:
                    print('Opcão Inválida')

                subponteiro = MenuPacientes()
        if ponteiro == 3:
            print('Menu de Consultas')
            subponteiro = MenuConsultas()
            while subponteiro != 6:
                if subponteiro == 1:
                    print('Listar Todos os Pacientes')

                elif subponteiro == 2:

                    print('Pesquisar Médico Paciente Específico')

                elif subponteiro == 3:
                    print('Cadastrar Paciente')
                    cadastrarConsulta()
                elif subponteiro == 4:
                    print('Alterar Cadastro')

                elif subponteiro == 5:
                    print('Excluir Cadastro')


                else:
                    print('Opcão Inválida')

                subponteiro = MenuConsultas()


        ponteiro = Menu()
    print('Programa Encerrado')


def Menu():
    print('[1] Médicos')
    print('[2] Pacientes')
    print('[3] Consultas')
    print('[4] Relatórios')
    print('[5] Encerrar')
    valor = int(input('Digite o número correspondente de cada opção:' '\n'))
    return valor

def MenuMedicos():
    print('[1] Listar Médicos')
    print('[2] Listar Médico específico ')
    print('[3] Cadastrar Médico')
    print('[4] Alterar Cadastro')
    print('[5] Excluir Cadastro')
    print('[6] Sair')
    valor = int(input('Digite o número correspondente de cada opção:' '\n'))
    return valor

def MenuPacientes():
    print('[1] Listar Pacientes')
    print('[2] Listar Paciente Específico')
    print('[3] Cadastar Paciente')
    print('[4] Alterar Cadastro')
    print('[5] Excluir Cadastro')
    print('[6] Sair')
    valor = int(input('Digite o número correspondente de cada opção:' '\n'))
    return valor

def MenuConsultas():
    print('[1] Listar Consultas')
    print('[2] Listar Consulta Específica')
    print('[3] Cadastar Consulta')
    print('[4] Alterar Cadastro')
    print('[5] Excluir Cadastro')
    print('[6] Sair')
    valor = int(input('Digite o número correspondente de cada opção:' '\n'))
    return valor 
def CadastrarConsultas():
    pacientes = CarregaArquivoPaciente
    medicos = CarregaArquivoMedico
    consultas = CarregaArquivoConsultas
    crm = int(input('Digite o CRM: '))
    #if VerificaCodigo(crm, medicos):
        return False
        cpf = int(input('Digite seu cpf: '))
        if VerificaCodigo(cpf, pacientes):
            return False
            data = input('Data xx/xx/xxxx'):
             ##if VerificaCodigo(data, consultas): 


        
    




def CadastroMedico():
    medico =[]
    medicos = CarregaArquivoMedico()
    cadastro = input('Digite o CRM do médico ou tecle ENTER para sair')
    while cadastro != '':
        valor = VerificaCodigo(cadastro,medicos)
        if valor == False:
            print('Esse Código já foi cadastrado')
        else:
            medico.append(cadastro)
            medico.append(input('Digite o nome do médico'))
            medico.append(input('Digite a data de nascimento ''xx/xx/xxx'))
            medico.append(input('Digite a especialidade'))
            medico.append(input('Digite em qual Instituição se formou'))
            medico.append(input('Digite o E-mail'))
            medico.append(input('Digite o Telefone'))
        medicos.append(medico)
        medico =[]

        AtualizarArquivoMedico(medicos)


        cadastro = input('Digite o CRM do médico ou tecle ENTER para sair')

def ListarMedicos():
    medicos = CarregaArquivoMedico()
    for medico in medicos:
        print('Código:', medico[0])
        print('Nome:', medico[1])
        print('Data de Nascimento:', medico[2])
        print('Especialidade:', medico[3])
        print('Instituição de Formação:', medico[4])
        print('E-mail:', medico[5])
        print('Telefone:', medico[6])
        print('----------------------------')

def ListarMedicoEspecifico():
    medicos = CarregaArquivoMedico()
    crm = input('Digite o CRM do médico que deseja procurar:')
    for c in range(len(medicos)):
            if crm == medicos[c][0]:
                print('Código:', medicos[c][0])
                print('Nome:', medicos[c][1])
                print('Data de Nascimento:',medicos[c][2])
                print('Especialidade:', medicos[c][3])
                print('Instituição de Formação:', medicos[c][4])
                print('E-mail:', medicos[c][5])
                print('Telefone:', medicos[c][6])
                print('----------------------------')
                return c
            else:
                print('Cadastro não Encontrado')

def AlterarCadastroMedico():
    medicos = CarregaArquivoMedico()
    ListarMedicos()
    crm = input('Digite o CRM do médico que deseja alterar dados')
    for c in range(len(medicos)):

                    if crm == medicos[c][0]:
                        print(f'[1]Código:', medicos[c][0])
                        print(f'[2]Nome:', medicos[c][1])
                        print(f'[3]Data de Nascimento:', medicos[c][2])
                        print(f'[4]Especialidade:', medicos[c][3])
                        print(f'[5]Instituição de Formação:', medicos[c][4])
                        print(f'[6]E-mail:', medicos[c][5])
                        print(f'[7]Telefone:', medicos[c][6])
                        print('----------------------------')
                        valor = int(input('Digite a opção correspondente ao dado que deseja alterar:'))
                        if valor == 1:
                            del medicos[c][0]

                            cod = input('Digite o novo CRM')
                            val = VerificaCodigo(cod,medicos)
                            if val == True:
                                medicos[c].insert(0, cod)
                                print('Alterado com Sucesso')
                            else:
                                print('Código Existente')
                        elif valor ==2:
                            del medicos[c][1]
                            nome = input('Digite o novo Nome')
                            medicos[c].insert(1, nome)
                            print('Alterado Com Sucesso')
                        elif valor ==3:
                            del medicos[c][2]
                            data = input('Insira a nova data de nascimento')
                            medicos[c].insert(2, data)
                            print('Alterado com Sucesso')
                        elif valor ==4:
                            del medicos[c][3]
                            esp = input('Insira a nova Especialidade')
                            medicos[c].insert(3, esp)
                            print('Alterado com Sucesso')
                        elif valor ==5:
                            del medicos[c][4]
                            it = input('Insira a nova Instituição de Formação')
                            medicos[c].insert(4, it)
                            print('Alterado com Sucesso')
                        elif valor ==6:
                            del medicos[c][5]

                            email = input('Insira o novo E-mail:')
                            medicos[c].insert(5, email)
                        elif valor ==7:
                            del medicos[c][6]
                            tel = input('Insira o novo Telefone:')
                            medicos[c].insert(6, tel)
                        else:
                            print('Opção inválida')


                        AtualizarArquivoMedico(medicos)
def ExcluirCadastroMedico():
    medicos = CarregaArquivoMedico()
    ListarMedicos()
    crm = input('Digite o CRM do médico que deseja excluir do bando de dados')
    for c in range(len(medicos)):
        if crm == medicos[c][0]:
            print(f'[1]Código:', medicos[c][0])
            print(f'[2]Nome:', medicos[c][1])
            print(f'[3]Data de Nascimento:', medicos[c][2])
            print(f'[4]Especialidade:', medicos[c][3])
            print(f'[5]Instituição de Formação:', medicos[c][4])
            print(f'[6]E-mail:', medicos[c][5])
            print(f'[7]Telefone:', medicos[c][6])
            print('----------------------------')

            ponteiro = input('Deseja Excluir Esse Cadastro?''\n''Tecle 1 para SIM e 2 para NÃO''\n')
            if ponteiro == '1':
                del medicos[c]
                AtualizarArquivoMedico(medicos)
                print('Cadastro Excluído')

            else:
                print('Voltando ao Menu')
            return c
        else:
            print('CRM não Encontrado')
def CadastroPaciente():
    paciente = []
    pacientes = CarregaArquivoPaciente()
    cadastro = input('Digite o CPF do paciente ou tecle ENTER para sair')
    while cadastro != '':
        valor = VerificaCodigo(cadastro,pacientes)
        if valor == False:
            print('Esse Código já foi cadastrado')
        else:
            paciente.append(cadastro)
            paciente.append(input('Digite o nome do paciente'))
            paciente.append(input('Digite a data de nascimento ''xx/xx/xxx'))
            paciente.append(input('Digite o sexo'))
            paciente.append(input('Digite o plano de Saúde'))
            paciente.append(input('Digite o E-mail'))
            paciente.append(input('Digite o Telefone'))
        pacientes.append(paciente)
        paciente =[]

        AtualizarArquivoPaciente(pacientes)


        cadastro = input('Digite o CPF do paciente ou tecle ENTER para sair')

def ListarPacientes():
    pacientes = CarregaArquivoPaciente()
    for paciente in pacientes:
        print('Código:', paciente[0])
        print('Nome:', paciente[1])
        print('Data de Nascimento:', paciente[2])
        print('Sexo:', paciente[3])
        print('Plano de Saúde:', paciente[4])
        print('E-mail:', paciente[5])
        print('Telefone:', paciente[6])
        print('----------------------------')

def ListarPacienteEspecifico():
    pacientes = CarregaArquivoPaciente()
    cpf = input('Digite o CPF do paciente que deseja procurar:')
    for c in range(len(pacientes)):
            if cpf == pacientes[c][0]:
                print('Código:', pacientes[c][0])
                print('Nome:', pacientes[c][1])
                print('Data de Nascimento:',pacientes[c][2])
                print('Sexo:', pacientes[c][3])
                print('Plano de Saúde:', pacientes[c][4])
                print('E-mail:', pacientes[c][5])
                print('Telefone:', pacientes[c][6])
                print('----------------------------')
                return c
            else:
                print('Cadastro não Encontrado')

def AlterarCadastroPaciente():
    pacientes = CarregaArquivoPaciente()
    ListarPacientes()
    cpf = input('Digite o CPF do paciente que deseja alterar dados')
    for c in range(len(pacientes)):

                    if cpf == pacientes[c][0]:
                        print(f'[1]Código:', pacientes[c][0])
                        print(f'[2]Nome:', pacientes[c][1])
                        print(f'[3]Data de Nascimento:', pacientes[c][2])
                        print(f'[4]Sexo:', pacientes[c][3])
                        print(f'[5]Plano de Saúde:', pacientes[c][4])
                        print(f'[6]E-mail:', pacientes[c][5])
                        print(f'[7]Telefone:', pacientes[c][6])
                        print('----------------------------')
                        valor = int(input('Digite a opção correspondente ao dado que deseja alterar:'))
                        if valor == 1:
                            del pacientes[c][0]

                            cod = input('Digite o novo CPF')
                            val = VerificaCodigo(cod,pacientes)
                            if val == True:
                                pacientes[c].insert(0, cod)
                                print('Alterado com Sucesso')
                            else:
                                print('Código Existente')
                        elif valor ==2:
                            del pacientes[c][1]
                            nome = input('Digite o novo Nome')
                            pacientes[c].insert(1, nome)
                            print('Alterado Com Sucesso')
                        elif valor ==3:
                            del pacientes[c][2]
                            data = input('Insira a nova data de nascimento')
                            pacientes[c].insert(2, data)
                            print('Alterado com Sucesso')
                        elif valor ==4:
                            del pacientes[c][3]
                            esp = input('Insira o Sexo')
                            pacientes[c].insert(3, esp)
                            print('Alterado com Sucesso')
                        elif valor ==5:
                            del pacientes[c][4]
                            it = input('Insira o novo Plano de Saúde:')
                            pacientes[c].insert(4, it)
                            print('Alterado com Sucesso')
                        elif valor ==6:
                            del pacientes[c][5]

                            email = input('Insira o novo E-mail:')
                            pacientes[c].insert(5, email)
                        elif valor ==7:
                            del pacientes[c][6]
                            tel = input('Insira o novo Telefone:')
                            pacientes[c].insert(6, tel)
                        else:
                            print('Opção inválida')


                        AtualizarArquivoPaciente(pacientes)
def ExcluirCadastroPaciente():
    pacientes = CarregaArquivoPaciente()
    ListarPacientes()
    cpf = input('Digite o CPF do paciente que deseja excluir do banco de dados')
    for c in range(len(pacientes)):
        if cpf == pacientes[c][0]:
            print(f'[1]Código:', pacientes[c][0])
            print(f'[2]Nome:', pacientes[c][1])
            print(f'[3]Data de Nascimento:', pacientes[c][2])
            print(f'[4]Sexo:', pacientes[c][3])
            print(f'[5]Plano de Saúde:', pacientes[c][4])
            print(f'[6]E-mail:', pacientes[c][5])
            print(f'[7]Telefone:', pacientes[c][6])
            print('----------------------------')

            ponteiro = input('Deseja Excluir Esse Cadastro?''\n''Tecle 1 para SIM e 2 para NÃO''\n')
            if ponteiro == '1':
                del pacientes[c]
                AtualizarArquivoPaciente(pacientes)
                print('Cadastro Excluído')

            else:
                print('Voltando ao Menu')
            return c
        else:
            print('CRM não Encontrado')





def VerificaCodigo(codigo,lista):
    for c in lista:
        if codigo == c[0]:
            return False
        else:
            return True

def CarregaArquivoMedico():

    import os
    if not os.path.isfile('medicos.txt'):
        arquivo = open('medicos.txt', 'w')
        arquivo.close()

    arquivo = open('medicos.txt', 'r')
    medicos = []

    for linha in arquivo:
        medico = linha.replace('\n','')
        medico = medico.split(';')

        medicos.append(medico)
    arquivo.close()

    return medicos
def AtualizarArquivoMedico(medicos):

    arquivo = open('medicos.txt', 'w')


    for c in range(len(medicos)):
        linha = ''

        for i in range(len(medicos[c])):
            linha += medicos[c][i] + ';'

        linha = linha[:-1] + '\n'
        arquivo.write(linha)
    arquivo.close()
def CarregaArquivoPaciente():

    import os
    if not os.path.isfile('pacientes.txt'):
        arquivo = open('pacientes.txt', 'w')
        arquivo.close()

    arquivo = open('pacientes.txt', 'r')
    pacientes = []

    for linha in arquivo:
        paciente = linha.replace('\n','')
        paciente = paciente.split(';')

        pacientes.append(paciente)
    arquivo.close()

    return pacientes
def AtualizarArquivoPaciente(pacientes):

    arquivo = open('pacientes.txt', 'w')


    for c in range(len(pacientes)):
        linha = ''

        for i in range(len(pacientes[c])):
            linha += pacientes[c][i] + ';'

        linha = linha[:-1] + '\n'
        arquivo.write(linha)
    arquivo.close()

def conferirSeExiste(dados, lista):
        for dados in lista:
            if dados in lista:
                return True
            else:
                return False

    # Função para o cadastramento de consultas

def cadastrarConsulta(pacientes, medicos, lista):
        con = []
        crm = int(input('CRM: '))

        if conferirSeExiste(pacientes, medicos):
            return False
            cpf = int(input('CPF: '))
            if conferirSeExiste(pacientes, medicos):
                return False
            else:
                print("PACIENTE NAO CADASTRADO!")
        else:
            ('MEDICO NAO CADASTRADO!')
            data = input('Data: ')
            if conferirSeExiste(con):
                return False
                hora = input('Hora: ')
                if conferirSeExiste(con):
                    return False
                else:
                    print("Horário não disponível")
            else:
                print('Data não disponível')

#Programa Principal:


#Programa Principal:
print('Bem vindo ao Sistema de Dados do Hospital São Carlos!')
main()