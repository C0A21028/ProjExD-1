from operator import imod


import pygame as pg
import sys

def main():
    clock=pg.time.Clock()
    pg.display.set_caption("逃げろこうかとん")
    screen_sfc=pg.display.set_mode((1600,900))
    screen_rct=screen_sfc.get_rect()
    bgimg_sfc=pg.image.load("./ex04/fig/pg_bg.jpg")
    bgimg_rct=bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)
    #pg.display.update()
    #clock.tick(0.5)

    kkimg_sfc=pg.image.load("./ex04/fig/6.png")
    kkimg_sfc=pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct=kkimg_sfc.get_rect()
    kkimg_rct.center=900,400

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        
        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
        #練習4
        key_states=pg.key.get_pressed()
        if key_states[pg.K_UP]==True:#上が押されていたなら
            kkimg_rct.centery-=1 #y座標を-1

        if key_states[pg.K_DOWN]==True:#下が押されていたなら
            kkimg_rct.centery+=1 #y座標を+1

        if key_states[pg.K_LEFT]==True:#左が押されていたなら
            kkimg_rct.centerx-=1 #x座標を-1

        if key_states[pg.K_RIGHT]==True:#右が押されていたなら
            kkimg_rct.centerx+=1 #x座標を+1
            
        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        pg.display.update()
        clock.tick(1000)


if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
