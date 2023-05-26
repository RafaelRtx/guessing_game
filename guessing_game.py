import random

def number_guess_game():
  random_number = random.randint(1, 10)
  print(random_number)
  attempts = 0

  print('Bem vindo ao jogo de adivinhação de números!')
  print('Estou pensando em um número de 1 a 10!')

  while True:
    attempt = int(input('Estou pensando em um número entre 1 e 10. Adivinhe! '))
    attempts += 1
    

    if attempt < random_number:
      print('Um pouco mais...')
    elif attempt > random_number:
      print('Um pouco menos...')
    else:
      print (f"Parabéns! Você acertou o número em {attempts} tentativa(s)!")
      break

number_guess_game()


    