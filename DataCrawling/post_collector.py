from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 크롤링할 게시물의 기본 URL
base_url = 'https://gall.dcinside.com/mgallery/board/view/?id=agony&no={}'

# 크롬 드라이버 초기화
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 브라우저 창을 열지 않고 실행 (headless 모드)
driver = webdriver.Chrome(options=chrome_options)

# 시작 포스트 번호 입력
start_post = int(input("시작 포스트 번호를 입력하세요: "))
end_post = start_post + 99999  # 시작 포스트로부터 10000개의 글까지 크롤링

# 파일명 생성
file_name = f'DCInsideGoGall_{start_post}_{end_post}.txt'

# 파일에 데이터 저장
with open(file_name, 'w', encoding='utf-8') as file:
    for post_number in range(start_post, end_post + 1):
        # 게시물 URL 생성
        post_url = base_url.format(post_number)

        # 게시물 로드
        driver.get(post_url)
        wait = WebDriverWait(driver, 10)  # 최대 10초 동안 기다림

        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'title_subject')))
            print(post_number)

            title_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'title_subject')))
            post_title = title_element.text

            post_content_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'writing_view_box')))
            post_content = post_content_element.text

            file.write(f'#C4K>{post_url}]\n')
            file.write(f'#C4K>{post_title}\n')
            file.write(f'{post_content}\n')

            comments = driver.find_elements(By.CSS_SELECTOR, 'li.ub-content')
            for idx, comment in enumerate(comments):
                commenter_info = comment.find_element(By.CLASS_NAME, 'nickname').text
                comment_time = comment.find_element(By.CLASS_NAME, 'date_time').text

                # 댓글 본문 가져오기
                comment_text = comment.find_element(By.CLASS_NAME, 'ub-word').text

                file.write(f'#C4K>{commenter_info}|{comment_time}\n')
                file.write(f'{comment_text}\n')

            file.write('#C4KX\n\n')
        except Exception as e:
            print(f"Error for post {post_number}")

# 웹 드라이버 종료
driver.quit()
