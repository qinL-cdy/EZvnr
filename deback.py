# coding=gbk
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open("b.jpg")
img = img.convert("RGB")
newImg = Image.new("RGB", img.size, (255,255,255,255))
#字典转list
def dict2list(dic:dict):
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst
w,h = img.size
a = {}
#统计颜值出现的次数
for i in range(w):
    for j in range(h):
        r,g,b = img.getpixel((i,j))
        t = r*255*255 + g * 255 + b
        if t in a.keys():
            a[t] =  a[t] + 1
        else:
            a[t]  = 1
l = sorted(dict2list(a), key=lambda x:x[1], reverse=True)
dic = {}
#去掉出现次数太多的颜色，不影响我们的观察
for i in l:
    if(i[1] < 500):
        dic[i[0]] = i[1]
#下面的代码是画图用的
plt.figure(1, figsize=(20,5))
plt.scatter(dic.keys(), dic.values(), linewidth=1)
plt.legend()
plt.show()
rmg = Image.new("RGB", img.size, (255,255,255,255))
for i in range(w):
    for j in range(h):
        r,g,b = img.getpixel((i,j))
        t = r*255*255 + g * 255 + b
        #小与颜值分界线的点我们就把颜色填充到新的图片上面
        if(t<4000000 or 10000000<t):
            rmg.putpixel((i,j), (r,g,b))
rmg.convert('L').show()
rmg.save('c.jpg')