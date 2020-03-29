with open("日记.txt","r",encoding="utf8") as f:
    text = f.readline()
for i in text:
    print(i)