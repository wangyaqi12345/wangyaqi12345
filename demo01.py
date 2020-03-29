"""print("hello world")
print(2333)  #字符串
print(2.333)  #小数
print(True)    #布尔值
print(())     #元组
print([])     #字典
print("你好")  
print("哈哈"+"嘻嘻")
锄禾日当午，汗滴禾下土
print("哈哈",2334)
print("呵呵"*20)
print(((1+2)*100-99)/2)
print(2>3)
"""

#数据格式的转换

# print(type(""))
# print(type(1343))
# print(type(1.22))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# a = "哈哈哈"
# print(len(a))

# a = input("请输入：")
# b = input("请输入：")
# print("长度和为",len(a)+len(b))

#元组
# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)
# print(a[3])
# print(a)
# print(a.index("哈哈"))
# print(a.index("嘻嘻"))
# print(a.count("哈哈"))
# 二维元组
# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)
# b = (a,"哈哈","嘻嘻")
# print(b[0])
# print(b[2])
# print(b[0][3])
# print(b[0][5])
# print(b[0][5],b[1])

#切片
# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)
# print(a[-1])
# print(a[0:4])  #左闭右开
# print(a[4:9])
# print(a[9:])

#数组[]
# a = [1,2,3,4,"哈哈","嘻嘻",True,False]

# 元组一旦写好不可以修改，而数组是可以修改的
# a.append("append1")
# a.append("append2")
# print(a)
# print(a.index("哈哈"))
# print(a.count("嘻嘻"))

# a.insert(4,"insert")
# print(a)

# b = a.pop(0)  #剪切
# c = a.pop(0)  #剪切

# print(b+c)
# print(a)

# #a.clear()

# xx = ["您好","不好"]
# # a.extend(xx)
# print(a+xx)

# print(a)
# a.remove("哈哈")
# print(a)


# #False = 0   True = 1
# x = [0,False,1,True]
# b = x.count(0)
# print(b)         

"""
python的语法
所有的方法都是小括号结尾。比如print(),input(),len()
元组、数组、字典的取值，都是用中括号，比如a[]
元组、数组、字典的定义，分别是(),[],{}
"""

"""
字典的特点
1、字典中的值没有顺序
2、字典的结构必须是键值对的结构。  key:value
3、字典的取值，是通过key去取value的
"""
"""
a = {"name":"张三",
      0:"哈哈",
      "age":25
}
# 取值
print(a["name"])
# 新增
a["high"] = "183cm"
print(a)
# 修改
a["name"] = "李四"
print(a)

b = a.get("name")
print(b)
print(a)

c = a.pop("name")
print(c)
print(a)

a.update(name=1111)
print(a)

print("--------------------------------------------")

print(a.get("name11"))
# print(a["name11"])

# 数组和字典的删除
del a["name"]
print(a)

del a[0]
"""

# a = input('请输入名字：')
# b = input('请输入年龄：')
# c = input('请输入性别：')
# userinfo = {}
# userinfo.update(name=a,age=b,gender=c)

# print(userinfo)
