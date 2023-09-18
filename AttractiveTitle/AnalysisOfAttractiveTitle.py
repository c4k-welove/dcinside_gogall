# Konlpy 설치
# https://konlpy.org/ko/latest/install/#id2

from konlpy.tag import Kkma
import pickle
from operator import itemgetter


kkma = Kkma()

dc_dict={}

#list_file = open('./AttractiveTitle/DCInside_gogall_list_with_reply.text')
list_file = open('./AttractiveTitle/1.text', encoding='utf-8')

for line in list_file.readlines():
    line = line.strip()

    # 1842020|정신차리자 개이야 |4|고갤러(118.235)|2023-08-31 20:34:14|32|0
    terms = line.split('|')

    try:
        title = terms[1]
        comment = int(terms[2])
        views = int(terms[5])
    except:
        continue

    # 제목의 형태소 분리
    morphs = kkma.morphs(title)

    for morph in morphs:
        if morph in dc_dict:
            dc_dict[morph] += views
        else:
            dc_dict[morph] = views
list_file.close()

dc_dict = sorted(dc_dict.items(), key=itemgetter(1))

with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(dc_dict, f)

print(dc_dict)
