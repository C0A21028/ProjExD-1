print("hello world")

import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

root=tk.Tk()
root.title("お試し")
root.geometry("500x350")
label=tk.Label(root,
text="ラベルを書いてみた",
font=("Helvetica",30))
label.pack()
button=tk.Button(root,text="押せ",font=("Helvetica",30),command=button_click)
button.bind("<1>",button_click)
button.pack()
entry=tk.Entry(width=40)
entry.insert(tk.END,"fugapiyo")
entry.pack()
root.mainloop()