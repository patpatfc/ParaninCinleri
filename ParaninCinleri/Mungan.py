import pygame
import time
pygame.init()

WIDTH = 1300
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Makedonya Uygarlığı (Büyük İskender İmparatorluğu)')
green = (0, 255, 0)
red = (255,0,0)
cogirenk = (200,150,20)


sınırlar = pygame.image.load('makedonya haritası.png')
yünanistan = pygame.image.load('yünanistan.png')
anadolu = pygame.image.load('anadolu.png')
mezopotamya = pygame.image.load('mezopotamya.png')
mısır = pygame.image.load('mısır.png')
asya = pygame.image.load('asya.png')
Backg1 = pygame.image.load('mungan.png')
Backg2 = pygame.image.load('Muratcım.png')

geri = pygame.image.load('geri.png')

mehtap = pygame.image.load('Mehtaplı geceler.png')
mehtap_pressed = pygame.image.load('Mehtaplı geceler pressed.png')

yönetim = pygame.image.load('yönetim biçimi.png')
yönetim_pressed = pygame.image.load('yönetim biçimi press.png')

sınıflar = pygame.image.load('toplumsal sınıflar.png')
sınıflar_pressed = pygame.image.load('toplumsal sınıflar press.png')

ekonomi = pygame.image.load('ekonomi.png')
ekonomi_pressed = pygame.image.load('ekonomi press.png')

aile = pygame.image.load('Aile.png')
aile_pressed = pygame.image.load('Aile pressed.png')

kapakfoto = pygame.image.load('Kapakfoto.png')
munganAlıntı = pygame.image.load('munganalıntı.png')

def text_objects(text,color,size):
    font = pygame.font.SysFont(None,size)
    textsurface = font.render(text,True,color)
    return textsurface,textsurface.get_rect()

def screen_message(msg,color,y_distance,x_distance,text_size):
    textSurf,textRect = text_objects(msg,color,text_size)
    textRect.center = (WIDTH/2)-x_distance,((HEIGHT/2)-y_distance)
    screen.blit(textSurf,textRect)

def message(mesg,color,mesg_x,mesg_y):
    font = pygame.font.SysFont(None,150)
    screen_text = font.render(mesg,True,color)
    screen.blit(screen_text, [mesg_x,mesg_y])


def yünanistani():
    yünanistan_info = pygame.image.load('yünanistan info.png')
    yünanistan_harita = pygame.image.load('yünanistan harita.png')
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
                coğrafya()
        else:
            geri_changer2 = False


        if geri_changer2 == True:
            geri = pygame.image.load('geri press.png')
        if geri_changer2 == False:
            geri = pygame.image.load('geri.png')

        screen.blit(yünanistan_info,[0,200])
        screen.blit(geri,[125,25])
        screen.blit(yünanistan_harita,[425,500])
        pygame.display.update()

        
def anadolui():
    anadolu_info = pygame.image.load('anadolu info.png')
    anadolu_harita = pygame.image.load('anadolu harita.png')
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
                coğrafya()
        else:
            geri_changer2 = False


        if geri_changer2 == True:
            geri = pygame.image.load('geri press.png')
        if geri_changer2 == False:
            geri = pygame.image.load('geri.png')

        screen.blit(anadolu_info,[0,200])
        screen.blit(geri,[125,25])
        screen.blit(anadolu_harita,[400,500])
        pygame.display.update()

def mezopotamyai():
    mezopotamya_info = pygame.image.load('mezopotamya info.png')
    mezopotamya_harita = pygame.image.load('mezopotamya harita.png')
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
                coğrafya()
        else:
            geri_changer2 = False


        if geri_changer2 == True:
            geri = pygame.image.load('geri press.png')
        if geri_changer2 == False:
            geri = pygame.image.load('geri.png')

        screen.blit(mezopotamya_info,[0,200])
        screen.blit(geri,[125,25])
        screen.blit(mezopotamya_harita,[400,490])
        pygame.display.update()

def mısıri():
    mısır_harita = pygame.image.load('mısır harita.png')
    mısır_info = pygame.image.load('mısır info.png')
    geri_changer2 = False
    mısri = True
    while mısri:
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
                coğrafya()
        else:
            geri_changer2 = False


        if geri_changer2 == True:
            geri = pygame.image.load('geri press.png')
        if geri_changer2 == False:
            geri = pygame.image.load('geri.png')

        screen.blit(mısır_info,[0,200])
        screen.blit(geri,[125,25])
        screen.blit(mısır_harita,[400,500])
        pygame.display.update()


def asyai():
    asya_harita = pygame.image.load('asya harita.png')
    asya_info = pygame.image.load('asya info.png')
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
                coğrafya()
        else:
            geri_changer2 = False


        if geri_changer2 == True:
            geri = pygame.image.load('geri press.png')
        if geri_changer2 == False:
            geri = pygame.image.load('geri.png')

        screen.blit(asya_info,[0,200])
        screen.blit(geri,[125,25])
        screen.blit(asya_harita,[400,400])
        pygame.display.update()




def opening_screen():
    start = False
    mehtap_changer = False
    yönetim_changer = False
    sınıflar_changer = False
    ekonomi_changer = False
    aile_changer = False
    while not start:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(green)
                
        if 100 < mouse[0] <  348 and 100 < mouse[1] < 124:
            mehtap_changer = True
            if click[0] == 1:
                coğrafya()
        else:
            mehtap_changer = False

        if 100 < mouse[0] <  380 and 200 < mouse[1] < 224:
            yönetim_changer = True
            if click[0] == 1:
                yönetimveanlayış()
        else:
            yönetim_changer = False

        if 100 < mouse[0] <  250 and 300 < mouse[1] < 324:
            sınıflar_changer = True
            if click[0] == 1:
                toplim()
        else:
            sınıflar_changer = False

        if 100 < mouse[0] <  320 and 400 < mouse[1] < 424:
            ekonomi_changer = True
            if click[0] == 1:
                ekomake()
        else:
            ekonomi_changer = False

        if 100 < mouse[0] <  174 and 500 < mouse[1] < 524:
            aile_changer = True
            if click[0] == 1:
                helenizmi()
        else:
            aile_changer = False

            



        if mehtap_changer == True:
            mehtap = pygame.image.load('Mehtaplı geceler pressed.png') 
        if mehtap_changer == False:
            mehtap = pygame.image.load('Mehtaplı geceler.png')

        if yönetim_changer == True:
            yönetim = pygame.image.load('yönetim biçimi press.png')
        if yönetim_changer == False:
            yönetim = pygame.image.load('yönetim biçimi.png')

        if sınıflar_changer == True:
            sınıflar = pygame.image.load('toplumsal sınıflar press.png')
        if sınıflar_changer == False:
            sınıflar = pygame.image.load('toplumsal sınıflar.png')

        if ekonomi_changer == True:
            ekonomi = pygame.image.load('ekonomi press.png')
        if ekonomi_changer == False:
            ekonomi = pygame.image.load('ekonomi.png')

        if aile_changer == True:
            aile = pygame.image.load('Aile pressed.png')
        if aile_changer == False:
            aile = pygame.image.load('Aile.png')




            
        screen.blit(Backg1,[0,0])
        screen.blit(Backg2,[650,0])
        screen.blit(mehtap,[100,100])           
        screen.blit(yönetim,[100,200])
        screen.blit(sınıflar,[100,300])
        screen.blit(ekonomi,[100,400])
        screen.blit(aile,[100,500])
        screen.blit(kapakfoto,[500,300])
        screen.blit(munganAlıntı,[750,550])
        pygame.display.update()



def coğrafya():
    geri = pygame.image.load('geri.png')
    cogi = True
    yünanistan_changer = False
    anadolu_changer = False
    mezopotamya_changer = False
    mısır_changer = False
    asya_changer = False
    geri_changer = False
    
    while cogi:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(cogirenk)

        if 50 < mouse[0] <  150 and 600 < mouse[1] < 624:
            yünanistan_changer = True
            if click[0] == 1:
                yünanistani()
        else:
            yünanistan_changer = False

        if 200 < mouse[0] <  280 and 600 < mouse[1] < 624:
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

        if 500 < mouse[0] <  560 and 600 < mouse[1] < 624:
            mısır_changer = True
            if click[0] == 1:
                mısıri()
        else:
            mısır_changer = False

        if 650 < mouse[0] <  730 and 600 < mouse[1] < 624:
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

            



        if yünanistan_changer == True:
            yünanistan = pygame.image.load('yünanistan press.png') 
        if yünanistan_changer == False:
            yünanistan = pygame.image.load('yünanistan.png')

        if anadolu_changer == True:
            anadolu = pygame.image.load('anadolu press.png')
        if anadolu_changer == False:
            anadolu = pygame.image.load('anadolu.png')

        if mezopotamya_changer == True:
            mezopotamya = pygame.image.load('mezopotamya press.png')
        if mezopotamya_changer == False:
            mezopotamya = pygame.image.load('mezopotamya.png')

        if mısır_changer == True:
            mısır = pygame.image.load('mısır press.png')
        if mısır_changer == False:
            mısır = pygame.image.load('mısır.png')

        if asya_changer == True:
            asya = pygame.image.load('asya press.png')
        if asya_changer == False:
            asya = pygame.image.load('asya.png')

        if geri_changer == True:
            geri = pygame.image.load('geri press.png')
        if geri_changer == False:
            geri = pygame.image.load('geri.png')












        
        screen.blit(sınırlar,[25,75])
        screen.blit(yünanistan,[50,600])
        screen.blit(anadolu,[200,600])
        screen.blit(mezopotamya,[350,600])
        screen.blit(mısır,[500,600])
        screen.blit(asya,[650,600])
        screen.blit(geri,[25,25])
        pygame.display.update()





def yönetimveanlayış():
    yöne_info = pygame.image.load('yöne info.png')
    emperor = pygame.image.load('emperor.png')
    geri = pygame.image.load('geri.png')
    geri_changer = False
    yönetim = True
    while yönetim:
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
            geri = pygame.image.load('geri press.png')
        if geri_changer == False:
            geri = pygame.image.load('geri.png')

        screen.blit(yöne_info,[0,50])
        screen.blit(emperor,[300,270])
        screen.blit(geri,[25,25])
        pygame.display.update()



def helenizmi():
    helenizm_info = pygame.image.load('helenizm info.png')
    geri = pygame.image.load('geri.png')
    helen_foto = pygame.image.load('helen foto.png')
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
            geri = pygame.image.load('geri press.png')
        if geri_changer == False:
            geri = pygame.image.load('geri.png')

        screen.blit(helenizm_info,[0,200])
        screen.blit(helen_foto,[300,400])
        screen.blit(geri,[25,25])
        pygame.display.update()


def ekomake():
    eko_info = pygame.image.load('eko info.png')
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
            geri = pygame.image.load('geri press.png')
        if geri_changer == False:
            geri = pygame.image.load('geri.png')

        screen.blit(eko_info,[0,200])
        screen.blit(geri,[25,25])
        pygame.display.update()


def toplim():
    toplum_info = pygame.image.load('toplum info.png')
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
            geri = pygame.image.load('geri press.png')
        if geri_changer == False:
            geri = pygame.image.load('geri.png')

        screen.blit(toplum_info,[0,200])
        screen.blit(geri,[25,25])
        pygame.display.update()
         

        

opening_screen()
        
