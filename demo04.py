# text = input("请输入今天的天气：")
# with open("日记.txt","w",encoding="utf8") as f:   #w是写入到文件中，并命名为f
#     f.write(text)

import time

now = time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入今天的天气：")
with open("日记.txt","a",encoding="utf8") as f:     #a是保存文件并继续写入
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("-----------------------")