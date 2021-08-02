import requests
from bs4 import BeautifulSoup
import time

KEYWORD = input("키워드를 입력해주세요. : ")
PAGE = int(input("Crawiling을 진행할 page 수를 입력해주세요. : "))

time = time.localtime()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"}

def create_soup(url) :
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_1page() :
    url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + KEYWORD + "&sort=0&photo=0&field=0&pd=0&ds=&de=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1"  

    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"list_news"}).find_all("li", attrs={"class":"bx"})
    for index , news in enumerate(news_list) :
        title = news.find("div", attrs={"class":"news_area"}).find("a", attrs={"class":"news_tit"})["title"]
        link = news.find("div", attrs={"class":"news_area"}).find("a", attrs={"class":"news_tit"})["href"]
        
        press = []
        for press_pick in news.find("div", attrs={"class":"news_area"}).find("div", attrs={"class":"news_info"}).find("div", attrs={"class":"info_group"}).find("a", attrs={"class":"info press"}).stripped_strings :
            press.append(press_pick)

        print("{}. {}".format(index+1, title))
        print("   링크 : {}".format(link))
        print("   언론사 : {}".format(press[0]))

def scrape_news() :
    print("[뉴스 정보]")
    print("Crawiling을 진행한 시각 {}.{}.{} {}:{}:{}".format(time.tm_year, time.tm_mon, time.tm_mday, time.tm_hour, time.tm_min, time.tm_sec))
    print()

    if PAGE == 1 :
        scrape_1page()  # 1page일 경우 start=1, 2page일 경우 start=11, 3page일 경우 start=21 이므로 규칙성을 위해 1page에서 Crawiling하는 과정은 함수처리하였다.
    elif PAGE > 1 :
        scrape_1page()

        page_index = 10

        for i in range(1, PAGE) :
            url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + KEYWORD + "&sort=0&photo=0&field=0&pd=0&ds=&de=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=" + str(i) + "1"
            
            soup = create_soup(url)
            news_list = soup.find("ul", attrs={"class":"list_news"}).find_all("li", attrs={"class":"bx"})   # 관련 기사가 있을 경우 <li class="sub_bx"> 가 존재하므로 attrs={"class":"bx"} 를 추가하여 메인 기사의 정보가 담겨있는 li 태그만 찾도록 하였다.
            for index , news in enumerate(news_list) :
                title = news.find("div", attrs={"class":"news_area"}).find("a", attrs={"class":"news_tit"})["title"]
                link = news.find("div", attrs={"class":"news_area"}).find("a", attrs={"class":"news_tit"})["href"]
                
                # 해당 언론사가 주요 기사로 직접 선정하여 'PICK' 이 붙어있다면 언론사를 불러오는 과정에서 '언론사 선정' 이라는 문자열이 같이 출력된다. 이를 방지하기 위해서 for문과 .stripped_strings 를 통해 각 문자열을 리스트에 저장하고 첫 번째 요솟값(언론사)을 출력한다.
                press = []
                for press_pick in news.find("div", attrs={"class":"news_area"}).find("div", attrs={"class":"news_info"}).find("div", attrs={"class":"info_group"}).find("a", attrs={"class":"info press"}).stripped_strings :
                    press.append(press_pick)

                page_index = page_index + 1

                print("{}. {}".format(page_index, title))
                print("   링크 : {}".format(link))
                print("   언론사 : {}".format(press[0]))

if __name__ == "__main__" :
    scrape_news()   #뉴스 정보 가져오기
