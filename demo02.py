#判断
# a = 1
# b = 2

# if a == 1:
#     print("哈哈哈")

# if a > b:
#     print("a比b大")
# else:
#     print("b更大")

# age = int(input("请输入你的年龄："))
 
# if age > 60:
#     print("你应该退休了")
# elif age > 30:
#     print("家庭的责任很重")
# elif age > 20:
#     print("好好规划未来")
# else:
#     print("认真读书")

# grade = int(input("请输入分数:"))

# if grade >= 90:
#     print("优秀，看好你")
# elif grade >= 80 and grade < 90:
#     print("良好，继续努力")
# elif grade >= 60 and grade < 80:
#     print("及格了")
# else:
#     print("你这个学渣")


# a = "你好"
# if a in  "你好吗":
#     print("ok")
# else:
#     print("no")

# a = input("请输入：")
# if a == "":
#     print ("不能为空！")
#     exit()
# if a in  "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的年龄！")
#     exit()
# if a > 5:
#     print("大")
# else:
#     print("小")


# a = "ssssdsf"
# if type(a) is int:
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")

# a = 1
# while a < 10:
#     print("循环",a)
#     a = a + 2


#遍历for
# a = "你好，今天你吃了吗？"
# b = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# for i in a:
#     print(i)
# for c in b:
#     print(c)

# aa = {"name":"张","age":20}
# print(len(aa))

# b = range(100)
# print(b)

# b = list(range(0,100,2))  #自动生成了一个数列，步进/步长
# print(b)

# for i in range(10):
#     if i == 4:
#         continue    #跳过本次循环
#     print(i)
    
# for i in range(10):
#     if i == 4:
#         break   #跳出本次循环，只跳出一层循环
#     print(i)

# for i in range(1,10):
#     for j in range(1,i+1):
#         if i == 3:
#             break
#         print(j,"X",i,"=",i*j,end="  ")
#     print()


# a = [1,2,3,5,68,5]
# x = a.index(68)
# print(a[x])

# def diancheng(a,b):
#     """
#     这个方法的作用是实现两个数和乘第一个数的结果
#     """
#     print((a+b)*b)
# diancheng(10,20)




# def length():
#     """
#     这个方法的作用比较长度
#     """
#     a = "sdssgdgg"
#     if len(a) > 10:
#         print("长度大于10")
#     else:
#         print("长度小于等于10")
# length()


# try:
#     print(we+23)
# except:
#     print("代码有错误！")

def jiafa(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    else:
        return "输入的数据类型不正确"
print(jiafa(1,2))