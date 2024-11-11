# 웹 크롤링(Web Crawling)
#  -> 뉴스기사 수집 프로그램 개발
#  -> 웹 사이트의  데이터를 수집 기술

# *URL: 해당 웹사이트의 주소

# 1. 라이브러리
#  - requests      : URL 접속해서 전체 소스코드(HTML) 가져오기(정적)
#  - beautifulsoup : 전체 소스코드(HTML)에서 원하는 정보 수집 
#  - selenium      : URL 접속해서 전체 소스코드(HTML) 가져오기(동적)
#                   + 마우스, 키보드 조작 가능!


# ~ 웹 크롤링 조합법
#  1) requests + beautifulsoup(정적)
#  2) selenium(동적)
#  3) selenium + beautifulsoup(동적)

# 2. 도메인 널리지
#  1) 웹 프로세스
#   - 웹브라우저(클라이언트)
#       아래
#   - request(https://www.naver.com)
#       아래
#   - 네이버 서버 
#       아래
#   - response(소스코드 및 이미지 등)
#       아래
#   - 웹 브라우저(랜더링)


# 3. 웹 표준 디자인
#  - IEEE 국제 기구 -> 웹 사이트 디자인은 웹 표준으로 디자인하세요!
#  - 웹 표준(HTML, CSS, Javascript)
#  - HTML (웹 사이트의 구성을 설계)
#  - CSS (디자인)
#  - JS(기능)
# * 웹 브라우저 종류: 네이버 웨일, 크롬, 파이어폭스, 사파리, 엣지, 오페라

# 4. HTML
#  - 하이퍼 텍스트 마크업 언어
#  - 태그로 구성  ex) <dic class = "contents"v>Hello</div>
#  - 태그는 상위-하위 관계
#     ex) <div>
#         <div>Hi</div>
#         <div>
#           Hello
#           <span>안녕</span>
#        </div>
#      </div>

# 5. 선택자
#  1) 태그 선택자(X)  ex) div, span
#  2) 자식 선택자(>)  ex) div > span
#  3) 자손 선택자( )  ex) div span
#  4) 아이디 선택자(#), 유니크(1개) ex) div#box
#  5) 클래스 선택자(.), 복수개  ex)div.contents


