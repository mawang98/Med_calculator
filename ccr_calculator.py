# 内生肌酐清除率计算器 根据 Cockcoft 公式 Ccr=[(140-年龄)*体重（kg）/[0.818*scr(umol/L)]]
# 女生按计算结果*0.85
import time

# 提醒软件版本: Ccr Calcultor 1.0 Powered by Ma wang
edition = 'Ccr Calcultor 1.0 内生肌酐清除率粗算器 2019-12-3'
copyright = 'Powered by 马旺 天津人民医院  MICU。 马旺 保留所有权利'
print('=' * 60 + '\n' + edition + '\n' + copyright + '\n' +'根据 Cockcoft 公式 Ccr=[(140-年龄)*体重（kg）/[0.818*scr(umol/L)]]'+'\n'+'=' * 60)
# 开始输入参数
wrong = '输入错误'
while 11:
    while 1:
        gender = input('请输入患者性别（1男，2女）：')
        try:
            g = int(gender)
        except Exception as e :
            print(e)
            print(wrong+'!!!  请输入1或2')
        else :
            if g != 1 and g != 2:
                print('中国不承认其它性别！请输入1或2')
            else:
                print('OK!')
                break
    while 2 :
        age = input('请输入患者年龄（岁）：')
        try:
            a = int(age)
        except Exception as e1:
            print(e1)
            print(wrong+'!!!  请输入正确的年龄数字')
        else:
            if a < 1 or a > 130:
                print('年龄超范围!!!')
            else:
                print('OK!')
                break
    while 3:
        weight = input('请输入患者体重（kg）：')
        try :
            w = float(weight)
        except Exception as e2:
            print(e2)
            print(wrong+'!!!  请输入正确的体重')
        else:
            if w < 10 or w > 200:
                print('体重超范围!!!')
            else:
                print('OK!')
                break
    while 4:
        cr = input('请输入患者肌酐值(mmol/L)：')
        try:
            c = float(cr)
        except Exception as e3:
            print(e3)
            print(wrong+'!!!  请输入正确的血肌酐数值')
        else:
            if c < 0 or c > 3000:
                print('肌酐超范围!!!')
            else:
                print('OK!')
                break
    ccr = 1.00
    if g == 1:
        ccr = (140 - a) * w / (0.818 * c)
    else:
        ccr = ((140 - a) * w / (0.818 * c)) * 0.85
    print('该患者的内生肌酐清除率估算值为：' + str(ccr))
    time.sleep(2)
    print('='*60)
    n=input('是否再次进行其它计算？（1： 是 其它： 否）')
    if n != '1':
        print('GoodBye!'*3)
        time.sleep(3)
        break
