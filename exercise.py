"""
练习：
现在有11个学生的成绩，需要录入到系统中
分别是："张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"
并且名字和成绩需要对应
大于60分和小于60分的需要分开存放

input
字典
数组

"""
# high = {}  # 定义一个空字典，用来存储大于60的信息
# low = {}
# #print(len(low))
# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# a = 0
# while a < len(studentlist):
#     chengji = int(input("请输入"+studentlist[a]+"的成绩："))
#     if chengji >=60:  #判断分数
#         high[studentlist[a]] = chengji
#     else:
#         low[studentlist[a]] = chengji
#     a+=1
# print("大于60的：",high)
# print("小于60的：",low)

# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# highgrade = {}
# lowgrade = {}
# a = 0
# while a < len(studentlist):
#     grade = int(input("请输入"+studentlist[a]+"的成绩："))
#     if grade >= 60:
#         highgrade[studentlist[a]] = grade
#     else:
#         lowgrade[studentlist[a]] = grade
#     a = a + 1
# print("高于60分的：",highgrade)
# print("低于60分的：",lowgrade)

#利用for循环
# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# highgrade = {}
# lowgrade = {}
# for i in studentlist:
#     grade = int(input("请输入"+i+"的成绩："))
#     if grade >= 60:
#         highgrade[i] = grade
#     else:
#         lowgrade[i] = grade    
# print("高于60分的：",highgrade)
# print("低于60分的：",lowgrade)


# for i in range(100):
#     print(i)

"""
练习
九九乘法表
"""


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",i*j,end="  ")
#     print()

"""
练习1：
通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
练习2：
使用代码，实现一个注册的功能。
用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
储到到字典中，{username:password}
"""

#我自己做的
# a = 1
# while a == 1:
#     for i in range(30,0,-1):
#         print("红灯还有",i,"秒结束")
#         i+=1
#     for j in range(35,0,-1):
#         print("绿灯还有",j,"秒结束")
#         j+=1
#     for m in range(3,0,-1):
#         print("黄灯",m,"秒结束")
#         m+=1

# username = input("请输入账号：")
# password = input("请输入密码：")
# userinfo = {}
# if len(username) < 5 and  len(username) > 0 or len(username) > 8:
#     print("账号的长度必须是5-8位")
# elif  username[0] not in "abcdefghijklmnopqrstuvwxyz":
#     print("账号必须小写字母开头")
# elif len(password) < 6 and  len(password) > 0 or len(password) > 12:
#     print ("密码长度必须是6-12位")
# elif len(username) == 0:
#     print("账号不能为空！")
# elif len(password) == 0:
#     print("密码不能为空！")
# else:
#     print("恭喜您注册成功！")
#     userinfo[username] = password
#     print(userinfo)


#老师讲的
# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print(i,"倒计时还有",light[i]-j,"秒")



# username = input("请输入账号：")
# password = input("请输入密码：")
# if len(username) >= 5 and len(username) <= 8:
#     if username[0] in "abcdefghigklmnopqrstuvwxyz":
#         if len(password) >= 8 and len(password) <= 12:
#             print("注册成功!",{username:password})
#         else:
#             print("密码必须8-10位")                
#     else:
#        print("账号首字母要小写字母")
# elif len(username) ==0 or len(password) == 0:
#     print("账号或密码不能为空！")
# else:
#     print("账号的长度不符合规范，账号要求5-8位")


"""
练习：
定义一个方法，用来判断用户输入的账号密码是否符合规范。
"""

def check(username,password):
    if len(username) >= 5 and len(username) <= 8:
        if username[0] in "abcdefghigklmnopqrstuvwxyz":
            if len(password) >= 8 and len(password) <= 16:
                return True
            else:
                return ("密码必须8-10位")            
        else:
            return "账号首字母要小写字母开头"
    else:
        return "账号的长度不符合规范，账号要求5-8位"
a = check("dgh367","168")
print(a)

