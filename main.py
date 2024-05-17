import os
from copy import deepcopy
from playsound import playsound
import threading
import time
import sys
from random import choice

voicelines = ['gambare.mp3', 'yowaimo.mp3']
def voiceline(arquivo, personagem):
    @audio(arquivo)
    def interação():
        if personagem == 'gojo':
            if 'yowaimo' in arquivo:
                time.sleep(1)
                mensagem('gojo: hahaha... ', 0.02)
                time.sleep(0.8)
                mensagem('eu vou ficar bem, ', 0.06)
                time.sleep(0.5)
                mensagem('afinal... ', 0.03)
                time.sleep(1.5)
                mensagem('você é \033[091mfraco\033[0m.\n')
        if personagem == 'sukuna':
            if 'gambare' in arquivo:
                time.sleep(0.5)
                mensagem('sukuna: vamos lá... ', 0.05)
                time.sleep(0.7)
                mensagem('você consegue.\n', 0.05)
    interação()

def random_voiceline(personagem):
    voiceline_escolhida = choice(personagens[personagem])
    return voiceline_escolhida

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mensagem(texto, intervalo=0.01):
    for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(intervalo)

def audio(arquivo):
    def decorador(interação):
        def closure():
            def reproduzir_audio(file_path):
                playsound(file_path)
            audio_thread = threading.Thread(target=reproduzir_audio, args=(f'audios/{arquivo}',))
            audio_thread.start()
            interação()
            audio_thread.join()
        return closure
    return decorador

def fuga(alvo, dmgadd=0):
    @audio('Fuga.mp3')
    def interação():
        time.sleep(2.5)
        print(f'\n{voce}:', end=' ')
        mensagem('abrir portões...')
        time.sleep(3.4)
        print(f'\n{inimigo}:', end=' ')
        mensagem('isso é?..')
        time.sleep(3.2)
        print(f'\n{voce}:', end=' ')
        mensagem('\033[091mflecha de fogo\033[0m!\n')
    interação()
    dano = 1000
    dano += dmgadd
    global status_atual
    alvo['hp'] -= dano

def poder(funcao, alvo, dmgadd=0,): 
    for personagem, ataques in poderes.items():
        for ataque in ataques:
            if funcao == ataque:
                jutsu = getattr(sys.modules[__name__], funcao)
                jutsu(alvo, dmgadd)


def seuturno(expansao=False, awk=False):
    print('\t|---\033[092mSEU TURNO\033[0m---|')
    print('')
    print(f'\t|---HABILIDADES---|')

    habilidades_list = list(habilidades.keys())
    habilidades_list.sort()

    for i, hab in enumerate(habilidades_list, 1):
        print(f"\t{i}) {hab}")

    hab_escolhida = None
    
    while hab_escolhida is None:
        try:
            opcao = int(input(f'\n\tEscolha uma habilidade: '))
            hab_escolhida = habilidades_list[opcao - 1]
        except (ValueError, IndexError):
            print('Escolha inválida!')

    if expansao:
        if hab_escolhida == 'expansão de dominio':
            domain_clash()
    elif hab_escolhida == 'expansão de dominio':
        return hab_escolhida
    else:
        poder(hab_escolhida, status_inimigo)
    mensagem(f'você usou \033[095m{hab_escolhida}\033[0m.\n')
    exibir_status(status_inimigo)

def domain_clash():
    print('domain clash!!!')

def exibir_status(status):
    for chave, valor in status.items():
        print(f"\t{chave}: {valor}")

ficha = {'hp': 5000, 'awk': False}
status_inimigo = {'hp': 5000, 'awk': False}

personagens = {'gojo' :['yowaimo.mp3'], 'sukuna' : ['gambare.mp3']}
lista_personagens = list(personagens)

poderes = {
    'gojo': {'roxo' : 'roxo'},
    'sukuna': {'fuga' : fuga, 'awakening' : 'awakening'},
    'megumi': {'mahoraga' : 'mahoraga'}
}

while True:
    try:
        print(f'''
        escolha seu personagem:
        \t1|gojo
        \t2|sukuna
        \t3|megumi  \033[093m(indisponivel)\033[0m''', end='\n')
        escolha = int(input('eu serei... '))
        if escolha < 1 or escolha > len(lista_personagens):
            raise ValueError
        
        voce = lista_personagens[escolha - 1]
        mensagem(f'você será {voce}')
        time.sleep(2)
        clear()
        habilidades = deepcopy(poderes[voce])
        status_atual = deepcopy(ficha)
        
    
        print(f'''
        escolha seu inimigo:
        \t1|gojo
        \t2|sukuna
        \t3|megumi  \033[093m(indisponivel)\033[0m''', end='\n')
        escolha = int(input('ele será... '))
        if escolha < 1 or escolha > len(lista_personagens):
            raise ValueError
        
        inimigo = lista_personagens[escolha - 1]
        mensagem(f'o inimigo será {inimigo}')
        time.sleep(2)
        clear()
        habilidades_inimigo = deepcopy(poderes[inimigo])
        status_inimigo = deepcopy(ficha)
        break

    except ValueError or NameError:
        print('personagem inválido!')
        clear()
    except:
        print('\t\033[091mERRO!\033[0m', end='\ntente novamente')
        time.sleep(2)
        clear()

mensagem('tudo \033[092mOK\033[0m.......\n')
mensagem('   iniciando...')
time.sleep(2)
clear()

print(inimigo, status_inimigo, habilidades_inimigo)
print(voce, status_atual, habilidades)

mensagem('\t\tAMBIENTE DE TESTE\n')
print('\t\033[093mCOMBATE\033[0m\n')

voiceline(random_voiceline(voce), voce)
voiceline(random_voiceline(inimigo), inimigo)

while True:
    seuturno()
    if status_inimigo['hp'] <= 0:
        print('\t\033[092mvocê venceu!\033[0m')
        break
    
