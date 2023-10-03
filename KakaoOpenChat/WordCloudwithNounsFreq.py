# https://www.codecademy.com/article/creating-a-word-cloud-with-python

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from collections import Counter

src_doc_path = './KakaoOpenChat/mecab.text'
src_doc = open(src_doc_path, 'r', encoding='utf-8')
documents = src_doc.read()

nouns_counter = Counter(documents)

wordcloud = WordCloud(
  background_color="white", 
  font_path='C:/Windows/Fonts/malgun.ttf',
  collocations=False, 
  stopwords=STOPWORDS, 
  contour_color="white", 
  contour_width=1)
wordcloud.generate_from_frequencies(nouns_counter)    # 빈도수가 구해진 전체 단어plt.

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()