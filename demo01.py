# print("hello world!")
# print(2333)
# print(2.333)
# print(True)
# print(False)
# print(())
# print([])
# # print({})
# a=input("请输入第一段内容：")
# b=input("请输入第二段内容：")
# print("两段内容为：",a,b,"两段字数和为：",len(a)+len(b))


#a=(1,2,3,4,"哈哈","嘻嘻",True,False)
# print(a)

# print(a[5])#只想打印一个

# #index（）查找某个值的下标
# print (a.index("哈哈"))

# b=(a,"哈哈","嘻嘻")#二维元组
# print(b[1])
# print(b[0][2])

# #批量取值:左闭右开,不超出范围，最左与最右可不写
# print(a[0:4])
# print(b[0:2])

#2.数组
#append（）追加，尾巴上加
# a=[1,2,3,4,"哈哈","嘻嘻",True,False]
# print(a)
# a.append("你好")
# print(a)

#insert()想插入到哪就到哪
# a.insert(1,"insert")#1是插入的位置
# print(a)

#pop()剪切的作用：把这个值从数据中拿出来，可赋值给新的变量
# b=a.pop(5)
# print(b)

#clear()清空
#copy()复制，测试里比较少用
#extend()与append()作用相同，区别在于一次可以放入多个值
# a.extend(["哈喽","嗨呀"])#记得加[]
# print(a)

#a.remove("哈哈")把哈哈删除
#a.remove(0)把false删除
#a.remove(1)把true删除

#字典/dict，字典中的值没有顺序，结构必须是键值对：key:value
# a={
#     "name":"张三",
#     0:"哈哈",
#     "age":25
#     }
# print(a)

#写key,把value取出
# print(a["name"])#取值
# a["high"]="183cm"#新增
# print(a)
# a["name"]="李四"#修改
# print(a)

#get()取值
#pop()剪切
#update()更新同修改，key 存在就修改，不存在就新增
# a.update(name=1111)
# a.update(weight=65)
# print(a)

#数组与字典的删除：字典：del a["name"]   数组：del a[0]
# del a["age"]
# print(a)

#练习 获取用户输入的个人信息，并且存储到字典中
#个人信息包括：name,age,sex
a=input("请输入个人信息：name:")
b={"name":a}
a=input("age:")
b["age"]=a
a=input("sex:")
b["sex"]=a
print(b)


"""
a={ "name":"张三",
    "外号":"哈哈",
    "age":25,
    "high":"180cm",
    "sex":"男",
    "hobby":"打篮球，下象棋
    }
"""










