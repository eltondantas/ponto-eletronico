import menu

print('-----------------------------------------------\n'+
      'Bem-vindo ao Sistema de Funcionários da Empresa\n'+
      '-----------------------------------------------\n')

while True:

  menu.exibir_opcoes()
  print()

  match menu.selecionar_opcao():
    case '0':
      print('_'*80)
      print('\nSistema encerrado.')
      break
    case '1':
      if menu.cadastrar_funcionario():
        print('\nFuncionário cadastrado com sucesso!')
      else:
        print('\nFuncionário não cadastrado.')
      print('\n'+'_'*80+'\n')
    case '2':
      if menu.remover_func() :
        print('\nFuncionário removido com sucesso!')
      else:
        print('\nFuncionário não removido.')
      print('\n'+'_'*80+'\n')
    case '3':
      print('\nAtualizar funcionário')
      if menu.atualizar_func():
        print('\nFuncionário atualizado com sucesso!')
      else:
        print('\nFuncionário não atualizado.')
      print('\n'+'_'*80+'\n')
    case '4':
      menu.relacao_func()
      print('\n'+'_'*80+'\n')
    case '5':
      print('\n Filtrar funcionário')
      menu.filtrar_func()
      print('\n'+'_'*80+'\n')
    case '6':
      print('\n Abrir ponto')
      if menu.abrir_ponto():
        print('\nAbertura de ponto realizada com sucesso!')
      else:
        print('\nAbertura de ponto não realizada.')
      print('\n'+'_'*80+'\n')
    case '7':
      print('\n Fechar ponto')
      if menu.fechar_ponto():
        print('\nFechamento de ponto realizado com sucesso!')
      else:
        print('\nFechamento de ponto não realizado.')
      print('\n'+'_'*80+'\n')
    case '8':
      print('\n Cadastrar funcionário')
      menu.zerar_ponto()
      print('\n'+'_'*80+'\n')