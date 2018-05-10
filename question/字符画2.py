#   _*_ coding:utf-8 _*_
from PIL import Image

def transform(im):
    im = im.convert("L")
    #   初始化txt
    txt = ""
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            grey = im.getpixel((j, i))
            #   坐标处的灰度值越小，说明灰的程序深，对应替换的字符应该越靠在ascii_char的前面
            txt += ascii_char[int(grey / unit)]
        txt += '\n'
    return txt

#   ascii字符列表(事先排序过的，为了效果)
ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#   ascii的字符的总长度
length = len(ascii_char)
#   灰度值与ascii_char中的字符转换时的系数，保证灰度值转换字符时不会超出列表ascii_char
unit = 256.0 / length
#   打开目标图片
im = Image.open(r"./2.jpg")
#   获取图片的大小:(1024, 768)
width, height = im.size
#   将图片进行一定比例的缩小(即重设图片大小)
im = im.resize((int(width * 0.25), int(height * 0.25)))
print("重新生成的图像大小为:%d*%d" % (im.size[0], im.size[1]))


txt = transform(im)
f = open(r"./output.txt", 'w')
f.write(txt)
f.close()