# 内生肌酐清除率计算器 根据 Cockcoft 公式 Ccr=[(140-年龄)*体重（kg）/[0.818*scr(umol/L)]]
# 女生按计算结果*0.85
import time
y = 1
wrong = '输入错误！！！，请重新输入'
# 1.提醒软件版本
def copyright_mw():
    edition = 'Ccr Calcultor 2.0 内生肌酐清除率粗算器 2019-12-24'
    copyright = 'Powered by 马旺 天津人民医院  MICU。 马旺 保留所有权利'
    print('=' * 60 + '\n' + edition + '\n' + copyright + '\n' +'根据 Cockcoft 公式 Ccr=[(140-年龄)*体重（kg）/[0.818*scr(umol/L)]]'+'\n'+'=' * 60)

def try_int_input(key):
    try:
        t = int(key)
    except Exception as e:
        print(e)
        print(wrong)
        return 0
    else:
        return 1

def gender_input():
    global g
    while True:
        gender = input('请输入患者性别（1男，2女）：')
        w = try_int_input(gender)
        if w == 0:
            continue
        else:
            g = int(gender)
            if g != 1 and g != 2:
                print('中国不承认其它性别！请输入1或2')
            else:
                print('OK!')
                break

def age_input():
    global a
    while True:
        age = input('请输入患者年龄（岁）：')
        w = try_int_input(age)
        if  w == 0:
            continue
        else:
            a = int(age)
            if a < 1 or a > 130:
                print('年龄超范围!!!')
            else:
                print('OK!')
                break

def weight_input():
    global w
    while True:
        weight = input('请输入患者体重（kg）：')
        v = try_int_input(weight)
        if v == 0:
            continue
        else:
            w = float(weight)
            if w < 10 or w > 200:
                print('体重超范围!!!')
            else:
                print('OK!')
                break

def cr_input():
    global c
    while True:
        cr = input('请输入患者肌酐值(mmol/L)：')
        w = try_int_input(cr)
        if w == 0:
            continue
        else:
            c = float(cr)
            if c < 0 or c > 3000:
                print('肌酐超范围!!!')
            else:
                print('OK!')
                break
def again():
    global y
    n = input('是否再次进行其它计算？（1 = 是 ,其它 = 否）')
    if n != '1':
        y = 0
        print('Goodby!  '*3)
    else:
        y =1
        print('='*60)

def main():
    copyright_mw()
    while y == 1:
        age_input()
        gender_input()
        weight_input()
        cr_input()
        if g == 1:
            ccr = (140 - a) * w / (0.818 * c)
        else:
            ccr = ((140 - a) * w / (0.818 * c)) * 0.85
        print('该患者的内生肌酐清除率估算值为：' + str(ccr))
        time.sleep(2)
        print('='*60)
        again()
main()
