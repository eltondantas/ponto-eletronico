# Funções que podem ser utilizadas mais de uma vez ao longo do código
import menu

# Checa se um nome é válido e imprime aviso quando não
def is_nome_valid(nome):
  if not nome.replace(' ','').isalpha():
    print('\nNome inválido! O nome deve ter apenas letras.')
    return False
  elif len(nome.split(' ')) < 2:
    print('\nNome inválido! O funcionário deve ter nome e sobrenome.')
    return False
  else:
    return True

# Checa se um CPF é válido e imprime aviso quando não
def is_cpf_valid(cpf):
  if not cpf.isdigit():
    print('\nCPF inválido! O CPF deve conter apenas dígitos.')
    return False
  elif len(cpf) != 11:
    print('\nCPF inválido! O CPF deve conter 11 dígitos.')
    return False
  else:
    return True

# Checa se um CPF já foi cadastrado
def check_cpf(cpf):
  for i in menu.F:
    if cpf in i:
      print('\nCPF Inválido! O CPF já foi cadastrado.')
      return False
    else:
      return True

# Checa se data e hora são válidas


# Formata CPF no formato XXX.XXX.XXX-XX
def formatar_cpf(cpf):
  return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'


# Calcula o tempo de expediente
# Retorna uma tupla de dois inteiros referentes a horas e minutos
from datetime import datetime
def tempo_expediente(t1,t2):
  tempo = str(datetime.strptime(t2,'%d/%m/%Y %H:%M') - datetime.strptime(t1,'%d/%m/%Y %H:%M'))
  tempo = tempo.split(':')
  tempo = (int(tempo[0]),int(tempo[1]))
  return tempo