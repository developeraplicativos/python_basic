AGENDA = {};
# AGENDA['Guilherme'] = {
#     'telefone':'819983233244',
#     'email':'discio@gmail.com',
#     'endereco':'rua nilson sabino pinnho, 322',
# }
#
# AGENDA['Maria'] = {
#     'telefone':'819983231111',
#     'email':'maria@gmail.com',
#     'endereco':'rua dois e tres, 322',
# }

def mostrar_contato():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print('----------------------')
    else:
        print('agenda vazia')

def buscar_contato(contato):
    try:
        print('Nome: ', contato)
        print('Telefone: ', AGENDA[contato]['telefone'])
        print('Email: ', AGENDA[contato]['email'])
        print('Endereço: ', AGENDA[contato]['endereco'])
    except KeyError:
        print('Contato inexistente ')
    except Exception:
        print('Algum erro aconteceu')

def lerEntrada():
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereço: ')
    return telefone,email,endereco

def incluir_editar_contato(contato,telefone,email,endereco):
    try:
        AGENDA[contato]
        print('editando : ', contato + '--------------------------')
    except:
        print('inserindo : ', contato + '--------------------------')

    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print('>>> contato {} adcionado com sucesso'.format(contato))

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print('>>> contato {} excluído com sucesso'.format(contato))
    except KeyError:
        print('Contato inexistente')
    except Exception:
        print('Algum erro aconteceu')

def menu():
    print('1 para incluir')
    print('2 para editar')
    print('3 para excluit')
    print('4 para buscar')
    print('5 para listar')
    print('6 para exportar')
    print('7 para importar')
    print('0 para fechar')

def exportCSV():
    with open('agenda.csv', 'w') as file:
        file.write('nome;telefone;email;endereco\n')
        for contato in AGENDA:
            telefone = AGENDA[contato]['telefone']
            email = AGENDA[contato]['email']
            endereco = AGENDA[contato]['endereco']
            file.write("{};{};{};{}\n".format(contato,telefone,email,endereco))
    print('agenda salva com sucesso')

def importarCSV(path):
    try:
        with open(path, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')
                contato = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(contato, telefone, email, endereco)
    except Exception as error:
        print('ocorreu um erro: ')
        print(error)


while True:
    menu()
    opcao = input('escolha uma opção: ')

    if opcao == '5':
        mostrar_contato()

    elif opcao == '4':
        buscar_contato(input('Digite o nome do contato:'))

    elif opcao == '1' or opcao == '2':
        contato = input('Digite o nome: ')
        telefone,email,endereco = lerEntrada()
        incluir_editar_contato(contato,telefone,email,endereco )
    elif opcao == '7':
        path = input('digite o path do arquivo: ')
        importarCSV(path)
    elif opcao == '6':
        exportCSV()
    elif opcao == '3':
        excluir_contato(input('Digite o nome do contato: '))
    elif opcao == '0':
        print('Fechando programa')
        break
    else:
        print('Opção invalida')
