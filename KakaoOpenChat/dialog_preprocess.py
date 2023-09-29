import os

# 소스 파일이 들어있는 폴더 경로
source_folder_path = 'C:\Study\c4k\dcinside_gogall\KakaoOpenChat\Kakaotalk_Chat'
file_list = os.listdir(source_folder_path)

# 결과 파일
result_file_path = 'C:\Study\c4k\dcinside_gogall\KakaoOpenChat\\result.text'
result_file = open(result_file_path, 'w', encoding='utf-8')

for ktalk_dialog in file_list:
    ktalk_file = open(source_folder_path+"\\"+ ktalk_dialog, 'r', encoding='utf-8')
    lines = ktalk_file.readlines()
    for line in lines:
        line = line.strip()

        # 카톡방에 따라 특성이 다를 수 있을 것 같은데...
        # 샘플로 사용한 로블록스 방은 거의 단문이라 대화 시작 문장만 사용하고, 여러줄은 무시함.
        # 정규식으로 형식 판별해도 되는데, 기간이 짧으면 그냥 특정 연도로...
        hm = line.find(':') # 시분 구분자
        hm2 = line.find(':',hm+1)
        if line[:4]=='2023' and  hm2> hm:
            print(line[hm2+1:])
            result_file.write(line[hm2+1:]+'\n')
    ktalk_file.close()

result_file.close()