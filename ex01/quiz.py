from random import randint as rad
def shutudai(n):
    mondai=["サザエのダンナの名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    return mondai[n]

def kaito():
    n=int(rad(0,2))
    p=shutudai(n)
    print(p)
    m=str(input("答えるんだ:"))
    k1=["マスオ","ますお"]
    k2=["ワカメ","わかめ"]
    k3=["甥","おい","甥っ子","おいっこ"]
    c=0
    kai=""
    if n==0:
        for i in range(len(k1)):
            if m==str(k1[i]):
                kai="正解!!!"
                c+=1
    elif n==1:
        for i in range(len(k2)):
            if m==str(k2[i]):
                kai="正解!!!"
                c+=1
    elif n==2:
        for i in range(len(k3)):
            if m==str(k3[i]):
                kai="正解!!!"
                c+=1
    if c==0:
        kai="出直してこい"
        c=0
    return kai

s=kaito()
print(s)