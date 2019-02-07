import pygame

pygame.init()
pygame.mixer.init()

WIDTH = 1300
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption ('img/Paranin Cinleri - Murathan Mungan')

#renkler/colors
green = (0, 255, 0)
red = (255,0,0)
cogirenk = (200,150,20)

#resimler/images
Backg1 = pygame.image.load ('img/mungan.png')
Backg2 = pygame.image.load ('img/Muratcim.png')

geri = pygame.image.load ('img/geri.png')

mehtap = pygame.image.load ('img/Mehtapligeceler.png')
mehtap_pressed = pygame.image.load ('img/Mehtapligecelerpressed.png')

yasam = pygame.image.load ('img/Munganyasam.png')
yasam_pressed = pygame.image.load ('img/Munganyasampressed.png')

bellek = pygame.image.load ('img/Ortakbellek.png')
bellek_pressed = pygame.image.load ('img/Ortakbellekpressed.png')

anilar = pygame.image.load ('img/Anilar.png')
anilar_pressed = pygame.image.load ('img/Anilarpressed.png')

aile = pygame.image.load ('img/Aile.png')
aile_pressed = pygame.image.load ('img/Ailepressed.png')

kapakfoto = pygame.image.load ('img/Kapakfoto.png')
munganAlıntı = pygame.image.load ('img/munganalinti.png')
mehtapfoto = pygame.image.load ('img/Mehtap.png')
Mehtapyazi = pygame.image.load ('img/Mehtapyazi.png')
mardin = pygame.image.load ('img/Mardin.png')
ailebck = pygame.image.load ('img/murathanmunganaile3.png')
pano = pygame.image.load ('img/pano.png')
aile1 = pygame.image.load ('img/aileyazi11.png')
aile2 = pygame.image.load ('img/aileyazi12.png')
aile3 = pygame.image.load ('img/aileyazi13.png')
mardinso = pygame.image.load ('img/mardinso.png')
ani1 = pygame.image.load ('img/ani11.png')
ani2 = pygame.image.load ('img/ani12.png')
ani3 = pygame.image.load ('img/ani13.png')
ani4 = pygame.image.load ('img/ani14.png')
bellek1 = pygame.image.load ('img/ortakbellek11.png')
bellek2 = pygame.image.load ('img/ortakbellek12.png')
sahmeran = pygame.image.load ('img/sahmeran.png')
peceli = pygame.image.load ('img/peceli.png')
yasam1 = pygame.image.load ('img/yasam11.png')
yasam2 = pygame.image.load ('img/yasam12.png')
yasam3 = pygame.image.load ('img/yasam13.png')
baslikaile = pygame.image.load ('img/baslikaile.png')
baslikanilar = pygame.image.load ('img/baslikanilar.png')
baslikbellek = pygame.image.load ('img/baslikbellek.png')
baslikcevre = pygame.image.load ('img/baslikcevre.png')
#pygame.mixer.music.load ("Helloworld.wav")
#pygame.mixer.music.play (-1)


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


def yunanistani():
    yunanistan_info = pygame.image.load ('img/yunanistaninfo.png')
    yunanistan_harita = pygame.image.load ('img/yunanistanharita.png')
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
                 
        else:
            geri_changer2 = False


        if geri_changer2 == True:
            geri = pygame.image.load ('img/geripress.png')
        if geri_changer2 == False:
            geri = pygame.image.load ('img/geri.png')

        screen.blit(yunanistan_info,[0,200])
        screen.blit(geri,[125,25])
        screen.blit(yunanistan_harita,[425,500])
        pygame.display.update()

        
def anadolui():
    anadolu_info = pygame.image.load ('img/anadoluinfo.png')
    anadolu_harita = pygame.image.load ('img/anadoluharita.png')
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
                 
        else:
            geri_changer2 = False


        if geri_changer2 == True:
            geri = pygame.image.load ('img/geripress.png')
        if geri_changer2 == False:
            geri = pygame.image.load ('img/geri.png')

        screen.blit(anadolu_info,[0,200])
        screen.blit(geri,[125,25])
        screen.blit(anadolu_harita,[400,500])
        pygame.display.update()

def mezopotamyai():
    mezopotamya_info = pygame.image.load ('img/mezopotamyainfo.png')
    mezopotamya_harita = pygame.image.load ('img/mezopotamyaharita.png')
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
                 
        else:
            geri_changer2 = False


        if geri_changer2 == True:
            geri = pygame.image.load ('img/geripress.png')
        if geri_changer2 == False:
            geri = pygame.image.load ('img/geri.png')

        screen.blit(mezopotamya_info,[0,200])
        screen.blit(geri,[125,25])
        screen.blit(mezopotamya_harita,[400,490])
        pygame.display.update()

def misiri():
    misir_harita = pygame.image.load ('img/misirharita.png')
    misir_info = pygame.image.load ('img/misirinfo.png')
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
                 
        else:
            geri_changer2 = False


        if geri_changer2 == True:
            geri = pygame.image.load ('img/geripress.png')
        if geri_changer2 == False:
            geri = pygame.image.load ('img/geri.png')

        screen.blit(misir_info,[0,200])
        screen.blit(geri,[125,25])
        screen.blit(misir_harita,[400,500])
        pygame.display.update()


def asyai():
    asya_harita = pygame.image.load ('img/asyaharita.png')
    asya_info = pygame.image.load ('img/asyainfo.png')
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
                 
        else:
            geri_changer2 = False


        if geri_changer2 == True:
            geri = pygame.image.load ('img/geripress.png')
        if geri_changer2 == False:
            geri = pygame.image.load ('img/geri.png')

        screen.blit(asya_info,[0,200])
        screen.blit(geri,[125,25])
        screen.blit(asya_harita,[400,400])
        pygame.display.update()




def opening_screen():
    start = False
    mehtap_changer = False
    yasam_changer = False
    bellek_changer = False
    anilar_changer = False
    aile_changer = False
    while not start:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        if 100 < mouse[0] <  348 and 100 < mouse[1] < 124:
            mehtap_changer = True
            if click[0] == 1:
                mehtapi()
        else:
            mehtap_changer = False

        if 100 < mouse[0] <  384 and 200 < mouse[1] < 224:
            yasam_changer = True
            if click[0] == 1:
                yasami()
        else:
            yasam_changer = False

        if 100 < mouse[0] <  216 and 300 < mouse[1] < 324:
            bellek_changer = True
            if click[0] == 1:
                belleki()
        else:
            bellek_changer = False

        if 100 < mouse[0] <  172 and 400 < mouse[1] < 424:
            anilar_changer = True
            if click[0] == 1:
                anii()
        else:
            anilar_changer = False

        if 100 < mouse[0] <  174 and 500 < mouse[1] < 524:
            aile_changer = True
            if click[0] == 1:
                ailei()
        else:
            aile_changer = False

            



        if mehtap_changer == True:
            mehtap = pygame.image.load ('img/Mehtapligecelerpressed.png') 
        if mehtap_changer == False:
            mehtap = pygame.image.load ('img/Mehtapligeceler.png')

        if yasam_changer == True:
            yasam = pygame.image.load ('img/Munganyasampressed.png')
        if yasam_changer == False:
            yasam = pygame.image.load ('img/Munganyasam.png')

        if bellek_changer == True:
            bellek = pygame.image.load ('img/Ortakbellekpressed.png')
        if bellek_changer == False:
            bellek = pygame.image.load ('img/Ortakbellek.png')

        if anilar_changer == True:
            anilar = pygame.image.load ('img/Anilarpressed.png')
        if anilar_changer == False:
            anilar = pygame.image.load ('img/Anilar.png')

        if aile_changer == True:
            aile = pygame.image.load ('img/Ailepressed.png')
        if aile_changer == False:
            aile = pygame.image.load ('img/Aile.png')




            
        screen.blit(Backg1,[0,0])
        screen.blit(Backg2,[650,0])
        screen.blit(mehtap,[100,100])           
        screen.blit(yasam,[100,200])
        screen.blit(bellek,[100,300])
        screen.blit(anilar,[100,400])
        screen.blit(aile,[100,500])
        screen.blit(kapakfoto,[500,300])
        screen.blit(munganAlıntı,[750,550])
        pygame.display.update()



def mehtapi():
    geri = pygame.image.load ('img/geri.png')
    cogi = True
    yunanistan_changer = False
    anadolu_changer = False
    mezopotamya_changer = False
    misir_changer = False
    asya_changer = False
    geri_changer = False
    
    while cogi:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(mehtapfoto,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if 25 < mouse[0] < 105 and 25 < mouse[1] < 59:
            geri_changer = True
            if click[0] == 1:
                opening_screen()
        else:
            geri_changer = False

        if geri_changer == True:
            geri = pygame.image.load ('img/geripress.png')
        if geri_changer == False:
            geri = pygame.image.load ('img/geri.png')




        screen.blit(Mehtapyazi,[270,200])
        screen.blit(geri,[25,25])
        pygame.display.update()





def yasami():
    geri = pygame.image.load ('img/geri.png')
    geri_changer = False
    yonetim = True
    while yonetim:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(mardin,[0,0])

        if 25 < mouse[0] < 105 and 25 < mouse[1] < 59:
            geri_changer = True
            if click[0] == 1:
                opening_screen()
        else:
            geri_changer = False


        if geri_changer == True:
            geri = pygame.image.load ('img/geripress.png')
        if geri_changer == False:
            geri = pygame.image.load ('img/geri.png')
        screen.blit(baslikcevre,[470,10])
        screen.blit(yasam1,[30,170])
        screen.blit(yasam2,[650,170])
        screen.blit(yasam3,[330,270])
        screen.blit(geri,[25,25])
        pygame.display.update()



def ailei():
    geri = pygame.image.load ('img/geri.png')
    geri_changer = False
    heli = True
    while heli:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if 25 < mouse[0] < 105 and 25 < mouse[1] < 59:
            geri_changer = True
            if click[0] == 1:
                opening_screen()
        else:
            geri_changer = False


        if geri_changer == True:
            geri = pygame.image.load ('img/geripress.png')
        if geri_changer == False:
            geri = pygame.image.load ('img/geri.png')

        screen.blit(pano,[0,0])
        screen.blit(ailebck,[-5,-5])
        screen.blit(baslikaile,[500,0])
        screen.blit(aile1,[50,200])
        screen.blit(aile3,[680,200])
        screen.blit(aile2,[280,380])
        screen.blit(geri,[25,25])
        pygame.display.update()


def anii():
    geri = pygame.image.load ('img/geri.png')
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
            geri = pygame.image.load ('img/geripress.png')
        if geri_changer == False:
            geri = pygame.image.load ('img/geri.png')

        screen.blit(pano,[0,0])
        screen.blit(mardinso,[0,0])
        screen.blit(baslikanilar,[150,450])
        screen.blit(ani1,[20,150])
        screen.blit(ani2,[660,150])
        screen.blit(ani3,[20,350])
        screen.blit(ani4,[640,350])
        screen.blit(geri,[25,25])
        pygame.display.update()


def belleki():
    geri = pygame.image.load ('img/geri.png')
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
            geri = pygame.image.load ('img/geripress.png')
        if geri_changer == False:
            geri = pygame.image.load ('img/geri.png')

        screen.blit(pano,[0,0])
        screen.blit(baslikbellek,[310,30])
        screen.blit(bellek1,[30,170])
        screen.blit(bellek2,[640,170])
        screen.blit(sahmeran,[30,280])
        screen.blit(peceli,[700,310])
        screen.blit(geri,[25,25])
        pygame.display.update()
         

        

opening_screen()
        
