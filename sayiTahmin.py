
# sayi tahmin oyunu kodlayalim.
# murattanhu

import random

oyun = True
while oyun:

    sayi = random.randint(1, 10)
    hak = 7
    while True:
        hak -= 1
        tahmin = int(input('Bilgisayar bir sayi tuttu, sence hangi sayidir? '))

        if tahmin == sayi:
            print('Tebrikler!. Bildiniz :))')
            break

        elif tahmin > sayi:
            print('Asagi ...')

        else:
            print('Yukari...')

        if hak == 0:
            print('Maalesef kazanamadiniz.\nTutulan sayi : {}'.format(sayi))
            break

    devam = input('Devam etmek ister misin? (E/H): ')
    if devam == 'e':
        oyun = True
    else:
        oyun = False










