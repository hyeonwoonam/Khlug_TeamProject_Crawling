import csv
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import collections

# 아래는 matplotlib 한글 깨짐 방지
import platform
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결


# user agent를 입력해야 함
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

# 검색 내용, 크롤링 할 첫 페이지~ 마지막 페이지 입력
query = input("검색어를 입력하시오 : ")
page1 = int(input("첫 페이지를 입력하시오 : "))
page2 = int(input("마지막 페이지를 입력하시오 : "))

# 크롤링 내용을 csv 파일로 저장
filename = f"{query}.csv"
f = open(filename, "w", encoding = "utf-8-sig", newline="")
writer = csv.writer(f)

abcd_title = ["기사제목", "링크", "언론사"]
writer.writerow(abcd_title)

# 크롤링 과정, 기사는 최신순으로 정렬되어 있음
office_list = []
for first in range(page1, page2+1): # 첫 페이지부터 끝 페이지까지 돌리기
    url = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={query}&sort=1&photo=0&field=0&pd=0&ds=&de=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:all,a:all&start={first*10-9}"

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")


    
    news_area = soup.find_all("div", attrs={"class":"news_area"})
    for i in news_area:
        title = i.find("a", attrs={"class":"news_tit"}).get_text()
        link = i.find("a", attrs={"class":"news_tit"})["href"]
        press = i.find("a", attrs={"class":"info press"}).stripped_strings
        
        for k in press:
            if k == "언론사 선정":
                continue
            elif k != "언론사 선정":
                m = k
        office_list.append(m)
                
                
        list1 = [title,link,m]
        writer.writerow(list1)
        print(list1)

