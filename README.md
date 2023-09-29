# 상위 프로젝트
## 프로젝트 이름
Code for Korea 프로젝트 '위로(慰勞, WeLove)

## 목적
위로가 필요한 우리의 이웃들을 위로 할 수 있는 활동을 해보자.

## 프로젝트 문서
프로젝트 구글 계정의 구글 드라이브 - https://drive.google.com/drive/folders/1NFsWFaOmIhy_NRoicCXr2nGQhpp0cKbt?usp=drive_link

# 본 Task
DCInside 고민갤러리(고갤) 분석을 통한 활동 방향 도출

## 목표
프로젝트의 다양한 후보 활동 중, 고민게시판에 위로가 되는 댓글을 달아주는 활동과 함께 작성 된 고민 글들을 분석하여 고갤의 사용자들이 가진 고민들은 어떤 것이며 어떻게 고민을 덜 수 있는 방법은 무엇일지 자료를 바탕으로 검토하여 실질적인 해결책을 찾아보자는 취지

## 실행 해 볼 Task들과 Task별 활동

### 위로의 댓글
- 고갤의 사용자가 되어, 고민이 있는 사람들의 이야기를 들어주고 따뜻한 댓글 남기기
- 이를 독려하기 위한 캠페인 홍보 활동
- 이를 독려하기 위한 "위로 댓글러 활동 수첩" 페이지 개발 : 활동 이력 기록 및 새로운 고민 게시판 발굴/등록 


### 고갤 분석
* 고갤 데이터 분석을 위한 데이터 수집(크롤링)
    * 고갤 글 목록 수집(DataCrawling/list_collector.pys)
* 수집 된 데이터를 이용한 고민 분석(데이터분석)
    * 분석한 글을 블로그 등에 게시하여 고민을 나누거나 고민을 덜 수 있는 방법을 제안
    * 위로와 관심을 받을 수 있는 글 제목(AttractiveTitle/*.py)
    * 이 데이터를 이용하여 분석한 블로그 포스트 주소를 알려주세요~(wonil.shim@gmail.com)


###  SNS 대화 분석
* 카카오톡 대화 데이터 기반, "재미있는" 분석
    * 청소년들이 스스로 자신이 속한 대화방의 데이터를 저장하는 일이 잦아지면 상담사분들께 전달하기 위한 허들이 조금은 낮아질 수 있지 않을까 싶고, 그 과정에서 상담사 선생님께 "공유"하기 위한 기회도 생길 수 있으며, 특히 분석 결과를 통해 대화방 내의 대화를 객관화 할 수 있게 되면 좋을 것 같습니다.
    * 데이터 전처리(KakaoOpenChat/dialog_preprocess.py) - 대화 내용만 추출 



# 데이터 출처 및 활용 범위

## 활용 범위
Code for Korea의 '위로' 프로젝트와 관련하여 수집 된 DCInside의 고민 갤러리 데이터는
Code for Korea의 '위로' 프로젝트의 범위 내에서 공익적인 목적의 활동에만 활용 되어야 하며,
데이터 활용 시, 데이터의 출처를 명시해야 합니다.

데이터 출처 : 디시인사이드 고민 갤러리 https://gall.dcinside.com/board/lists/?id=agony

## 프로젝트 참여 방법
본 프로젝트의 데이터를 활용하여 공익성 있는 프로젝트를 하고자 하시면,
Code for Korea '위로' 프로젝트(Slack : https://code-for-korea.slack.com/archives/C05NCGCMWS2)에 참여하여 함께 하실 수 있습니다.
참여하여 하고자 하는 활동을 참여 멤버들과 공유하고 자유롭게 진행하면 됩니다.

# 결과물

## DCInside 고민 갤러리(https://gall.dcinside.com/board/view/?id=agony)

### 글목록
* 글 목록(~2023.8.31) : https://drive.google.com/file/d/1tzcjHYIwrdZnlTu5u62F1fYjC2-kZJfG/view?usp=drive_link
* 댓글있는 글 목록(~2023.8.31) : https://drive.google.com/file/d/13FRCeDtysC0HFzpbef_eUjn-Q_kuqzRN/view?usp=drive_link


* 글 목록(JSON)(~2023.9.11) : https://drive.google.com/file/d/1eL3ZykC0neI0Yh-oTJpbHYby-1kq7plZ/view?usp=drive_link
* 댓글있는 글 목록(JSON)(~2023.9.11) : https://drive.google.com/file/d/1LpVjnq1jp4KnScCFaH3pP0bTYUq6lGkO/view?usp=drive_link


### 고민글
* 최근 10만건 : https://drive.google.com/drive/folders/1yOq_frrXIUENW0CT_kww581c5PSx9CbY?usp=drive_link

