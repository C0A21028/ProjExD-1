
import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global tmr,jid
    tmr=tmr+1
    label["text"]=tmr
    jid=root.after(1000,count_up)

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,f"{txt}ボタンが押されました")

def key_down(event):
    global jid
    if jid!=None:
        root.after_cancel(jid)
        jid=None
        return
    #key=event.keysym
    #tkm.showinfo("キー押下",f"{key}キーが押されました")
    jid=root.after(1000,count_up)

if __name__=="__main__":
    root = tk.Tk()
    label = tk.Label(root,
            text="Hello",
            font=("Times New Roman",80)
            )
    label.pack()
    button=tk.Button(root,text="押すな",command=button_click)
    button.bind("<1>",button_click)
    button.pack()
    tmr=0
    jid=None
    #root.after(1000,count_up)
    root.bind("<KeyPress>",key_down)
    root.mainloop()



