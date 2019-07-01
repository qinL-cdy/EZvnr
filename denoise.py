# coding=gbk
from PIL import Image, ImageEnhance

img_name = 'c.jpg'
# ȥ��������
im = Image.open(img_name)
# ͼ���ֵ��
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
data = im.getdata()
w, h = im.size
# im.show()
black_point = 0
for x in range(1, w - 1):
    for y in range(1, h - 1):
        mid_pixel = data[w * y + x]  # �������ص�����ֵ
        if mid_pixel == 0:  # �ҳ����������ĸ��������ص�����ֵ
            top_pixel = data[w * (y - 1) + x]
            left_pixel = data[w * y + (x - 1)]
            down_pixel = data[w * (y + 1) + x]
            right_pixel = data[w * y + (x + 1)]

            # �ж��������ҵĺ�ɫ���ص��ܸ���
            if top_pixel == 0:
                black_point += 1
            if left_pixel == 0:
                black_point += 1
            if down_pixel == 0:
                black_point += 1
            if right_pixel == 0:
                black_point += 1
            if black_point >= 3:
                im.putpixel((x, y), 0)
            # print black_point
            black_point = 0
im.save('d.jpg')