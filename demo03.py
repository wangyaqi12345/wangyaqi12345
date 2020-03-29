# a = input("请输入你的名字：")
# b = input("请输入你的年龄：")
# try:      #用来处理用户输入的数据
#     if int(b) > 18:
#         print(a,"成年人")
#     else:
#         print(a,"未成年")
# except:
#     print("请输入正确年龄")


# #导入包，习惯写在py文件的最上方
# import time
# import random   
# for i in range(10):
#     time.sleep(1)    #控制运行的速度，停顿1s
#     print(i) 
# a = random.randint(10,100)   #生成某个范围的随机数
# print(a)

"""
class 声明类的名字
然后类的名字首字母必须大写
面向对象编程
类里面所有的方法，都必须要传一个参数，叫self
"""
class GirlFriend():
    """
    女朋友
    """
    def __init__(self):       #对象的描述
        self.sex = "女"
        self.high = "170cm"
        self.weight = "55kg"
        self.hair = "大波浪"
        self.age = "18岁"
    
    def caiyi(self,num):
        """
        才艺表演
        """
        if num == 1:
            print("胸口碎大石")
        elif num == 2:
            print("唱跳rap篮球")
        else:
            print("单手开瓶盖")

    def chuyi(self):
        """
        厨艺持家
        """
        print("精通八大菜系")
    
    def work(self):
        """
        工作挣钱
        """
        print("开挖掘机！")

#类的实例化

zhangsan = GirlFriend()
zhangsan.caiyi(1)
zhangsan.work()
print(zhangsan.high)





# class Student():
#     def __init__(self,name,gender,age):
#         self.name = name
#         self.gender = gender
#         self.age = age
#     def hobby(self):
#         print("我最喜欢打游戏")
#     def dream(self,num):
#         if num == 1:
#             print("曾梦想执剑走天涯")
#         elif num == 2:
#             print("家里呆着吧")
# zhangsan = Student("张三","男","20")
# zhangsan.hobby()
# zhangsan.dream(2)
# print(zhangsan.name)

# class Newst(Student):
#     def hobby(self):
#         print("我喜欢唱歌")
# lisi = Newst("李四","男",44)
# lisi.hobby()
# print(lisi.name)

