def menu(tam=60):
    print('='*tam)
    print('MENU PRINCIPAL'.center(tam))
    print('='*tam)
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastradas nova pessoa\033[m')
    print('\033[33m3\033[m - \033[34mSair do Sistema\033[m')
    print('='*tam)

    while True:
        try:
            op = str(input('Digite sua Opção:')).strip()
        except KeyboardInterrupt:
            print('\033O usuário não deseja digitar mais nada, Saindo do Sistema\033[m')
            return '3'
        else:
            if op == '1' or op == '2' or op == '3':
                return op
            else:
                print('\033[31mOpção Inválida. Digite novamente\033[m')

