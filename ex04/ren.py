import pygame as pg
import sys


def main():
    pg.display.set_caption("初めてのPygame")
    screen=pg.display.set_mode(800,600)
    tori_img=pg.image("./ex04/fig/pg_bg.jpg")
    tori_rect=tori_img.get_rect()
    tori_rect.center=900,400
    screen.blit(tori_img,tori_rect)

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
