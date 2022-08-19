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
        print( AGENDA[contato] )


mostrar_contato();