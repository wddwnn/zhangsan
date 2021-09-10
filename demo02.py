a=1
while a<=10:
    studentlevel ={}
    name=input("请录入姓名：")
    score=int(input("请录入成绩："))
    studentlevel.update(name=name)
    studentlevel.update(score=score)
    high={}
    low={}
    if score>=60:
        high.update(score=score)
    else:
        low.update(score=score)
    a=a+1
print(studentlevel)
print(high)
print(low)