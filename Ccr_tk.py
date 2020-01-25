from tkinter import *

root = Tk()
ww = 330
wh = 350
screeWidth = root.winfo_screenwidth()
screeHeight = root.winfo_screenheight()
wx = (screeWidth - ww)/2
wy = (screeHeight - wh)/2
root.geometry('%dx%d+%d+%d'%(ww,wh,wx,wy))
root.title('内生肌酐清除率粗算器')

l0 = Label(root)
l1 = Label(root,text ='年龄（岁）：')
l2 = Label(root,text ='体重（Kg）：')
l3 = Label(root,text ='血肌酐（mmol/L）：')
l5 = Label(root,text = '性别:')

l0.grid(row=0)
l1.grid(column = 0, row = 1, sticky = W,padx = 5)
l2.grid(column = 0, row = 2, sticky = W,padx = 5)
l3.grid(column = 0, row = 3, sticky = W,padx = 5)
l5.grid(column = 0, row = 4, sticky = W,padx = 5)

ex1 = StringVar()
ex2 = StringVar()
ex3 = StringVar()
e1 = Entry(root,textvariable = ex1)
e2 = Entry(root,textvariable = ex2)
e3 = Entry(root,textvariable = ex3)
e1.grid(column = 1, row = 1, sticky = W)
e2.grid(column = 1, row = 2, sticky = W)
e3.grid(column = 1, row = 3, sticky = W)

rx = IntVar()
rx.set(1)
r1 = Radiobutton(root,text = '男',variable = rx,value = 1)
r2 = Radiobutton(root,text = '女',variable = rx,value = 2)
r1.grid(column = 1, row = 4, sticky = W)
r2.grid(column = 1, row = 4, sticky = E)

def cacul():
    r = rx.get()
    a = ex1.get()
    w = ex2.get()
    c = ex3.get()
    if r == 1:
        ccr = (140 - int(a)) * float(w) / (0.818 * float(c))
    else:
        ccr = ((140 - int(a)) * float(w) / (0.818 * float(c)))*0.85
    lx1.set('Ccr ='+str(ccr)+'ml/min')

lx1 = StringVar()
l4 = Label(root, textvariable = lx1,bg = 'yellow',width = 30,height =2)
l4.grid(column = 0, columnspan = 3, row = 7, padx = 15,pady = 20)

l6 = Label(root,text = '软件版权：天津人民医院MICU-马旺')
l6.grid(column = 0, columnspan = 3, row = 8, sticky = W+S, pady =20)

l7 = Label(root,text ='注：该方法为粗算估计，误差较大，请谨慎应用！',fg = 'red')
l7.grid(column = 0, columnspan = 3, row = 9, sticky = W+S)

b1= Button(root,text = '计算',command = cacul,width = 8)
b1.grid(column = 1, row = 5)

root.mainloop()
