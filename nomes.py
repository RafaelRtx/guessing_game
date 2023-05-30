nome = input('Digite o seu nome: ')
idade = input('digite sua idade: ')

nome_length = len(nome)
 
if nome and idade:
  print(f'Seu nome é: {nome}')
  print(f'Seu nome invertido é: {nome[::-1]}')

  if ' ' in nome:
   print('Seu nome contem espaços')
  else:
   print('Seu nome não contém espaços')

  if ' ' in nome:
   nome_length -= 1
   print(f'Seu nome tem {nome_length} letras')
  
  print(f'A primeira letra do seu nome é {nome[0]}')
  print(f'A última letra do seu nome é: {nome[-1]}')
else:
 print('Você não digitou os dados requeridos')