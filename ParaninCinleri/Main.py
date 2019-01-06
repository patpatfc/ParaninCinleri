import pygame
import time
from Tkinter import *


pygame.init()

WIDTH = 1300
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paranin Cinleri - Murathan Mungan')



#renkler/colors
green = (0, 255, 0)
red = (255, 0, 0)
cogirenk = (200, 150, 20)

#resimler/images
sinirlar = pygame.image.load('makedonyaharitasi.png')
yunanistan = pygame.image.load('yunanistan.png')
anadolu = pygame.image.load('anadolu.png')
mezopotamya = pygame.image.load('mezopotamya.png')
misir = pygame.image.load('misir.png')
asya = pygame.image.load('asya.png')
Backg1 = pygame.image.load('mungan.png')
Backg2 = pygame.image.load('Muratcim.png')

geri = pygame.image.load('geri.png')

harita = pygame.image.load('haritavecografya.png')
harita_pressed = pygame.image.load('haritavecografyapress.png')

yonetim = pygame.image.load('yonetimbicimi.png')
yonetim_pressed = pygame.image.load('yonetimbicimipress.png')

siniflar = pygame.image.load('toplumsalsiniflar.png')
siniflar_pressed = pygame.image.load('toplumsalsiniflarpress.png')

ekonomi = pygame.image.load('ekonomi.png')
ekonomi_pressed = pygame.image.load('ekonomipress.png')

helenizm = pygame.image.load('helenizm.png')
helenizm_pressed = pygame.image.load('helenizmpress.png')

kapakfoto = pygame.image.load('buyukiskenderun.png')


def text_objects(text, color, size):
    font = pygame.font.SysFont(None, size)
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


def screen_message(msg, color, y_distance, x_distance, text_size):
    textSurf, textRect = text_objects(msg, color, text_size)
    textRect.center =(WIDTH / 2) - x_distance,((HEIGHT / 2) - y_distance)
    screen.blit(textSurf, textRect)


def message(mesg, color, mesg_x, mesg_y):
    font = pygame.font.SysFont(None, 150)
    screen_text = font.render(mesg, True, color)
    screen.blit(screen_text, [mesg_x, mesg_y])


def yunanistani():
    yunanistan_info = pygame.image.load('yunanistaninfo.png')
    yunanistan_harita = pygame.image.load('yunanistanharita.png')
    geri_changer2 = False
    yuni = True
    while yuni:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(cogirenk)

        if 125 < mouse[0] < 205 and 25 < mouse[1] < 59:
            geri_changer2 = True
            if click[0] == 1:
                MardinScreen()
        else:
            geri_changer2 = False

        if geri_changer2 == True:
            geri = pygame.image.load('geripress.png')
        if geri_changer2 == False:
            geri = pygame.image.load('geri.png')

        screen.blit(yunanistan_info, [0, 200])
        screen.blit(geri, [125, 25])
        screen.blit(yunanistan_harita, [425, 500])
        pygame.display.update()


def anadolui():
    anadolu_info = pygame.image.load('anadoluinfo.png')
    anadolu_harita = pygame.image.load('anadoluharita.png')
    geri_changer2 = False
    ani = True
    while ani:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(cogirenk)

        if 125 < mouse[0] < 205 and 25 < mouse[1] < 59:
            geri_changer2 = True
            if click[0] == 1:
                MardinScreen()
        else:
            geri_changer2 = False

        if geri_changer2 == True:
            geri = pygame.image.load('geripress.png')
        if geri_changer2 == False:
            geri = pygame.image.load('geri.png')

        screen.blit(anadolu_info, [0, 200])
        screen.blit(geri, [125, 25])
        screen.blit(anadolu_harita, [400, 500])
        pygame.display.update()


def mezopotamyai():
    mezopotamya_info = pygame.image.load('mezopotamyainfo.png')
    mezopotamya_harita = pygame.image.load('mezopotamyaharita.png')
    geri_changer2 = False
    mezi = True
    while mezi:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(cogirenk)

        if 125 < mouse[0] < 205 and 25 < mouse[1] < 59:
            geri_changer2 = True
            if click[0] == 1:
                MardinScreen()
        else:
            geri_changer2 = False

        if geri_changer2 == True:
            geri = pygame.image.load('geripress.png')
        if geri_changer2 == False:
            geri = pygame.image.load('geri.png')

        screen.blit(mezopotamya_info, [0, 200])
        screen.blit(geri, [125, 25])
        screen.blit(mezopotamya_harita, [400, 490])
        pygame.display.update()


def misiri():
    misir_harita = pygame.image.load('misirharita.png')
    misir_info = pygame.image.load('misirinfo.png')
    geri_changer2 = False
    misri = True
    while misri:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(cogirenk)

        if 125 < mouse[0] < 205 and 25 < mouse[1] < 59:
            geri_changer2 = True
            if click[0] == 1:
                MardinScreen()
        else:
            geri_changer2 = False

        if geri_changer2 == True:
            geri = pygame.image.load('geripress.png')
        if geri_changer2 == False:
            geri = pygame.image.load('geri.png')

        screen.blit(misir_info, [0, 200])
        screen.blit(geri, [125, 25])
        screen.blit(misir_harita, [400, 500])
        pygame.display.update()


def asyai():
    asya_harita = pygame.image.load('asyaharita.png')
    asya_info = pygame.image.load('asyainfo.png')
    geri_changer2 = False
    asyi = True
    while asyi:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(cogirenk)

        if 125 < mouse[0] < 205 and 25 < mouse[1] < 59:
            geri_changer2 = True
            if click[0] == 1:
                MardinScreen()
        else:
            geri_changer2 = False

        if geri_changer2 == True:
            geri = pygame.image.load('geripress.png')
        if geri_changer2 == False:
            geri = pygame.image.load('geri.png')

        screen.blit(asya_info, [0, 200])
        screen.blit(geri, [125, 25])
        screen.blit(asya_harita, [400, 400])
        pygame.display.update()


def opening_screen():
    start = False
    harita_changer = False
    yonetim_changer = False
    siniflar_changer = False
    ekonomi_changer = False
    helenizm_changer = False
    while not start:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if 100 < mouse[0] < 310 and 100 < mouse[1] < 124:
            harita_changer = True
            if click[0] == 1:
                MardinScreen()
        else:
            harita_changer = False

        if 100 < mouse[0] < 380 and 200 < mouse[1] < 224:
            yonetim_changer = True
            if click[0] == 1:
                AileScreen()
        else:
            yonetim_changer = False

        if 100 < mouse[0] < 250 and 300 < mouse[1] < 324:
            siniflar_changer = True
            if click[0] == 1:
                KisilerScreen()
        else:
            siniflar_changer = False

        if 100 < mouse[0] < 320 and 400 < mouse[1] < 424:
            ekonomi_changer = True
            if click[0] == 1:
                ekomake()
        else:
            ekonomi_changer = False

        if 100 < mouse[0] < 260 and 500 < mouse[1] < 524:
            helenizm_changer = True
            if click[0] == 1:
                helenizmi()
        else:
            helenizm_changer = False

        if harita_changer == True:
            harita = pygame.image.load('haritavecografyapress.png')
        if harita_changer == False:
            harita = pygame.image.load('haritavecografya.png')

        if yonetim_changer == True:
            yonetim = pygame.image.load('yonetimbicimipress.png')
        if yonetim_changer == False:
            yonetim = pygame.image.load('yonetimbicimi.png')

        if siniflar_changer == True:
            siniflar = pygame.image.load('toplumsalsiniflarpress.png')
        if siniflar_changer == False:
            siniflar = pygame.image.load('toplumsalsiniflar.png')

        if ekonomi_changer == True:
            ekonomi = pygame.image.load('ekonomipress.png')
        if ekonomi_changer == False:
            ekonomi = pygame.image.load('ekonomi.png')

        if helenizm_changer == True:
            helenizm = pygame.image.load('helenizmpress.png')
        if helenizm_changer == False:
            helenizm = pygame.image.load('helenizm.png')


        screen.blit (Backg1, [0, 0])
        screen.blit (Backg2, [650, 0])
        screen.blit(harita, [100, 100])
        screen.blit(yonetim, [100, 200])
        screen.blit(siniflar, [100, 300])
        screen.blit(ekonomi, [100, 400])
        screen.blit(helenizm, [100, 500])
        screen_message("Paranin Cinleri", red, 300, 0, 30)
        #screen.blit(kapakfoto, [500, 100])
        pygame.display.update()


def MardinScreen():
    geri = pygame.image.load('geri.png')
    Loop = True
    yunanistan_changer = False
    anadolu_changer = False
    mezopotamya_changer = False
    misir_changer = False
    asya_changer = False
    geri_changer = False

    while Loop:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(cogirenk)

        if 50 < mouse[0] < 150 and 600 < mouse[1] < 624:
            yunanistan_changer = True
            if click[0] == 1:
                yunanistani()
        else:
            yunanistan_changer = False

        if 200 < mouse[0] < 280 and 600 < mouse[1] < 624:
            anadolu_changer = True
            if click[0] == 1:
                anadolui()
        else:
            anadolu_changer = False

        if 350 < mouse[0] < 450 and 600 < mouse[1] < 624:
            mezopotamya_changer = True
            if click[0] == 1:
                mezopotamyai()
        else:
            mezopotamya_changer = False

        if 500 < mouse[0] < 560 and 600 < mouse[1] < 624:
            misir_changer = True
            if click[0] == 1:
                misiri()
        else:
            misir_changer = False

        if 650 < mouse[0] < 730 and 600 < mouse[1] < 624:
            asya_changer = True
            if click[0] == 1:
                asyai()
        else:
            asya_changer = False

        if 25 < mouse[0] < 105 and 25 < mouse[1] < 59:
            geri_changer = True
            if click[0] == 1:
                opening_screen()
        else:
            geri_changer = False

        if yunanistan_changer == True:
            yunanistan = pygame.image.load('yunanistanpress.png')
        if yunanistan_changer == False:
            yunanistan = pygame.image.load('yunanistan.png')

        if anadolu_changer == True:
            anadolu = pygame.image.load('anadolupress.png')
        if anadolu_changer == False:
            anadolu = pygame.image.load('anadolu.png')

        if mezopotamya_changer == True:
            mezopotamya = pygame.image.load('mezopotamyapress.png')
        if mezopotamya_changer == False:
            mezopotamya = pygame.image.load('mezopotamya.png')

        if misir_changer == True:
            misir = pygame.image.load('misirpress.png')
        if misir_changer == False:
            misir = pygame.image.load('misir.png')

        if asya_changer == True:
            asya = pygame.image.load('asyapress.png')
        if asya_changer == False:
            asya = pygame.image.load('asya.png')

        if geri_changer == True:
            geri = pygame.image.load('geripress.png')
        if geri_changer == False:
            geri = pygame.image.load('geri.png')

        screen.blit(sinirlar, [25, 75])
        screen.blit(yunanistan, [50, 600])
        screen.blit(anadolu, [200, 600])
        screen.blit(mezopotamya, [350, 600])
        screen.blit(misir, [500, 600])
        screen.blit(asya, [650, 600])
        screen.blit(geri, [25, 25])
        pygame.display.update()


def AileScreen():
    yone_info = pygame.image.load('yoneinfo.png')
    emperor = pygame.image.load('emperor.png')
    geri = pygame.image.load('geri.png')
    geri_changer = False
    yonetim = True
    while yonetim:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(cogirenk)

        if 25 < mouse[0] < 105 and 25 < mouse[1] < 59:
            geri_changer = True
            if click[0] == 1:
                opening_screen()
        else:
            geri_changer = False

        if geri_changer == True:
            geri = pygame.image.load('geripress.png')
        if geri_changer == False:
            geri = pygame.image.load('geri.png')

        screen.blit(yone_info, [0, 50])
        screen.blit(emperor, [300, 270])
        screen.blit(geri, [25, 25])
        pygame.display.update()


def helenizmi():
    helenizm_info = pygame.image.load('helenizminfo.png')
    geri = pygame.image.load('geri.png')
    helen_foto = pygame.image.load('helenfoto.png')
    geri_changer = False
    heli = True
    while heli:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(cogirenk)

        if 25 < mouse[0] < 105 and 25 < mouse[1] < 59:
            geri_changer = True
            if click[0] == 1:
                opening_screen()
        else:
            geri_changer = False

        if geri_changer == True:
            geri = pygame.image.load('geripress.png')
        if geri_changer == False:
            geri = pygame.image.load('geri.png')

        screen.blit(helenizm_info, [0, 200])
        screen.blit(helen_foto, [300, 400])
        screen.blit(geri, [25, 25])
        pygame.display.update()


def ekomake():
    eko_info = pygame.image.load('ekoinfo.png')
    geri = pygame.image.load('geri.png')
    geri_changer = False
    eki = True
    while eki:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(cogirenk)

        if 25 < mouse[0] < 105 and 25 < mouse[1] < 59:
            geri_changer = True
            if click[0] == 1:
                opening_screen()
        else:
            geri_changer = False

        if geri_changer == True:
            geri = pygame.image.load('geripress.png')
        if geri_changer == False:
            geri = pygame.image.load('geri.png')

        screen.blit(eko_info, [0, 200])
        screen.blit(geri, [25, 25])
        pygame.display.update()


def KisilerScreen():
    toplum_info = pygame.image.load('topluminfo.png')
    geri = pygame.image.load('geri.png')
    geri_changer = False
    topi = True
    while topi:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(cogirenk)

        if 25 < mouse[0] < 105 and 25 < mouse[1] < 59:
            geri_changer = True
            if click[0] == 1:
                opening_screen()
        else:
            geri_changer = False

        if geri_changer == True:
            geri = pygame.image.load('geripress.png')
        if geri_changer == False:
            geri = pygame.image.load('geri.png')

        screen.blit(toplum_info, [0, 200])
        screen.blit(geri, [25, 25])
        pygame.display.update()


opening_screen()


