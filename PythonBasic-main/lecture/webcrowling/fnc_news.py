import requests
from bs4 import BeautifulSoup

#URL -> 제목, 기자 , 날짜 , 본문 수집
def get_news_info(url:str):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h1.tit_view")[0].get_text()
    contents = doc.select("section > p")  
    content = ""
    for text in contents:
        content += text.get_text() 
        
    # 기자 0 : "span.txt_info" => [0]기자, [1]날짜
    # 기자 X : "span.txt_info" -> [0]날짜 해결해야 할 문제 
    writer_list = doc.select("span.txt_info")
    
    if len(writer_list)<2:
        writer = ""
    else:
        writer = writer_list[0].get_text()

    writer = doc.select("span.txt_info")[0].get_text()
    reg_date = doc.select("span.num_date")[0].get_text()
    list_date = reg_date.split(".")
    list_date = list(map(lambda x: x.strip(), list_date))
    reg_date = list_date[0] + list_date[1] + list_date[2]

# 오류남 

