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
#   User Header 참고 : https://chicken-nlp.tistory.com/4
#   WebDriver : https://getitall.tistory.com/entry/Python-Selenium-%ED%81%AC%EB%A1%AC-%EC%9B%B9%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B2%84-Chrome-Webdriver-%EC%84%A4%EC%A0%95-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0
#
##############################

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import time
from datetime import datetime
from bs4 import BeautifulSoup as bs

# 구분자
welove_mark = '#C4K>'


# 웹드라이버 설정
options = Options()
user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
options.add_argument('user-agent=' + user_agent)
options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.
options.add_argument('--blink-settings=imagesEnabled=false') 
options.add_argument('--mute-audio') 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(),options=options))

## 작업 환경 설정
# 수집 대상 목록 파일 - 전체 목록 파일 중, 수집 할 대상만 저장한 텍스트 파일(각 행 가장 앞에 글 번호만 있으면 되며, 일단 글목록 형식을 따르는 것으로 가정)
list_file_path = 'DCInsideGoGall_List_296300_3.text'

# 결과 파일 경로
result_file_path = list_file_path+'.result'

# 각 글 연결 URL 기본 형식 - 가장 마지막에 글 번호만 붙이면 됨.
base_URL = 'https://gall.dcinside.com/board/view/?id=agony&no='


## 수집 작업
# 저장 될 파일
fResult = open(result_file_path, 'w',encoding='UTF-8')

# 목록 파일 행 순회
row_cnt = 0
with open(list_file_path, encoding='utf-8') as fSource:
   for line in fSource:
       
        # article number
        artible_number = line[:line.find('|')]
        # article URL
        article_URL = base_URL + artible_number

        # open target article
        bPassed = False
        print("Ready " + article_URL)

        bPassed = False
        while bPassed==False:
            try:
                driver.get(article_URL)
                element = wait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "view_comment")))
                bPassed = True
                time.sleep(1)
            except:
                print("Missed page " + str(artible_number))
                # 혹시 모르니 여기까지 저장해두고.
                fResult.close()
                fResult = open(result_file_path, 'a+t',encoding='UTF-8')
                time.sleep(30)

        # body
        soup = bs(driver.page_source, 'html.parser')
        #title = driver.find_element_by_class_name("view_comment")

        # URL
        fResult.write(welove_mark+article_URL+'\n')
     
        # Title
        title = soup.select(".title_subject") 
        #print(title[0].text.strip(), end="")
        fResult.write(welove_mark+title[0].text.strip() + '\n')

        # article body
        body_divs = soup.select(".write_div") 
        for div in body_divs:
            #print(div.text, end="")
            fResult.write(div.text.lstrip())

        # comment 
        try:
            cmt_list = driver.find_element(by=By.CLASS_NAME,value="cmt_list")

            cmts = cmt_list.find_elements(by=By.TAG_NAME,value="li")
            # 댓글도 더 깊은 Depth에서 검출 되기 때문에 댓글 여부를 먼저 판정하기 위해 최상위 레벨의 li만 추출 -> 보류
            #cmts = cmt_list.find_elements(by=By.CSS_SELECTOR,value="li:first-of-type")
            #print(len(cmts))

            for cmt in cmts:
                try:
                    # comment - 광고행 등, 댓글 없으면 바로 예외 처리 하기 위해 가장 먼저 검사
                    cmt_txt = cmt.find_element(by=By.CLASS_NAME,value="usertxt")

                    # nickname & date
                    nickname = cmt.find_element(by=By.TAG_NAME,value="em")#cmt.find_element(by=By.CLASS_NAME,value="nickname in")
                    
                    # 광고 필터링
                    if nickname==None:
                        continue

                    # user/ date
                    cmt_date = cmt.find_element(by=By.CLASS_NAME,value="date_time")
                    #print(nickname.text.strip()+"|"+cmt_date.text.strip())
                    #print(cmt_txt.text.strip())   

                    # 댓글 여부
                    #reply_div = cmt.find_element(by=By.CLASS_NAME,value="reply_box")
                    #if not reply_div:
                    #    fResult.write(welove_mark+nickname.text.strip()+"|"+cmt_date.text.strip()+'\n')
                    #else:
                    #    fResult.write(welove_reply+nickname.text.strip()+"|"+cmt_date.text.strip()+'\n')
                    fResult.write(welove_mark+nickname.text.strip()+"|"+cmt_date.text.strip()+'\n')
                    fResult.write(cmt_txt.text.strip()+'\n')

                except NoSuchElementException:
                    print("Not comment row")   

        except NoSuchElementException:
            print("No comment")    

        # end of an article
        fResult.write(welove_mark+"X\n\n")   
        # completed log
        print('Done : ' + artible_number+ " " + str(datetime.now()))

        #  저장이 안될 경우를 대비하여 100개마다 저장 후 다시 열기
        if row_cnt % 100 == 0:
            fResult.close()
            fResult = open(result_file_path, 'a+t',encoding='UTF-8')
   
fResult.close()
