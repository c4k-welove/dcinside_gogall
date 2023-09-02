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
#       본 코드는 디시인사이드 고민 갤러리의 글들의 분석을 위한 수집용 기초 데이터로써,
#       해당 갤러리의 글 목록을 수집하는 코드 입니다. 
#       이렇게 수집 된 코드를 이용하여 참여자들과 수집 범위를 나누거나 수집 진도를 관리하기도 하고,
#       게시글 수집 코드의 작성을 편리하게 할 수 있도록 글 번호를 추출하기 위해 사용합니다.
#       또한, 게시글 목록을 통한 통계적 분석으로도 활용 가능할 것으로 기대합니다.
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

# 수집 페이지 범위 - 2023년 8월 말 기준, 100개 단위로 전체 페이지 범위 (1~9715)
page_from = 1
page_to = 9715

# 결과 파일 경로
result_file_path = 'result_'+str(page_from)+'_'+str(page_to)+'.text'

# 수집 대상 사이트
base_URL = 'https://gall.dcinside.com/board/lists/?id=agony&list_num=100&page='

# 저장 될 파일
f = open(result_file_path, 'a+t',encoding='UTF-8')

for page in range(page_from, page_to+1):
    target_url = base_URL + str(page)
    bPassed = False

    while bPassed==False:
        try:
            driver.get(target_url)
            bPassed = True
        except:
            print("Missed page " + str(page))
            time.sleep(60)

    time.sleep(2)

    # table
    list_table = driver.find_element(By.XPATH,'//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody')

    # contents
    trs = list_table.find_elements(By.TAG_NAME,'tr')
    for tr in trs:
        #number
        number = tr.get_attribute('data-no')
        if number==None:
            continue

        print(number)

        #title
        title = tr.find_element(By.CLASS_NAME,'gall_tit').text

        #reply
        reply_cnt = "#"
        replay_open_idx = title.rfind('[')

        if len(title)<3:
            reply_cnt="0"
        elif  title[-1]!=']' and replay_open_idx<0:
            reply_cnt="0"
        else:
            reply_cnt = title[replay_open_idx+1:-1]
            title = title[:replay_open_idx]
  
        #writer
        writer = tr.find_element(By.CLASS_NAME,'gall_writer').text

        #date
        date = tr.find_element(By.CLASS_NAME,'gall_date').get_attribute('title')

        #count
        count = tr.find_element(By.CLASS_NAME,'gall_count').text

        #recommend
        recommend = tr.find_element(By.CLASS_NAME,'gall_recommend').text

        #tr
        tr_string = number+"|"+title+"|"+reply_cnt+"|"+writer+"|"+date+"|"+count+"|"+recommend+"\n"

        #print
        #print(tr_string)
        f.write(tr_string)

    # 중간에 에러가 발생 할 경우, 진행 된 만큼의 데이터를 온전히 확보
    if  page%10==0:
        f.close()
        f = open(result_file_path, 'a+t',encoding='UTF-8')
        
    # 진척 상황 확인
    print('progress - '+ str(page) + ' - ' + str(datetime.now()))

f.close()