# SOFA 评分系统，分级选择法
from tkinter import *
from tkinter.ttk import Separator
root = Tk()
ww = 800
wh = 600
screeWidth = root.winfo_screenwidth()
screeHeight = root.winfo_screenheight()
wx = (screeWidth - ww)/2
wy = (screeHeight - wh)/2
root.geometry('%dx%d+%d+%d'%(ww,wh,wx,wy))
root.title('SOFA评分系统')

wid = 12  #定义grid 的宽度

#标题行
Label(root,text = 'SOFA评分系统', font = 'Helvetic 20 bold').grid(column = 0,row =0,columnspan =8)

#分割线
Separator(root, orient = HORIZONTAL).grid(row=1,column = 0,columnspan =8,sticky = W+E)

# 项目列表行
row1 = ['系统','项目','0分','1分','2分','3分','4分','得分']
colu = 0
for i in row1:
    Label(root,text=i,width =wid).grid(row =2 ,column = colu)
    colu +=1
    
#分割线
Separator(root, orient = HORIZONTAL).grid(row=3,column = 0,columnspan =8,sticky = W+E)

# 呼吸系统
row4 =['呼吸','PO2/FiO2','>=400','<400','<300','<200','<100']
Label(root,text=row4[0]).grid(row =4 ,column = 0)
Label(root,text=row4[1]).grid(row =4 ,column = 1)
r=0
colu=2
v1 = IntVar()
for i in row4[2:]:
    Radiobutton(root, text =i,variable = v1,value =r).grid(row =4 ,column = colu)
    r+=1
    colu+=1
    
#分割线
Separator(root, orient = HORIZONTAL).grid(row=5,column = 0,columnspan =8,sticky = W+E)

# 凝血系统
row6 =['凝血','PLT','>=150','<150','<100','<50','<20']
Label(root,text=row6[0]).grid(row =6 ,column = 0)
Label(root,text=row6[1]).grid(row =6 ,column = 1)
r=0
colu=2
v2 = IntVar()
for i in row6[2:]:
    Radiobutton(root, text =i,variable = v2,value =r).grid(row =6 ,column = colu)
    r+=1
    colu+=1
#分割线
Separator(root, orient = HORIZONTAL).grid(row=7,column = 0,columnspan =8,sticky = W+E)

# 肝脏
row8 =['肝脏','胆红素','<20.5','<=34.1','<=102.5','<=205.1','>205.2']
Label(root,text=row8[0]).grid(row =8 ,column = 0)
Label(root,text=row8[1]).grid(row =8 ,column = 1)
r=0
colu=2
v3 = IntVar()
for i in row8[2:]:
    Radiobutton(root, text =i,variable = v3,value =r).grid(row =8 ,column = colu)
    r+=1
    colu+=1
#分割线
Separator(root, orient = HORIZONTAL).grid(row=9,column = 0,columnspan =8,sticky = W+E)

# 循环系统
row10=['循环','平均动脉压（mmHg）','>=70','<70']
row11=['多巴胺（ug/kg*min）','<=5','>5','>15']
row12=['多巴酚丁胺（ug/kg*min）','任何剂量']
row13=['肾上腺素（ug/kg*min）','<=0.1','>0.1']
row14=['去甲肾上腺素（ug/kg*min）','<=0.1','>0.1']
Label(root,text=row10[0]).grid(row = 10, column = 0, rowspan =5)
Label(root,text=row10[1]).grid(row = 10 ,column = 1)
Label(root,text=row11[0]).grid(row = 11 ,column = 1)
Label(root,text=row12[0]).grid(row = 12 ,column = 1)
Label(root,text=row13[0]).grid(row = 13 ,column = 1)
Label(root,text=row10[0]).grid(row = 14 ,column = 1)
v4 = IntVar()
Radiobutton(root, text = row10[2], variable = v4, value = 0).grid(row = 10, column = 2)
Radiobutton(root, text = row10[3], variable = v4, value = 1).grid(row = 10, column = 3)
Radiobutton(root, text = row11[1], variable = v4, value = 2).grid(row = 11, column = 4)
Radiobutton(root, text = row11[2], variable = v4, value = 3).grid(row = 11, column = 5)
Radiobutton(root, text = row11[3], variable = v4, value = 4).grid(row = 11, column = 6)
Radiobutton(root, text = row12[1], variable = v4, value = 5).grid(row = 12, column = 4)
Radiobutton(root, text = row13[1], variable = v4, value = 6).grid(row = 13, column = 5)
Radiobutton(root, text = row13[2], variable = v4, value = 7).grid(row = 13, column = 6)
Radiobutton(root, text = row14[1], variable = v4, value = 8).grid(row = 14, column = 5)
Radiobutton(root, text = row14[2], variable = v4, value = 9).grid(row = 14, column = 6)
#分割线
Separator(root, orient = HORIZONTAL).grid(row=15,column = 0,columnspan =8,sticky = W+E)

# 神经系统
row16 =['神经','GCS评分','15','13-14','10-12','6-9','<6']
Label(root,text=row16[0]).grid(row =16 ,column = 0)
Label(root,text=row16[1]).grid(row =16 ,column = 1)
r=0
colu=2
v5 = IntVar()
for i in row16[2:]:
    Radiobutton(root, text =i,variable = v5,value =r).grid(row =16 ,column = colu)
    r+=1
    colu+=1
#分割线
Separator(root, orient = HORIZONTAL).grid(row=17,column = 0,columnspan =8,sticky = W+E)

# 肾功能
row18 =['肾脏','肌酐（umol/L）','<106','<=176','<=308','<=442','>442']
row19 =['尿量（ml/d）','<=500','<=200']
Label(root,text=row18[0]).grid(row =18 ,column = 0)
Label(root,text=row18[1]).grid(row =18 ,column = 1)
Label(root,text=row19[0]).grid(row =19 ,column = 1)
r=0
colu=2
v6 = IntVar()
for i in row18[2:]:
    Radiobutton(root, text =i,variable = v6,value =r).grid(row =18 ,column = colu)
    r+=1
    colu+=1
Radiobutton(root, text =row19[1],variable = v6,value =5).grid(row =19 ,column = 5)
Radiobutton(root, text =row19[2],variable = v6,value =6).grid(row =19 ,column = 6)
#分割线
Separator(root, orient = HORIZONTAL).grid(row=20,column = 0,columnspan =8,sticky = W+E)

# 评分计算
#    设置分项得分
vc1 = StringVar()
vc2 = StringVar()
vc3 = StringVar()
vc4 = StringVar()
vc5 = StringVar()
vc6 = StringVar()
vc7 = StringVar()
Label(root, textvariable = vc1).grid(row = 4, column =7)
Label(root, textvariable = vc2).grid(row = 6, column =7)
Label(root, textvariable = vc3).grid(row = 8, column =7)
Label(root, textvariable = vc4).grid(row = 10, column =7, rowspan = 5)
Label(root, textvariable = vc5).grid(row = 16, column =7)
Label(root, textvariable = vc6).grid(row = 18, column =7, rowspan = 2)
Label(root, textvariable = vc7, font ='黑体 18 bold').grid(row = 21, column =7)

def coculate():
    vc1.set(str(v1.get()))
    vc2.set(str(v2.get()))
    vc3.set(str(v3.get()))

    if v4.get()<5:
        f4 = v4.get()
    elif 5<=v4.get()<8:
        f4 = v4.get()-3
    else:
        f4 = v4.get()-5
    vc4.set(str(f4))

    vc5.set(str(v5.get()))

    if v6.get()<5:
        f6 = v6.get()
    else:
        f6 = v6.get()-2
    vc6.set(str(f6))
    vc7.set(str(v1.get()+v2.get()+v3.get()+f4+v5.get()+f6))
Label(root,text='SOFA评分=',font ='黑体 15 bold').grid(column =6, row =21)

B = Button(root, text = '进行评分', font = '黑体 15 bold',command = coculate, width = 8, height = 2)
B.grid(row = 21, column = 2)

# 患者信息登记
""" Label(root, text ='床号').grid(column =0, row = 22)
Label(root, text ='住院号').grid(column =0, row = 23)
Label(root, text ='姓名').grid(column =0, row = 24)
Label(root, text ='性别').grid(column =0, row = 25)
Label(root, text ='年龄').grid(column =0, row = 26) """

root.mainloop()
