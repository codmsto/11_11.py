# pip install requests
# pip install beautifulsoup
# pip install selenium



import requests
from bs4 import BeautifulSoup

# 1. URL설정
#   - 수집하고 싶은 웹사이트 설정
url = "https://v.daum.net/v/20241028164052926"

# 2.전체 소스 코드 가져오기
#  - 상대 코드
#     200(성공)
#     400대(클라이언트 오류)
#     500대 (서버 오류)
result = requests.get(url)
# print(result)
# print(result.text)

# 3. BS가 읽을 수 있도록 전체 소스코드 파싱
doc = BeautifulSoup(result.text, "html.parser")

# 4. 웹 크롤링
#   -select() -> LIST Type
# title = doc.select("he.tit_view")[0].get_text()


#아래 gpt수정
titles = doc.select("he.tit_view")

if titles:
    title = titles[0].get_text()
else:
    title = "제목을 찾을 수 없습니다."  # Default message if no title is found


contents = doc.select("section > p")   # [<p>본1</p>, <p>본2</p>]
content = ""
for text in contents:
    # text -> <p>본1</p>
    content += text.get_text()  # -> "본1 + 본2"

writer = doc.select("span.txt_info")[0].get_text()



reg_date = doc.select("span.num_date")[0].get_text()
# 2024. 10. 28. 16:40
# print(f"기사 날짜: {reg_date}")  #20241028
list_date = reg_date.split(". ")


# 1. 단독 strip()
# reg_date = list_date[0] + list_date[1] + list_date[2].strip()
# 2. 리스트 컴프린핸션
# ["년","월","일","시간"]
# list_date = [x.strip() for x in list_date]
# 3. lambda식
#  - map, reduce, filter
# list_date = list(map(lambda x: x.strip(), list_date))

reg_date = list_date[0] + list_date[1] + list_date[2]







print(f"뉴스제목:{title}")
print(f"뉴스 기자: {writer}")
print(f"뉴스 본문:{content}")
print(f"뉴스 날짜:{reg_date}")
