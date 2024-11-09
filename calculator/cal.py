import tkinter as tk
from tkinter import ttk,END,messagebox

win = tk.Tk()
win.geometry("460x350")
win.configure(background="cadet blue")
win.resizable(False,False)


def ansewr():
    disp = ent1.get()

    try:
        result = eval(disp)
        rou = round(result,1)
        ent1.delete(0,END)
        ent1.insert(0,rou)
    
    except ZeroDivisionError:
        messagebox.showerror("error","number can not divided by 0")

    except SyntaxError:
        messagebox.showerror("error","calculation not correct")

def delete():
    ent1.delete(0,END)

def nine(number):
    ent1.insert(END, number)

def eight(number):
    ent1.insert(END,number)

def seven(number):
    ent1.insert(END, number)

def six(number):
    ent1.insert(END,number)

def five(number):
    ent1.insert(END,number)

def four(number):
    ent1.insert(END,number)

def three(number):
    ent1.insert(END,number)

def two(number):
    ent1.insert(END,number)

def one(number):
    ent1.insert(END,number)

def zero(number):
    ent1.insert(END,number)

def plus(num):
    ent1.insert(END,num)

def min(num):
    ent1.insert(END,num)

def mult(num):
    ent1.insert(END,num)

def dot(num):
    ent1.insert(END,num)

def div(num):
    ent1.insert(END,num)

ent1 = tk.Entry(win,bg="light cyan",width=40,font=25)
ent1.grid(row=0,column=0,padx=8,pady=8,columnspan=4)

btn1 = tk.Button(win,text="9",font=10,width=7,cursor="hand2",command=lambda: nine("9"))
btn1.grid(row=1,column=0,padx=8,pady=8)

btn2 = tk.Button(win,text="8",font=10,width=7,cursor="hand2",command=lambda: eight("8"))
btn2.grid(row=1,column=1,padx=8,pady=8)

btn3 = tk.Button(win,text="7",font=10,width=7,cursor="hand2",command=lambda: seven("7"))
btn3.grid(row=1,column=2,padx=8,pady=8)

btn4 = tk.Button(win,text="+",font=10,width=7,cursor="hand2",command=lambda: seven("+"))
btn4.grid(row=1,column=3,padx=8,pady=8)

btn5 = tk.Button(win,text="6",font=10,width=7,cursor="hand2",command=lambda:six("6"))
btn5.grid(row=2,column=0,padx=8,pady=8)

btn6 = tk.Button(win,text="5",font=10,width=7,cursor="hand2",command=lambda:five("5"))
btn6.grid(row=2,column=1,padx=8,pady=8)

btn7 = tk.Button(win,text="4",font=10,width=7,cursor="hand2",command=lambda:four("4"))
btn7.grid(row=2,column=2,padx=8,pady=8)

btn8 = tk.Button(win,text="-",font=10,width=7,cursor="hand2",command=lambda:min("-"))
btn8.grid(row=2,column=3,padx=8,pady=8)

btn9 = tk.Button(win,text="3",font=10,width=7,cursor="hand2",command=lambda:three("3"))
btn9.grid(row=3,column=0,padx=8,pady=8)

btn10 = tk.Button(win,text="2",font=10,width=7,cursor="hand2",command=lambda:two("2"))
btn10.grid(row=3,column=1,padx=8,pady=8)

btn11 = tk.Button(win,text="1",font=10,width=7,cursor="hand2",command=lambda:one("1"))
btn11.grid(row=3,column=2,padx=8,pady=8)

btn12 = tk.Button(win,text="0",font=10,width=7,cursor="hand2",command=lambda:zero("0"))
btn12.grid(row=3,column=3,padx=8,pady=8)

btn13 = tk.Button(win,text="x",font=10,width=7,cursor="hand2",command=lambda:mult("*"))
btn13.grid(row=4,column=0,padx=8,pady=8)
btn14 = tk.Button(win,text=".",font=10,width=7,cursor="hand2",command=lambda:dot("."))
btn14.grid(row=4,column=1,padx=8,pady=8)
btn15 = tk.Button(win,text="/",font=10,width=7,cursor="hand2",command=lambda:div("/"))
btn15.grid(row=4,column=2,padx=8,pady=8)
btn16 = tk.Button(win,text="C",font=10,width=7,cursor="hand2",command=delete)
btn16.grid(row=4,column=3,padx=8,pady=8)


calbtn = tk.Button(win,text="=",width=40,cursor="hand2",command=ansewr)
calbtn.grid(row=5,column=0,padx=8,pady=8,columnspan=4)





win.mainloop()