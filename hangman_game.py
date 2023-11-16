import os
import random
import time
from functools import reduce


def logo_hangman():
    print('''

    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   █   █   █████   █   █   █████   █   █   █████   █   █   ║
    ║   █   █   █   █   ██  █   █       ██ ██   █   █   ██  █   ║
    ║   █████   █████   █ █ █   █████   █ █ █   █████   █ █ █   ║
    ║   █   █   █   █   █  ██   █   █   █   █   █   █   █  ██   ║
    ║   █   █   █   █   █   █   █████   █   █   █   █   █   █   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
''')


def image_hangman():
    die0 = '''













'''
    die1 = '''







        _____________
      /             /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die2 = '''
          ╔
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die3 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die4 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die5 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die6 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die7 = '''
          ╔═════╦  
          ║
          ║
          ║    ─┼─
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die8 = '''
          ╔═════╦  
          ║
          ║
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die9 = '''
          ╔═════╦  
          ║
          ║     @
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die10 = '''
          ╔═════╦  
          ║     │
          ║     @       ¡AHORCADO!
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    win = '''
          ╔═════╦  
          ║
          ║     
          ║
          ║              ¡GANASTE!
          ║
          ║                  
        __║__________        @
      /   ║         /|     └─┼─┘  
     /____________ / |       │
    |             | /       / '''+chr(92)+'''
    |_____________|/       d   b

'''
    deaths = {0: die0, 1: die1, 2: die2, 3: die3, 4: die4, 5: die5, 6: die6, 7: die7, 8: die8, 9: die9, 10: die10, 11: win}
    return deaths

# Clear Screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_word(file_path):
    word_li = []
    with open(file_path, 'r', encoding='utf-8') as data_words:
        word = random.choice([word.strip().upper() for word in data_words])
    for letter in word:
        if letter == 'Á':
            letter = 'A'
        elif letter == 'É':
            letter = 'E'
        elif letter == 'Í':
            letter = 'I'
        elif letter == 'Ó':
            letter = 'O'
        elif letter == 'Ú':
            letter = 'U'
        word_li.append(letter)
    return ''.join(word_li)

def initialize_game(word, dict_word, discovered, deaths, letters, file_path):
    word = read_word(file_path)
    dict_word = {i[0] : i[1] for i in enumerate(word)}
    discovered = ['- ' for i in range (len(dict_word))]
    deaths = 0
    letters = ['A','B','C','D','E','F','G','H',
               'I','J','K','L','M','N','O','P',
               'Q','R','S','T','U','V','W','X',
               'Y','Z']
    return word, dict_word, discovered, deaths, letters

def compare_letter(letter, dict_word, discovered, fail):
    for l in range(len(dict_word)):
        if dict_word.get(l) == letter:
            discovered[l] = letter + ' '
            fail = False
    return discovered, fail

def refresh(hangman_deaths,deaths,letters):
    clear_screen()
    logo_hangman()
    print('Letras faltantes: '+"  ".join(letters))
    print(hangman_deaths.get(deaths))

def run_game(file_name='data.txt'):
    file_path = os.path.join('./archivos', file_name)
    hangman_deaths = image_hangman()
    word = ''
    dict_word = {}
    discovered = []
    deaths = 0
    letters = []
    non_letter = 0
    word, dict_word, discovered, deaths, letters = initialize_game(word, dict_word, discovered, deaths, letters, file_path)
    while True:
        refresh(hangman_deaths,deaths,letters)
        if non_letter == 1:
            print('Debes ingresas una de las letras faltantes')
            non_letter = 0
        try:
            letter = input('''¡Adivina la palabra!     '''+ ''.join(discovered) +'''
Ingresa una letra: ''').upper()
            letters[letters.index(letter)] = ''
        except ValueError:
            non_letter = 1
        fail = True
        discovered,fail = compare_letter(letter, dict_word, discovered, fail)
        if fail == True:
            deaths += 1
            if deaths == 10:
                refresh(hangman_deaths,deaths,letters)
                print('¡Perdiste! La palabra era ' + word)
                again = input('¿Quieres jugar otra vez? (1-Si 0-No):  ')
                if again == '1':
                    word, dict_word, discovered, deaths, letters = initialize_game(word, dict_word, discovered, deaths, letters, file_path)
                    continue
                else:
                    print('Gracias por jugar :)')
                    break
        if ''.join(discovered).replace(' ','') == word:
            refresh(hangman_deaths,11,letters)
            print('Tuviste ', deaths, ' erorres      '+ ''.join(discovered))
            again = input('¿Quieres jugar otra vez? (1-Si 0-No):  ')
            if again == '1':
                word, dict_word, discovered, deaths, letters = initialize_game(word, dict_word, discovered, deaths,letters, file_path)
                continue
            else:
                print('Gracias por jugar :)')
                break

if __name__ == '__main__':
    clear_screen()
    file_name = input('Ingresa el nombre del archivo\ndata.txt\nnames.txt\nnumbers.txt \n(o presiona Enter para usar el archivo por defecto "data.txt"): ').strip()
    file_name = file_name if file_name else 'data.txt'
    run_game(file_name)