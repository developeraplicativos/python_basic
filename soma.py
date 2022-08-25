AGENDA = {};
AGENDA['Guilherme'] = {
    'telefone':'819983233244',
    'email':'discio@gmail.com',
    'endereco':'rua nilson sabino pinnho, 322',
}

AGENDA['Maria'] = {
    'telefone':'819983231111',
    'email':'maria@gmail.com',
    'endereco':'rua dois e tres, 322',
}

def mostrar_contato():
    for contato in AGENDA:
        buscar_contato(contato)
        print('----------------------')

def buscar_contato(contato):
    print('Nome: ',contato)
    print('Telefone: ',AGENDA[contato]['telefone'])
    print('Email: ',AGENDA[contato]['email'])
    print('Endereço: ',AGENDA[contato]['endereco'])

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print('>>> contato {} adcionado com sucesso'.format(contato))

def excluir_contato(contato):
    AGENDA.pop(contato)
    print('>>> contato {} excluído com sucesso'.format(contato))

def menu():
    print('1 para incluir')
    print('2 para editar')
    print('3 para excluit')
    print('4 para buscar')
    print('5 para listar')
    print('0 para fechar')


menu()
opcao = input('escolha uma opção: ')

if opcao == '5':
    mostrar_contato()
elif opcao == '4':
    buscar_contato(input('Digite o nome do contato:'))
elif opcao == '1' or opcao == '2':
    contato = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereço: ')
    incluir_editar_contato(contato, telefone, email, endereco)
    mostrar_contato()
elif opcao == '3':
    excluir_contato(input('Digite o nome do contato: '))
elif opcao == '0':
    print('Fechando programa')
else:
    print('Opção invalida')

