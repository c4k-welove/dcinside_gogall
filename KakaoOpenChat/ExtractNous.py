from konlpy.tag import Komoran, Kkma
import pickle
import time
from eunjeon import Mecab
import re
import pandas as pd

def text_clean(text):
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail제거
    text = re.sub(pattern, '', text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern, '', text)
    pattern = '[a-zA-Z0-9]'    # 숫자와 알파벳 제거
    text = re.sub(pattern, '', text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern, '', text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern, '', text)
    pattern = '[^\w\s]'         # 특수기호제거
    text = re.sub(pattern, '', text)
    return text 


mecab = Mecab()
komoran = Komoran()
#kkma = Kkma()

all_nouns = []

start_time = time.time()

# 소스 파일 읽기
src_doc_path = './KakaoOpenChat/dialog_only_filtered.text'
src_doc = open(src_doc_path, 'r', encoding='utf-8')
for line in src_doc.readlines():
  line = line.strip()
  try:
    line = text_clean(line)

    komoran_nouns = komoran.nouns(line)
    #nouns = kkma.nouns(line)
    mecab_nouns = mecab.nouns(line)
    merged_row = [line, komoran_nouns, mecab_nouns]

    all_nouns.append(merged_row)
    print(merged_row)  
  except:
    print("ERROR>"+line)

src_doc.close()
end_time = time.time()

#with open('./KakaoOpenChat/nouns_kkma_with_preprocess.pkl', 'wb') as f:
#with open('./KakaoOpenChat/nouns_komoran_with_preprocess.pkl', 'wb') as f:
#with open('./KakaoOpenChat/nouns_mecab_with_preprocess.pkl', 'wb') as f:
#with open('./KakaoOpenChat/nouns_mecab_with_preprocess.pkl', 'wb') as f:
#    pickle.dump(all_nouns, f)

frame = pd.DataFrame(all_nouns)
frame.to_excel('./KakaoOpenChat/nouns_compare.xlsx')

print("Elapsed time - "+str(end_time - start_time))