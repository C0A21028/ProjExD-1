
import tkinter.messagebox as tkm
import pygame as pg
import sys
import random
import tkinter as tk

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

    kkimg_sfc=pg.image.load("./ex04/fig/3.png")
    kkimg_sfc=pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct=kkimg_sfc.get_rect()
    kkimg_rct.center=900,400

    #練習5
    #数を増やす
    bmimg_sfc=[] #surfaceの空リストを作成
    bmimg_rct=[] #rectの空リストを作成
    vx=[] #vxの空リストを作成
    vy=[] #vyの空リストを作成
    color=[[255,0,0],[0,255,0],[0,0,255],[0,255,255],[255,255,0],[255,0,255]] #色の設定
    for i in range(6):
        bmimg_sfc.append(pg.Surface((20,20)))   #Surfaceリストに追加
        pg.draw.circle(bmimg_sfc[i],(color[i][0],color[i][1],color[i][2]),(10,10),10) #colorから色を取得
        bmimg_rct.append(bmimg_sfc[i].get_rect())   #Rectリストに追加
        bmimg_rct[i].centerx=random.randint(0,screen_rct.width)
        bmimg_rct[i].centery=random.randint(0,screen_rct.height)
        vx.append(1) #vxリストに追加
        vy.append(1) #vyリストに追加
    count=[0,0,0,0,0,0]#countリストを作成。中身は6個で全て0
    bom=random.randint(0,5)#爆弾を設定
    count[bom]=1#爆弾のcountを1に
    bmimg_sfc[bom]=pg.image.load("./ex04/fig/bomb.png")#爆弾の画像を描画
    bmimg_sfc[bom]=pg.transform.rotozoom(bmimg_sfc[bom], 0, 0.05)#画像の大きさを調整
    bmimg_rct[bom]=bmimg_sfc[i].get_rect()#Rectリストを更新
    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        
        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
        #練習4
        move=[pg.K_UP,pg.K_DOWN,pg.K_LEFT,pg.K_RIGHT]
        move2=[[-2,0],[2,0],[0,-2],[0,2]]
        key_states=pg.key.get_pressed()
        for a,m in enumerate(move):
            if key_states[m]==True:
                y,x=move2[a]
                kkimg_rct.centery+=y 
                kkimg_rct.centerx+=x

            if check_bound(kkimg_rct,screen_rct)!=(1,1):
                for j,n in enumerate(move):
                    if key_states[n]==True:
                        y,x=move2[j]
                        kkimg_rct.centery-=y 
                        kkimg_rct.centerx-=x
        #練習6
        #追加機能
        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        for i in range(6):
            bmimg_rct[i].move_ip(vx[i],vy[i])
            screen_sfc.blit(bmimg_sfc[i],bmimg_rct[i])
            yoko,tate=check_bound(bmimg_rct[i],screen_rct)
            vx[i]*=yoko
            vy[i]*=tate
            if kkimg_rct.colliderect(bmimg_rct[i]):#接触したとき
                bmimg_sfc[i].set_colorkey((color[i][0],color[i][1],color[i][2]))#中身の色を消す
                bmimg_rct.append(bmimg_sfc[i].get_rect())#bmimg_rctを更新
                count[i]=1#countのi番目を1にする
                if kkimg_rct.colliderect(bmimg_rct[bom]):#爆弾にあたったとき
                    root = tk.Tk()
                    root.withdraw()
                    tkm.showinfo("ねえ今どんな気持ち？","Game Over")#コメントを表示
                    return
                if (count[0]==1  and count[1]==1 and count[2]==1 and count[3]==1
                    and count[4]==1 and count[5]==1):#爆弾以外のものをすべて取ったとき
                    root = tk.Tk()
                    root.withdraw()
                    pg.display.update()
                    tkm.showinfo("なかなかやるじゃん！","Game Clear")#コメントを表示
                    return
        pg.display.update()
        clock.tick(1000)

def check_bound(rct,scr_rct):
    """
    [1]rct:こうかとん　or 爆弾のRect
    [2]src_rct:スクリーンのRect
    """
    yoko,tate=1,1
    if rct.left<scr_rct.left or rct.right>scr_rct.right:
        yoko=-1
    if rct.top<scr_rct.top or rct.bottom>scr_rct.bottom:
        tate=-1
    return yoko,tate

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
