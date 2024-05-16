import os
from copy import deepcopy
from playsound import playsound
import threading
import time
import sys

def mensagem(texto):
    for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)

def audio(arquivo):
    def decorador(interação):
        def closure():
            def reproduzir_audio(file_path):
                playsound(file_path)
            audio_thread = threading.Thread(target=reproduzir_audio, args=(arquivo))
            audio_thread.start()
            interação()
            audio_thread.join()
        return closure
    return decorador

def fuga():
    @audio('Fuga.mp3')
    def interação():
        time.sleep(2.3)
        print('\nvocê:', end=' ')
        mensagem('abrir portões...')
        time.sleep(3.2)
        print('\ninimigo:', end=' ')
        mensagem('isso é?..')
        time.sleep(3)
        print('\nvocê:', end=' ')
        mensagem('\033[091mflecha de fogo\033[0m!')
    interação()


status = {'hp' : 5000, 
          'awk' : None}

personagens = ['gojo', 'sukuna', 'megumi']

poderes = {
    'gojo' : 
    [
        {'roxo' : {'dano' : 1000}}
        ],
    
    'sukuna' : 
    [
        {'fuga' : {'dano' : 1000,}}
        ],
    
    'megumi' : 
    [
        {'mahoraga' : {'dano' : 1000,}}
        ]
}

while True:
    try:
        print(f'''
        escolha seu personagem:
        \t1|gojo
        \t2|sukuna
        \t3|megumi  ''', end='\n')
        escolha = int(input('eu serei... '))
        print(personagens[escolha - 1])

        if escolha < 1 or escolha > len(personagens):
            raise ValueError

        character = deepcopy(poderes[personagens[escolha - 1]])
        break

    except ValueError or NameError:
        print('personagem inválido!')
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print('\t\033[091mERRO!\033[0m', end='\ntente novamente')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

playsound('audios_mp3/Fuga.mp3')