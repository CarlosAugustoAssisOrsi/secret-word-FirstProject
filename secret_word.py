import random

segredo = random.choice([
    'segredo', 'bicicleta', 'travesseiro', 'almofada', 'sapato', 'falso'
])
digitadas = []
chances = 3

print('Te desafio a descobrir a palavra secreta !!')
print('A palavra contém {} letras!!'.format(len(segredo)))

while True:
    letra = input('Digite uma letra: ')

    if chances < 2:
        print('Suas chances acabaram :(')
        print('A palavra secreta é {}'.format(segredo))
        break

    if len(letra) > 2 and letra != segredo:
        chances += -1
        print('Essa não é a palavra secreta')
        print('Ainda restam {} chances'.format(chances))
        continue

    if len(letra) > 1:

        if letra == segredo:
            print('PARABÉNS !! você descobriu que a palavra secreta é {} !!!'.format(segredo))
            break
        else:
            print('Digite apenas 1 letra por vez ou a palavra completa !!')
            continue

    digitadas.append(letra)

    if letra in segredo:
        print(f'Parabéns, você descobriu uma das letras :)')
    else:
        chances += -1
        print(f'Essa letra não faz parte da palavra secreta :(')
        print('Ainda restam {} tentativa(s)'.format(chances))
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in segredo:

        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '_'

    print(secreto_temporario)

    if secreto_temporario == segredo:
        print('PARABÉNS !!')
        print('Você descobriu que a palavra secreta é {} !!'.format(segredo))
        break
