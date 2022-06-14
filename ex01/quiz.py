from random import randint as rad
def shutudai():
    mondai=[["サザエのダンナの名前は？","マスオ","ますお"],
    ["カツオの妹の名前は？","ワカメ","わかめ"],
    ["タラオはカツオから見てどんな関係？","甥","おい","甥っ子","おいっこ"]]
    return mondai

def kaito():
    n=int(rad(0,2))
    p=shutudai()
    print(p[n][0])
    m=str(input("答えるんだ:"))
    c=0
    for i in range(int(len(p[n])-1)):
        if m==str(p[n][i+1]):
            kai="正解!!!"
            c+=1
    if c==0:
        kai="出直してこい"
        c=0
    return kai

s=kaito()
print(s)