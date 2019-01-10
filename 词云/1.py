# coding=utf-8
from os import path
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread


d = path.dirname('.')
text = open(path.join(d, '1'),encoding='utf-8', errors='ignore').read()
bg_pic = imread(path.join(d, '1.gif'))

# 生成词云
wordcloud = WordCloud(mask=bg_pic, background_color='white', scale=1.5,
                      font_path=r'‪C:\Windows\Fonts\simkai.ttf').generate(text)
image_colors = ImageColorGenerator(bg_pic)
# 显示词云图片

plt.imshow(wordcloud.recolor(color_func=image_colors))
plt.axis('off')
plt.show()

# 保存图片
wordcloud.to_file(path.join(d, 'd:/txt_data/result.jpg'))