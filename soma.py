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

def incluir_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print('>>> contato {} adcionado com sucesso'.format(contato))

mostrar_contato()
incluir_contato('emerson','816223223','jaja@hotmail.com','rua alberto pereira')
mostrar_contato()

#buscar_contato('Maria');
