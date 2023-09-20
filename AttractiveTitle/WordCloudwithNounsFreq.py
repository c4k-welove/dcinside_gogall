# https://www.codecademy.com/article/creating-a-word-cloud-with-python

import os
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

current_directory = os.path.dirname(__file__)
heart_image_path = os.path.join(current_directory, "heart_mask.JPG")
heart_image = Image.open(heart_image_path)
heart_mask = np.array(heart_image)
#print(heart_mask)

#target_file_path = "nouns_by_view_top100.text"
target_file_path = "nouns_by_comment_top100.text"

with open(os.path.join(current_directory+'/result/', target_file_path), encoding='utf-8') as f:
  hot_nouns = f.read()


wordcloud = WordCloud(
  background_color="white", 
  font_path='C:/Windows/Fonts/malgun.ttf',
  mask=heart_mask, 
  collocations=False, 
  stopwords=STOPWORDS, 
  contour_color="white", 
  contour_width=1)
wordcloud.generate(hot_nouns)

image_colors = ImageColorGenerator(heart_mask)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()