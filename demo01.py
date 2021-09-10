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
a=[1,2,3,4,"哈哈","嘻嘻",True,False]
print(a)
a.append("你好")
print(a)

#insert()想插入到哪就到哪
a.insert(1,"insert")#1是插入的位置
print(a)

#pop()剪切的作用：把这个值从数据中拿出来，可赋值给新的变量
b=a.pop(5)
print(b)

#clear()清空
#copy()复制，测试里比较少用
#extend()与append()作用相同，区别在于一次可以放入多个值
a.extend(["哈喽","嗨呀"])#记得加[]
print(a)

#a.remove("哈哈")把哈哈删除
#a.remove(0)把false删除
#a.remove(1)把true删除







