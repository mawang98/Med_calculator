from tkinter import *
from tkinter.ttk import Separator
from time import time
import csv
# 主窗体
root = Tk()
ww = 800
wh = 400
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
wx = (screenWidth - ww)/2
wy = (screenHeight - wh)/2
root.geometry('%dx%d+%d+%d'%(ww,wh,wx,wy))
tit = '住院登记系统'
root.title(tit)
# 题头和分割线
r = 0    # 定标0行
Label(root,text =tit,fon ='黑体 20 bold',anchor = 'center').grid(column= 0, row = r, columnspan = 6)
Separator(root, orient = HORIZONTAL).grid(column = 0 ,columnspan = 6, row =r+1, sticky = E+W)
# 登录患者内容
l = ['住院号：','床号：','姓名：','性别：','年龄：','入院主要诊断：']
Label(root, text = l[0]).grid(column = 0 ,row = r+2, sticky = W)
Label(root, text = l[1]).grid(column = 2 ,row = r+2, sticky = W)    # 应改为下拉选择
Label(root, text = l[2]).grid(column = 0 ,row = r+3, sticky = W)
Label(root, text = l[3]).grid(column = 0 ,row = r+4, sticky = W)
Label(root, text = l[4]).grid(column = 0 ,row = r+5, sticky = W)
Label(root, text = l[5]).grid(column = 0 ,row = r+6, sticky = W)

ex1 = StringVar()
ex2 = StringVar()
ex3 = StringVar()
#ex4 = StringVar()
ex5 = StringVar()
ex6 = StringVar()
vx1 = IntVar()
ex = [ex1, ex2, ex3, vx1, ex5, ex6]
Entry(root, textvariable = ex1).grid(column = 1 ,row = r+2, sticky = W)
Entry(root, textvariable = ex2).grid(column = 3 ,row = r+2, sticky = W)
Entry(root, textvariable = ex3).grid(column = 1 ,row = r+3, sticky = W)
Radiobutton(root, text = '男', variable = vx1, value = 1).grid(column = 1 ,row = r+4, sticky = W)
Radiobutton(root, text = '女', variable = vx1, value = 2).grid(column = 1 ,row = r+4, sticky = E)
#Entry(root, textvariable = ex4).grid(column = 3 ,row = r+3, sticky = W)
Entry(root, textvariable = ex5).grid(column = 1 ,row = r+5, sticky = W)
Entry(root, textvariable = ex6, width = 30).grid(column = 1 ,row = r+6, columnspan = 2, sticky = W)

n = 1
def get_admis():
    eg = []
    for i in ex:
        eg.append(i.get())
    k = 0
    for n in eg:
        if n == '' or n == 0:
            k=k+0
        else:
            k=k+1
    if k != 6:
        print(k)
        print('信息不完整，请补足信息')
    else:
        eg.append(time())
        eg.append(n)
        print(eg)
        with open('admission.csv','a',newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(eg)
        with open('admission.csv','r',encoding='utf-8') as rfile:
            reader = csv.reader(rfile)
            inhos = []
            for row in reader:
                if row[-1] == '1':
                    print(row)
                    inhos.append(row)
                print(inhos)
    

Button(root, text = '登记新患者', command = get_admis).grid(column = 0 ,row = r+7,pady =10)
root.mainloop()
