# Konlpy 설치
# https://konlpy.org/ko/latest/install/#id2

from konlpy.tag import Kkma

kkma = Kkma()

text = '아버지가 방에 들어갑니다.'

morphs = kkma.morphs(text)
print(morphs)