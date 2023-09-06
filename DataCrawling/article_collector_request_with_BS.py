############################
# 
#   Code for Korea
#   프로젝트 : 위로
#   Task : DCInside 고민갤러리(고갤) 분석을 통한 활동 방향 도출
#   
#   데이터 출처 및 활용 범위
#
#       Code for Korea의 '위로' 프로젝트와 관련하여 수집 된 DCInside의 고민 갤러리 데이터는
#       Code for Korea의 '위로' 프로젝트의 범위 내에서 공익적인 목적의 활동에만 활용 되어야 하며,
#       데이터 활용 시, 데이터의 출처를 명시해야 합니다.
#       
#       데이터 출처 : 디시인사이드 고민 갤러리 https://gall.dcinside.com/board/lists/?id=agony)
#
#   프로젝트 참여 방법
#        본 프로젝트의 데이터를 활용하여 공익성 있는 프로젝트를 하고자 하시면,
#        아래 링크로 Code for Korea '위로' 프로젝트(Slack)에 참여하실 수 있습니다.
#        참여하여 하고자 하는 활동을 참여 멤버들과 공유하고 자유롭게 진행하면 됩니다.
#
#   본 코드의 목적
#       본 코드는 디시인사이드 고민 갤러리의 글들의 분석을 위한 글 본문과 댓글 수집 코드 입니다.
#       수집 된 데이터를 이용하여 다양한 고민의 유형을 분석하여, 도움이 될 만한 활동을 도출하고자 합니다.
#
#   수집봇 차단 처리 헤더 설정 참고 : https://pgh268400.tistory.com/310
#       
#   XXXX  댓글은 아래 코드로 수집이 불가능 합니다. XXXX
#
##############################

import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs

# 구분자
welove_mark = '#C4K>'


#봇 차단을 위한 헤더 설정
headers = {
    "Connection" : "keep-alive",
    "Cache-Control" : "max-age=0",
    "sec-ch-ua-mobile" : "?0",
    "DNT" : "1",
    "Upgrade-Insecure-Requests" : "1",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site" : "none",
    "Sec-Fetch-Mode" : "navigate",
    "Sec-Fetch-User" : "?1",
    "Sec-Fetch-Dest" : "document",
    "Accept-Encoding" : "gzip, deflate, br",
    "Accept-Language" : "ko-KR,ko;q=0.9"
    }


## 작업 환경 설정
# 수집 대상 목록 파일 - 전체 목록 파일 중, 수집 할 대상만 저장한 텍스트 파일(각 행 가장 앞에 글 번호만 있으면 되며, 일단 글목록 형식을 따르는 것으로 가정)
# list_file_path = 'DCInsideGoGall_300000_3_list.text'
list_file_path = 'sample_list.text'

# 결과 파일 경로
result_file_path = 'DCInsideGoGall_300000_3.text'

# 각 글 연결 URL 기본 형식 - 가장 마지막에 글 번호만 붙이면 됨.
base_URL = 'https://gall.dcinside.com/board/view/?id=agony&no='


## 수집 작업
# 저장 될 파일
fResult = open(result_file_path, 'w',encoding='UTF-8')

# 목록 파일 행 순회
with open(list_file_path, encoding='utf-8') as fSource:
   for line in fSource:
       
        # article number
        artible_number = line[:line.find('|')]
        # article URL
        article_URL = base_URL + artible_number

        # open target article
        bPassed = False
        while bPassed==False:

            try:
                print("Try... " + article_URL)
                res = requests.get(article_URL, headers=headers)
                time.sleep(1)

                soup = bs(res.text, "html.parser")

                # URL
                print(welove_mark+article_URL)

                # Title
                title = soup.select(".title_subject") 
                print(welove_mark+title[0].text.strip(), end="")

                # article body
                body_divs = soup.select(".write_div") 
                for div in body_divs:
                    print(div.text, end="")

                # comments - commnets는 후처리로 읽어서  request 된 결과에 없음.              
                '''
                for cmt in cmmts_ul:

                    # nickname & date
                    nickname = cmt.select_one(".nickname")
                    cmt_date = cmt.select_one(".date_time")
                    print(welove_mark+nickname.text.strip()+"|"+cmt_date.text.strip())

                    # comment
                    cmt_txt = cmt.select_one("usertxt")
                    print(cmt_txt.text.strip())
                '''

                # end of article
                print(welove_mark+"X\n")

                bPassed = True
            except:
                print("Failed and Retry... "+article_URL)
                time.sleep(10)

        # completed log
        print('Done : ' + artible_number+ " " + str(datetime.now()))

    
fResult.close()







