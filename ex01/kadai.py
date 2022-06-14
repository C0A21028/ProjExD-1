from random import randint
import datetime
def mondai(k):
    l=[]
    L=[]
    while len(l) < k:
        p=randint(65,90)
        if not p in L:
            L.append(p)
            l.append(chr(p))
    return l
def kesson(l):
    L=int(len(l))
    k=[]
    r=randint(2,5) #何個欠損させるか
    while len(k) < r:
        R=randint(0,L-1)
        if not l[R] in k:
            k.append(l[R])
    return k
def hyouji(l,k):
    o=int(len(k))
    g=0
    while g<o:
        l.remove(k[g])
        g+=1
    return l

def kaito(k):
    while True:
        p=int(input("欠損文字はいくつあるでしょうか？"))
        q=len(k)
        if p==q:
            print("正解です。それでは具体的に欠損文字を1つずつ入力してください")
        else:
            print("不正解です。またチャレンジして下さい")
            break
        u=[]
        for i in range(q):
            m=str(input(f"{i+1}つ目の文字を入力してください"))
            u.append(m)
        count=0
        for i in range(q):
            re=str(u[i]) in k
            if re==True:
                count+=1
                continue
            else:
                print("不正解です。またチャレンジしてください")
                break
        if count==q:
            print("全問正解です。おめでとうございます")
            return True
        break

st = datetime.datetime.now()
for i in range(5):
    print("対象文字")
    l=mondai(10)
    print(l)
    print("欠損文字")
    k=kesson(l)
    print(k)
    print("表示文字")
    h=hyouji(l,k)
    print(h)
    kai=kaito(k)
    if kai==True:
        break
ed = datetime.datetime.now()
print(f"{(ed-st).seconds}かかりました")

