import auxiliares as aux

# Exibe as opções do menu
def exibir_opcoes():
  print('1 - Cadastrar funcionário\n'+
        '2 - Remover funcionário\n'+
        '3 - Atualizar dados de funcionário\n'+
        '4 - Exibir funcionários\n'+
        '5 - Pesquisar funcionário\n'+
        '6 - Abrir ponto de funcionário\n'+
        '7 - Fechar ponto de funcionário\n'+
        '8 - Zerar ponto de funcionário\n'+
        '0 - Sair do sistema')

# Seleciona uma opção do menu
def selecionar_opcao():
  while True:
    opcao = input('Escolha uma opção: ')
    if opcao not in ['0','1','2','3','4','5','6','7','8']:
      print('Opção inválida!')
    else:
      return opcao

# F: Matriz de funcionários da empresa
# Coluna 0: NOME | Coluna 1: CPF | Coluna 2: Hora de Entrada | Coluna 3: Hora de Saída
F = []

# 1) CADASTRAR FUNCIONÁRIO
def cadastrar_funcionario():
  print('\nCadastrar funcionário')
  print('Digite \'sair\' para voltar ao menu.')
  nome = input('Digite o nome completo do funcionário: ')
  if nome.lower() == 'sair':
    return False
  elif not aux.is_nome_valid(nome):
    return False
  else:
    cpf = input('Digite o CPF do funcionário (somente dígitos): ')
    if cpf.lower() == 'sair':
      return False
    elif not aux.is_cpf_valid(cpf):
      return False
    elif aux.check_cpf(cpf):
      return False
    else:
      F.append([nome, cpf, None, None])
      return True

# 2) REMOVER FUNCIONÁRIO
def remover_func():
  print('\nRemover funcionário')
  print('Digite \'sair\' para voltar ao menu.')
  cpf = input('Digite o CPF do funcionário (somente dígitos): ')
  if cpf.lower() == 'sair':
    return False
  elif not aux.is_cpf_valid(cpf):
    return False
  for i in F:
    if cpf in i:
      F.remove(i)
      return True
    else:
      continue
  print('\nCPF não encontrado.')
  return False

# 3) ATUALIZAR FUNCIONÁRIO
def atualizar_func():
  print('\nAtualizar dados do funcionário:')
  print('Digite \'sair\' para voltar ao menu.')
  cpf = input('Digite o CPF do funcionário (somente dígitos): ')
  if cpf.lower() == 'sair':
    return False
  elif not aux.is_cpf_valid(cpf):
    return False
  for i in F:
    if cpf in i:
      print('Nome: '+i[0]+'\nCPF: '+i[1])
      nome = input('Digite o novo nome completo do funcionário: ')
      if nome.lower() == 'sair':
        return False
      elif not aux.is_nome_valid(nome):
        return False
      else:
        cpf = input('Digite o novo CPF do funcionário (somente dígitos): ')
        if cpf.lower() == 'sair':
          return False
        elif not aux.is_cpf_valid(cpf):
          return False
        elif aux.check_cpf(cpf):
          return False

        i[1] = input('Digite o novo nome do funcionário: ')
      return True
    else:
      continue
  print('\nCPF não encontrado.')
  return False

# 4) VISUALIZAR FUNCIONÁRIOS
# Exibe a relação de todos os funcionarios
def relacao_func():
  print('Relação de Funcionários:')
  for i in F:
    print('\n- ' + i[0] +
          '\n   CPF: ' + aux.formatar_cpf(i[1]))
    if i[2] == None:
      print('   Sem informações sobre ponto eletrônico.')
      continue
    else:
      print('   Abertura do ponto às: ' + i[2])
    if i[3] == None:
      continue
    else:
      print('   Fechamento do ponto às: ' + i[3] +
            '\n   Tempo de expediente: %d hora(s) %d minuto(s)' % aux.tempo_expediente(i[2],i[3]))

# 5) FILTRAR FUNCIONÁRIO
# Filtra funcionário por nome
def filtrar_func():
  nome = input('Digite o nome do funcionário: ')
  cont = 0
  for i in F:
    if nome.lower() in i[0].lower():
      print('\n- ' + i[0] +
            '\n   CPF: ' + aux.formatar_cpf(i[1]))
      if i[2] == None:
        print('   Sem informações sobre ponto eletrônico.')
        continue
      else:
        print('   Abertura do ponto às: ' + i[2])
      if i[3] == None:
        continue
      else:
        print('   Fechamento do ponto às: ' + i[3] +
              '\n   Tempo de expediente: %d hora(s) %d minuto(s)' % aux.tempo_expediente(i[2],i[3]))
    else:
      cont += 1

  if cont == len(F):
    print('\nNenhum resultado encontrado.')

# 6) ABRIR PONTO ELETRÔNICO
# Abre o ponto de um funcionário pelo seu CPF
def abrir_ponto():
  cpf = input('Digite o CPF do funcionário (somente dígitos): ')
  if not aux.is_cpf_valid(cpf):
    return False

  for i in F:
    if cpf in i:
      if i[2] == None:
        i[2] = input('Digite a data (dd/mm/aaaa) e hora (hh:mm) de abertura: ')
        return True
      else:
        print('O ponto do funcionário já foi aberto.')
        return False
    else:
      continue

  print('CPF não encontrado.')
  return False

# 7) FECHAR PONTO ELETRÔNICO
# Fecha o ponto de um funcionário pelo seu CPF
def fechar_ponto():
  cpf = input('Digite o CPF do funcionário (somente dígitos): ')
  if not aux.is_cpf_valid(cpf):
    return False

  for i in F:
    if cpf in i:
      if i[2] == None:
        print('O ponto do funcionário não foi aberto.')
        return False
      if i[3] == None:
        i[3] = input('Digite a data (dd/mm/aaaa) e hora (hh:mm) de fechamento: ')
        return True
      else:
        print('O ponto do funcionário já foi fechado.')
        return False
    else:
      continue

  print('CPF não encontrado.')
  return False

# 8) Zera informações de horários do ponto eletrônico
def zerar_ponto():
  for i in F:
    i[2] = i[3] = None
  print('Informações de ponto eletrônico apagadas com sucesso!')