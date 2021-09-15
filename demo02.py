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

for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,end="  ")
    print()    
