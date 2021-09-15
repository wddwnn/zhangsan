# a=1
# while a<=10:
#     studentlevel ={}
#     name=input("请录入姓名：")
#     score=int(input("请录入成绩："))
#     studentlevel.update(name=name)
#     studentlevel.update(score=score)
#     high={}
#     low={}
#     if score>=60:
#         high.update(score=score)
#     else:
#         low.update(score=score)
#     a=a+1
# print(studentlevel)
# print(high)
# print(low)

#录入成绩并分成大于60与小于60
'''
highchengji={}
lowchengji={}
studentlist=["张三","李四","王五","赵六","陈七","二狗","牛牛","亚索","兮兮","哈哈"]
a=0
while a<len(studentlist):
    chengji=int(input("请输入"+studentlist[a]+"的成绩："))
    if chengji >= 60:
        highchengji[studentlist[a]]=chengji
    else:
        lowchengji[studentlist[a]]=chengji
    a=a+1
print("大于60的：",highchengji)
print("小于60的：",lowchengji)

'''

#打印99乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,end="  ")
    print()    
'''

#通过print打印，模拟一个红绿灯的功能：倒计时，红灯30次，绿的35次，黄灯3次
# red=list(range(1,31))
# green=list(range(1,36))
# yellow=list(range(1,4))

'''
for red in range(1,31):
    print("红灯还有",end="")
    print(31-red,end="")
    print("秒")
for green in range(1,36):
    print("绿灯还有",end="")
    print(36-green,end="")
    print("秒")
for yellow in range(1,4):
    print("黄灯还有",end="")
    print(4-yellow,end="")
    print("秒")

#老师版本
light={"红灯":30,"绿灯"：35,"黄灯”:3}
while True:
    for i in light:
        for j in range(light[i]):
            print(i,"倒计时还有",light[i]-j,"秒")
'''

#使用代码，实现一个注册的功能。用户输入账号和密码，要求账号长度是5~8位，密码6~12位，
# 并且账号必须小写开头，储存到字典中，{usename:password}
'''
username=input("请输入账号：")
password=input("请输入密码：")
if len(username)>=5 and len(username)<=8:
    if username[0] in "qazwsxedcrfvtgbyhnujmikopl":
        print("OK")
        if len(password)>=8 and len(password)<=12:
             print("注册成功",{username:password})
        else:
            print("密码必须是8-12位！")
    else:
        print("账号的首字母必须小写字母开头！")
else:
    print("账号的长度不符合规范，请输入5-8位的账号")
'''

