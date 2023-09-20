# Konlpy 설치
# https://konlpy.org/ko/latest/install/#id2

from konlpy.tag import Kkma, Komoran
import pickle
from operator import itemgetter


#kkma = Kkma()
komoran = Komoran()

dc_dict={}

list_file = open('./AttractiveTitle/DCInside_gogall_list_with_reply.text', encoding='utf-8')
#list_file = open('./AttractiveTitle/1.text', encoding='utf-8')

cnt = 0
lines = list_file.readlines()
line_cnt = len(lines)

for line in lines:
    line = line.strip()

    cnt += 1
    #if cnt % 100 == 0:

    # 1842020|정신차리자 개이야 |4|고갤러(118.235)|2023-08-31 20:34:14|32|0
    terms = line.split('|')

    try:
        title = terms[1]
        comment = int(terms[2])
        views = int(terms[5])
        # 같은 글자만 연속으로 있는 문장에서 hang 걸림
        # 첫번째-마지막 글자가 같고 띄어쓰기 없으면 skip하는걸로.
        if title[0]==title[-1] and title.find(' ')<0:
            continue

        print(f"Progress - {cnt} / {line_cnt} : {title}")

        # 제목의 형태소 분리
        #morphs = kkma.morphs(title)
        #morphs = kkma.pos(title)
        #nouns = kkma.nouns(title)
        nouns = komoran.nouns(title)

        for morph in nouns:
            if morph in dc_dict:
                dc_dict[morph] += comment#views
            else:
                dc_dict[morph] = comment#views

    except:
        print('Unkown exception.')
        continue


list_file.close()

dc_dict = sorted(dc_dict.items(), key=itemgetter(1), reverse=True)

with open('./AttractiveTitle/result/nouns_by_comments.pkl', 'wb') as f:
    pickle.dump(dc_dict, f)

dc_dict = dc_dict[:100]
print(dc_dict)
