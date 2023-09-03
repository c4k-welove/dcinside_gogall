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
##############################

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import re

# 드라이버 파일은 py파일과 같은 위치에 위치하도록 합니다.
driver = webdriver.Chrome()


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
        print("Ready " + artible_number)
        while bPassed==False:
            try:
                driver.get(article_URL)
                bPassed = True
                print("Opened " + artible_number)
            except:
                print("Missed article : " + artible_number+ " " + str(datetime.now()))
                time.sleep(60)
        time.sleep(1)

        # completed log
        print('Done : ' + artible_number+ " " + str(datetime.now()))




fResult.close()