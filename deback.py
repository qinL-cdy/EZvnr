# coding=gbk
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open("b.jpg")
img = img.convert("RGB")
newImg = Image.new("RGB", img.size, (255,255,255,255))
#�ֵ�תlist
def dict2list(dic:dict):
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst
w,h = img.size
a = {}
#ͳ����ֵ���ֵĴ���
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
#ȥ�����ִ���̫�����ɫ����Ӱ�����ǵĹ۲�
for i in l:
    if(i[1] < 500):
        dic[i[0]] = i[1]
#����Ĵ����ǻ�ͼ�õ�
plt.figure(1, figsize=(20,5))
plt.scatter(dic.keys(), dic.values(), linewidth=1)
plt.legend()
plt.show()
rmg = Image.new("RGB", img.size, (255,255,255,255))
for i in range(w):
    for j in range(h):
        r,g,b = img.getpixel((i,j))
        t = r*255*255 + g * 255 + b
        #С����ֵ�ֽ��ߵĵ����ǾͰ���ɫ��䵽�µ�ͼƬ����
        if(t<4000000 or 10000000<t):
            rmg.putpixel((i,j), (r,g,b))
rmg.convert('L').show()
rmg.save('c.jpg')