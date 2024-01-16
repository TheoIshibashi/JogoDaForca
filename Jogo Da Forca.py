import random

FORCAIMG = ['''

    +---+
    |   |
        |
        |
        |
        |
===========''','''

    +---+
    |   |
    O   |
        |
        |
        |
===========''','''


    +---+
    |   |
    O   |
    |   |
        |
        |
===========''','''

    +---+
    |   |
    O   |
   /|   |
        |
        |
===========''','''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========''','''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===========''','''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===========''']

palavras = 'banana telescopio cachorro martelo girafa hamburguer chocolate alimentos bolacha carne boi mae pai preguica tampa privada seculo'.split()

def main():
    global FORCAIMG
    print('F O R C A')
    letrasErradas = ''
    letrasAcertadas = ''
    palavraSecreta = geraPalavraAleatoria().upper()
    jogando = True
    
    while jogando:
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
        palpite = recebePalpite(letrasErradas + letrasAcertadas)
        if palpite in palavraSecreta:
            letrasAcertadas += palpite
            if VerificaSeGanhou(palavraSecreta, letrasAcertadas):
                print("Exato! A palavra secreta é " +palavraSecreta)
                jogando = False
        else:
            letrasErradas += palpite
            if len(letrasErradas) == len(FORCAIMG)-1:
               imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
               print("Voce excedeu o seu limite de palpites")
               print("Depois de "+str(len(letrasErradas))+' letras erradas e'+str(len(letrasAcertadas)), end = ' ')
               print("Palpites corretos, a palavra era "+palavraSecreta+'.')
               jogando = False

        if not jogando:
            if JogarNovamente():
               letrasErradas = ''
               letrasAcertadas = ''
               jogando = True
               palavraSecreta = geraPalavraAleatoria().upper()
            

def geraPalavraAleatoria():
    global palavras
    return random.choice(palavras)


def imprimeComEspacos(palavra):
    for letra in palavra:
        print(letra, end = '')
    print()
        

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)] + '\n')

    print("Letras Erradas: ", end = ' ')
    imprimeComEspacos(letrasErradas)

    vazio = '_'*len(palavraSecreta)

    for i in range(len(palavraSecreta)):
          if palavraSecreta[i] in letrasAcertadas:
              vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]

    imprimeComEspacos(vazio)

def recebePalpite(palpitesFeitos):
    while True:
        palpite = input("Advinhe uma letra. \n").upper()

        if len(palpite) != 1:
            print("Coloque uma unica letra. \n")
        elif palpite in palpitesFeitos:
            print("Esta letra ja existe, digite outra \n")
        elif not 'A' <= palpite <= 'Z':
            print("Insira apenas letras.")
        else:
            return palpite
        
def JogarNovamente():
    return input("Voce quer jogar novamente? (Sim ou Nao) \n").upper().startswith('S')
                


def VerificaSeGanhou(palavraSecreta, letrasAcertadas):

    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break
    return ganhou


main()



