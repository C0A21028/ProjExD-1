from os import scandir

import random
from re import S
import tkinter.messagebox as tkm
import pygame as pg
import sys
import tkinter as tk

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
gara = ["CL","HT","SP","DI"]
jisyo = {"CL":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "HT":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "SP":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "DI":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]}
pw = 0
dw = 0

def bgm():
    bgm_file = "./ProjExD/ex06/fig/bgm.wav"
    sounds = pg.mixer.Sound(bgm_file)
    sounds.play(loops = -1)
    pg.mixer.music.set_volume(0.6)


def se_card_open():
    bgm_file = "./ProjExD/ex06/fig/card_open.mp3"
    sounds = pg.mixer.Sound(bgm_file)
    sounds.play(1)


class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(image)
        self.bgi_rct = self.bgi_sfc.get_rect()
    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)

class Fuda:
    def __init__(self,hand:list,label:list,hito):
        self.sfc1 = pg.image.load(f"./ProjExD/ex06/トランプ/{label[0]}/{hand[0]}_{label[0]}.png")
        self.sfc1 = pg.transform.rotozoom(self.sfc1, 0, 0.15)
        self.rct1 = self.sfc1.get_rect()
        self.y = 0
        if hito == 'P':
            self.y = 700
        else:
            self.y = 100
        self.rct1.center = (725,self.y)
        self.sfc2 = pg.image.load(f"./ProjExD/ex06/トランプ/{label[1]}/{hand[1]}_{label[1]}.png")
        self.sfc2 = pg.transform.rotozoom(self.sfc2, 0, 0.15)
        self.rct2 = self.sfc2.get_rect()
        self.rct2.center = (875,self.y)
    def blit(self,scr:Screen):
        scr.sfc.blit(scr.sfc,scr.rct)
    def update(self,scr:Screen):
        scr.sfc.blit(self.sfc1,self.rct1)
        scr.sfc.blit(self.sfc2,self.rct2)
        self.blit(scr)


class Tuika:
    def __init__(self,hand,label,x,player_hit_count):
        self.sfc = pg.image.load(f"./ProjExD/ex06/トランプ/{label[0]}/{hand[0]}_{label[0]}.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.15)
        self.rct = self.sfc.get_rect()
        if player_hit_count == 1:
            mod = x + 160
        else:
            mod = x + 75
        self.rct.center = (mod,700)
    def blit(self,scr:Screen):
        scr.sfc.blit(scr.sfc,scr.rct)
    def update(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
        self.blit(scr)


class Tuika_d:
    def __init__(self,hand,label,x):
        self.sfc = pg.image.load(f"./ProjExD/ex06/トランプ/{label[0]}/{hand[0]}_{label[0]}.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.15)
        self.rct = self.sfc.get_rect()
        self.rct.center = (x,100)
    def blit(self,scr:Screen):
        scr.sfc.blit(scr.sfc,scr.rct)
    def update(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)


class Hit_s:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)  
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()  
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


class Stand_s:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)  
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()  
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


class Ura:
    def __init__(self,x,y):
        self.sfc = pg.image.load("./ProjExD/ex06/トランプ/card_back.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.4)
        self.rct = self.sfc.get_rect()
        self.rct.center=(x,y)
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)


class Deck:
    def __init__(self,image):
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.4)
        self.rct = self.sfc.get_rect()
        self.rct.center = (1400,450)
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)


class Score:
    def __init__(self, size, color, xy, win):
        self.fonto = pg.font.Font("./ProjExD/ex06/トランプ/JKG-L_3.ttf", size)                          
        self.sfc = self.fonto.render(f"勝利数{win}", True, color) 
        self.rct = self.sfc.get_rect()                                 
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


class Mytotal:
    def __init__(self, size, color, xy, total):
        self.fonto = pg.font.Font("./ProjExD/ex06/トランプ/JKG-L_3.ttf", size)                          
        self.sfc = self.fonto.render(f"今の手札の合計:{total}", True, color) 
        self.rct = self.sfc.get_rect()                                 
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


def main():
    global pw, dw
    bgm()
    clock = pg.time.Clock()
    scr = Screen("black Jack",(1600,900),"./ProjExD/ex06/トランプ/bg.jpg")
    hit_s = Hit_s("./ProjExD/ex06/トランプ/hit.png", 0.3, (1400,600))
    std_s = Stand_s("./ProjExD/ex06/トランプ/stand.png", 0.3, (1400,750))
    play_s= Stand_s("./ProjExd/ex06/トランプ/play.png",0.3,(1400,450))
    BAK = Ura(875,100)
    score = Score(60, (0 ,0 , 0), (200, 100), pw)
    dealer_kigo,dealer_hand = deal()
    player_kigo,player_hand = deal()
    player_total = total(player_hand[0])+total(player_hand[1])
    dealer_total = total(dealer_hand[0])+total(dealer_hand[1])
    ur = Ura(1400,450)
    print(player_kigo)
    player_CL = Fuda(player_hand,player_kigo,'P')
    dealer_CL = Fuda(dealer_hand,dealer_kigo,'D')
    player_hit_count = 0
    countd = 0
    m = 0
    kb = 1
    j = 0
    posi_x = player_CL.rct2.centerx
    hit_list = []
    x1 = player_CL.rct1.centerx
    kktd = []
    key_type = False

    while True:
        scr.blit()
        if key_type == True:
            hit_s.blit(scr)
            std_s.blit(scr)
            ur.blit(scr)
            m = 1
        else:
            play_s.blit(scr)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if play_s.rct.collidepoint(event.pos):
                    key_type = True
                    kb = True
                if hit_s.rct.collidepoint(event.pos):
                    se_card_open()
                    ga,ph = deal2()
                    player_hit_count += 1
                    player_total += total(ph[0])
                    if player_hit_count >= 2:
                        player_hit_count = 2
                if std_s.rct.collidepoint(event.pos):
                    se_card_open()
                    kb = 0
                    while (dealer_total < 17):
                        gad,phd = deal2()
                        countd += 1
                        dealer_total += total(phd[0])
                        dealer_CL.rct1.centerx -= 100
                        dealer_CL.rct2.centerx -= 100
                        kktd.append(Tuika_d(phd,gad,1000))
                        for j in kktd:
                            while True:
                                j.rct.centerx -= 10
                                if j.rct.centerx <= posi_x - 75:
                                    break
                        player_hit_count = 0
                    j = 1
            
               
        if m == 1:
            player_CL.update(scr)
            dealer_CL.update(scr)
            mytotal = Mytotal(40, (0 ,0 , 0), (200, 700), player_total)
            mytotal.blit(scr)
            dltotal = Mytotal(40, (0 ,0 , 0), (200, 400), dealer_total)
            dltotal.blit(scr)
        if kb:
            BAK.blit(scr)
        if player_hit_count >= 1:
            player_CL.rct1.centerx -= 10
            player_CL.rct2.centerx -= 10
            if player_CL.rct1.centerx<=x1-75/2:
                player_CL.rct1.centerx = player_CL.rct1.centerx - 75/2
                player_CL.rct2.centerx = player_CL.rct1.centerx + 150
                hit_list.append(Tuika(ph,ga,posi_x,player_hit_count))
                for j in hit_list:
                    posi_x = j.rct.centerx
                    while True:
                        j.rct.centerx -= 10
                        if j.rct.centerx <= posi_x - 75:
                            break
                x1 = player_CL.rct1.centerx
                player_hit_count = 0
        for i in hit_list:
            i.update(scr)
        for i in kktd:
            i.update(scr)
        pg.display.update()
        clock.tick(1000)

        if j == 1:
            judge(player_total, dealer_total)
        if pw == 5 or dw == 5:
            tkm.showinfo("game over","ゲームを終了します")
            pg.quit()
            sys.exit()


def deal():
    global gara,jisyo
    hand = []
    kis = []
    for i in range(2):
        m = random.randint(0,3)
        ki = gara[m]
        ho = jisyo[ki]
        random.shuffle(ho)
        card = ho.pop()
        jisyo.update({ki:ho})
        kis.append(ki)
        hand.append(card)
    return kis,hand

def deal2():
    global gara,jisyo
    hand = []
    kis = []
    m = random.randint(0,3)
    ki = gara[m]
    ho = jisyo[ki]
    random.shuffle(ho)
    card = ho.pop()
    jisyo.update({ki:ho})
    kis.append(ki)
    hand.append(card)
    return kis,hand


def judge(n1, n2):
    global pw, dw
    if (n1 > 21) and (n2 > 21):
        tkm.showinfo("ドロー", "両者バーストです")
        main()
    elif (n1 > n2) or (n2 > 21):
        pw += 1
        tkm.showinfo("勝ち", "あなたの勝ちです")
        main()
    else :
        dw += 1
        tkm.showinfo("負け", "あなたの負けです")
        main()

def total(hand):
    if hand >= 10:
        score = 10
    else:
        score = hand
    return score


if __name__=="__main__":
    pg.init()
    root = tk.Tk()
    root.withdraw()
    main()
