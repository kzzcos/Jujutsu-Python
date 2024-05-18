import os
from copy import deepcopy
from playsound import playsound
import threading
import time
import sys
from random import choice, uniform
import signal
import string

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

def linha():
    print('-' * 30)

def roxo(alvo, dmgadd=0):
    @audio('hollowpurple.mp3')
    def interação():
        linha()
        time.sleep(9.5)
        mensagem('gojo(?): sabe quem mais é o honrado?\n', 0.05)
        time.sleep(4)
        mensagem('amplificação de feitiço;\033[034mazul\033[0m.\n', 0.08)
        time.sleep(1)
        mensagem('reversão de feitiço;\t\033[031mvermelho\033[0m.\n', 0.08)
        time.sleep(1)
        mensagem('tecnica imaginária;')
        time.sleep(1)
        mensagem('\tvazio \033[035mROXO\033[0m.\n', 0.08)
        print('gojo(?): (a minha mãe)')
        linha()
    interação()
    dano = 1000
    dano += dmgadd
    global status_inimigo
    global status_atual
    alvo['hp'] -= 1000

def fuga(alvo, dmgadd=0):
    @audio('Fuga.mp3')
    def interação():
        time.sleep(2.5)
        print('\nsukuna:', end=' ')
        mensagem('abrir...')
        time.sleep(3.4)
        print(f'\n', end=' ')
        mensagem('isso é?..')
        time.sleep(3.2)
        print('\nsukuna:', end=' ')
        mensagem('\033[091mflecha de fogo\033[0m!\n')
    interação()
    dano = 1000
    dano += dmgadd
    global status_atual
    global status_inimigo
    alvo['hp'] -= dano

def malevolent_shrine():
    global expansao
    expansao = True
    global expansao_ativa
    expansao_ativa = 'malevolent_shrine'
    @audio('malevolentshrine1.mp3')
    def interação():
        mensagem('expansão de dominio...\n')
    interação()
    
def malevolent_shrine2(alvo):    
    global expansao_ativa
    @audio('malevolentshrine2.mp3')
    def interação2():
        time.sleep(8.5)
        mensagem('\t\033[031mmalevolent shrine...\033[0m\n')
    interação2()
    dano = 2000
    global status_atual
    global status_inimigo
    expansao_ativa = None
    alvo['hp'] -= dano

def muryokusho():
    global expansao
    expansao = True
    global expansao_ativa
    expansao_ativa = 'muryokusho'
    @audio('muryokusho1.mp3')
    def interação():
        mensagem('expansão de dominio...\n')
    interação()
def muryokusho2(alvo):
    global sucesso_expansao
    global expansao
    global expansao_ativa
    @audio('muryokusho2.mp3')
    def interação2():
        time.sleep(2)
        mensagem('\t\033[034mvoid infinito...\033[0m\n')
    interação2()
    dano = 2000
    global status_atual
    global status_inimigo
    alvo['hp'] -= dano
    expansao_ativa = None

expansoes = ['muryokusho', 'malevolent_shrine']

def poder(funcao, alvo=None, dmgadd=0): 
    global expansao
    global expansao_ativa2
    global expansao_ativa
    for personagem, ataques in poderes.items():
        for ataque in ataques:
            if funcao == ataque:
                jutsu = getattr(sys.modules[__name__], funcao)
                if funcao in expansoes:
                    if expansao == True and clash == False:
                        jutsu = getattr(sys.modules[__name__], str(funcao) + '2')
                        jutsu(alvo)
                        expansao = False
                        expansao_ativa = None
                        expansao_ativa2 = None
                    else:
                        jutsu()
                else:
                    jutsu(alvo, dmgadd)


def seuturno(expansao=False, awk=False):
    print('|---\033[092mSEU TURNO\033[0m---|')
    print(f'|---HABILIDADES---|')

    for i, hab in enumerate(habilidades, 1):
        print(f"|{i}) {hab}")

    hab_escolhida = None
    
    while hab_escolhida is None:
        try:
            opcao = int(input(f'\nEscolha uma habilidade: '))
            hab_escolhida = habilidades[opcao - 1]
        except (ValueError, IndexError):
            print('Escolha inválida!')

    if expansao:
        if hab_escolhida in expansoes:
            global clash
            global expansao_ativa2
            expansao_ativa2 = expansao_ativa
            clash = True
            poder(hab_escolhida)
            domain_clash()
            clash = False
            if venceu:
                poder(expansao_ativa, status_inimigo)
            else:
                poder(expansao_ativa2, status_atual)

        else:
            poder(expansao_ativa, status_atual)
            mensagem(f'{inimigo} usou expansão de dominio!')
            exibir_status(status_atual)
    elif hab_escolhida in expansoes:
        poder(hab_escolhida)
        mensagem(f'{voce} usou \033[095m{hab_escolhida}\033[0m.\n')
    if hab_escolhida not in expansoes:
        poder(hab_escolhida, status_inimigo)
        mensagem(f'{voce} usou \033[095m{hab_escolhida}\033[0m.\n')

    linha()
    exibir_status(status_inimigo)
    linha()

def turnoinimigo(expansao=False, awk=None):
    print('|---\033[031mTURNO DO INIMIGO\033[0m---|')
    hab_escolhida = choice(habilidades_inimigo)
    if expansao:
        if hab_escolhida in expansoes:
            global clash
            global expansao_ativa2
            expansao_ativa2 = expansao_ativa
            clash = True
            poder(hab_escolhida)
            domain_clash()
            clash = False
            if venceu == False:
                poder(expansao_ativa, status_atual)
            else:
                poder(expansao_ativa2, status_inimigo)

            
        else:
            poder(expansao_ativa, status_inimigo)
            mensagem(f'{voce} usou expansão de dominio!')
            exibir_status(status_inimigo)
    elif hab_escolhida in expansoes:
        poder(hab_escolhida)
    if hab_escolhida not in expansoes:
        poder(hab_escolhida, status_inimigo)
        mensagem(f'{inimigo} usou \033[095m{hab_escolhida}\033[0m.\n')

    linha()
    exibir_status(status_atual)
    linha()

def domain_clash():
    global expansao_ativa
    global expansao_ativa2
    global expansao
    global clash
    print('\tBATALHA DE DOMINIO!')
    print(f'{expansao_ativa} VS {expansao_ativa2}')
    letras_corretas = []
    pontos_usuario = 0
    pontos_inimigo = 0
    global venceu
    
    def verificar(letra_correta, jogador):
        nonlocal pontos_usuario, pontos_inimigo
        print(f"Digite a letra '{letra_correta}'!")
        start_time = time.time()
        entrada = input("Sua resposta: ")
        end_time = time.time()
        tempo_decorrido = end_time - start_time

        if entrada.lower() == letra_correta:
            print(f"{jogador} digitou corretamente em {tempo_decorrido:.2f} segundos!")
            pontos_usuario += 2
        else:
            print(f"{jogador} errou!")

    def entrada_inimigo(letra_correta):
        nonlocal pontos_usuario, pontos_inimigo
        tempo_aleatorio = uniform(0, 2)
        time.sleep(tempo_aleatorio)
        print(f"Inimigo digitou: {letra_correta} em {tempo_aleatorio:.2f} segundos!")
        pontos_inimigo += 1

    # Loop para a batalha de domínio
    pontos_usuario = 0
    pontos_inimigo = 0

    while pontos_usuario < 16 and pontos_inimigo < 10:
        letra_correta = choice(string.ascii_lowercase)
        print(f"Próxima letra: {letra_correta.upper()}")

        thread_usuario = threading.Thread(target=verificar, args=(letra_correta, "Você"))
        thread_inimigo = threading.Thread(target=entrada_inimigo, args=(letra_correta,))

        thread_usuario.start()
        thread_inimigo.start()

        thread_usuario.join(2)
        thread_inimigo.join(2)

        if thread_usuario.is_alive():
            print("Você não digitou a tempo!")
            pontos_inimigo += 1  # O inimigo ganha um ponto se o jogador não digitar a tempo
            thread_usuario.join()
        if thread_inimigo.is_alive():
            print("Inimigo não digitou a tempo!")
            pontos_usuario += 1  # O jogador ganha um ponto se o inimigo não digitar a tempo
            thread_inimigo.join()

        print()

    if pontos_usuario > pontos_inimigo:
        print("Você venceu a batalha de domínio!")
        venceu = True
    elif pontos_usuario < pontos_inimigo:
        print("Inimigo venceu a batalha de domínio!")
        venceu = False
    else:
        print("Empate na batalha de domínio!")
        expansao_ativa2 = None
        expansao_ativa = None
        expansao = False
        clash = False


def exibir_status(status):
    for chave, valor in status.items():
        print(f"\t{chave}: {valor}")

ficha = {'hp': 5000, 'awk': False}

personagens = {'gojo' :['yowaimo.mp3'], 'sukuna' : ['gambare.mp3']}
lista_personagens = list(personagens)

poderes = {
    'gojo': {'roxo' : 'roxo', 'muryokusho' : muryokusho},
    'sukuna': {'fuga' : fuga, 'malevolent_shrine' : malevolent_shrine},
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
        habilidades = list(poderes[voce].keys())
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
        habilidades_inimigo = list(poderes[inimigo].keys())
        status_inimigo = deepcopy(ficha)
        break

    except ValueError or NameError:
        print('personagem inválido!')
        time.sleep(1)
        clear()
    except:
        print('\t\033[091mERRO!\033[0m', end='\ntente novamente')
        time.sleep(1)
        clear()

mensagem('tudo \033[092mOK\033[0m.......\n')
mensagem('   iniciando...')
time.sleep(1)
clear()

print(inimigo, status_inimigo, habilidades_inimigo)
print(voce, status_atual, habilidades)

mensagem('\t\tAMBIENTE DE TESTE\n')
print('\t\033[093mCOMBATE\033[0m\n')

voiceline(random_voiceline(voce), voce)
voiceline(random_voiceline(inimigo), inimigo)

clash = False
venceu = None
expansao_ativa2 = None
expansao_ativa = None
expansao = False
fase = 0
escolha2 = None
derrota = False
while True:
    if escolha2 is not None and escolha2 in 'nN':
        break
    if derrota:
        while True:
            try:
                print('deseja tentar novamente?(S/N)')
                escolha2 = str(input('decisão: '))
                if len(escolha2) > 1:
                    raise ValueError
                if escolha2 in 'Ss':
                    derrota = False
                    break
                else:
                    derrota = True
            except ValueError:
                print('escolha inválida!')
        if derrota:
            break
    
    status_inimigo = deepcopy(ficha)
    status_atual = deepcopy(ficha)
    if fase > 0:
        status_inimigo['hp'] += hpadd
    while True:
        seuturno(expansao)
        if status_inimigo['hp'] <= 0:
            print('\t\033[092mVITÓRIA\033[0m')
            print('você venceu!')
            break
        turnoinimigo(expansao)
        if status_atual['hp'] <= 0:
            print('\t\033[094mDERROTA\033[0m\n')
            print('você perdeu!')
            derrota = True
            break
    while True:
        try:
            print('deseja ir para a próxima fase? (S/N)')
            escolha2 = str(input('decisão: '))
            if len(escolha2) > 1:
                raise ValueError
            if escolha2 in 'sS':
                fase += 1
                hpadd = fase * 1000
                break
            else:
                break
        except ValueError:
            print('\t opção \033[091minválida!\033[0m')
            time.sleep(1)
            clear()
print('\t\033[091mFIM DE JOGO!\033[0m')