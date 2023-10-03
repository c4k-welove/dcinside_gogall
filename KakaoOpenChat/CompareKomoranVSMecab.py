import pandas as pd

list_komoran = pd.read_pickle('./KakaoOpenChat/nouns_komoran_with_preprocess.pkl')
list_mecab = pd.read_pickle('./KakaoOpenChat/nouns_mecab_with_preprocess.pkl')

print(len(list_komoran))
print(len(list_mecab))
