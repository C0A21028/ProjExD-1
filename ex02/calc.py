
from ast import Num
import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

def button_click(event):
    btn=event.widget
    num=btn["text"]
    if num=="=":
        kei=entry.get()
        res=eval(kei)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    elif num=="C":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,num)

if __name__ == "__main__":

    root=tk.Tk()
    root.title("お試し")

    entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=0,column=1,columnspan=10)

    
    for l,i in enumerate([9,8,7,6,5,4,3,2,1,0,"+","-","=","C"]):
        button=tk.Button(root,text=f"{i}",
                        font=("Helvetica",30),
                        width=4,height=1,
                        command=button_click)
        button.bind("<1>",button_click)
        k=l%3+1
        j=l//3+1
        button.grid(row=j,column=k)

    root.mainloop()
