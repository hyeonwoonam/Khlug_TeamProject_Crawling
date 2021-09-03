import requests
from bs4 import BeautifulSoup
import time
import tkinter.ttk as ttk
from tkinter import *
root = Tk()
root.title("CRAWLING GUI") 
root.geometry("640x480+700+300")
root.resizable(False, False) # 너비, 높이 값 변경 불가 -> 창 크기 변경 불가, 최소화도 안됨

time = time.localtime()

# 현재 시간 레이블
time_label = Label(root, text = "크롤링 진행 시간")
time_label.pack()

# 텍스트 프레임 - 결과 창
txt_frame = Frame(root)
txt_frame.pack(fill="x", padx=10, pady=10)

scrollbar = Scrollbar(txt_frame)
scrollbar.pack(side="right", fill="y")

txt_file= Text(txt_frame, height=15, yscrollcommand=scrollbar.set)
txt_file.pack(side="left",  expand=True, fill="both")
scrollbar.config(command=txt_file.yview)

# INPUT 프레임 - input 으로 받는 값

input_frame = LabelFrame(root, text="INPUT")
input_frame.pack(fill="x", padx=5, pady=5)

# 키워드 텍스트
keyword_label = Label(input_frame, text="키워드", width=8)
keyword_label.pack(side="left", padx=5, pady=5)

keyword_txt = Entry(input_frame, width=30)
keyword_txt.pack(side="left")
keyword_txt.insert(0, "키워드를 입력하시오")

# 크롤링 페이지 수
page_label = Label(input_frame, text="크롤링 페이지 수")
page_label.pack(side="left", padx=5, pady=5)

page_values = [int(i) for i in range(1,16)] 

page_combobox = ttk.Combobox(input_frame,width=2 , height=5, values=page_values,state="readonly")
page_combobox.current(0)
page_combobox.pack(side="left",padx=5, pady=5)

# 검색 옵션
search_label = Label(input_frame, text="검색옵션")
search_label.pack(side="left", padx=5, pady=5)

search_value = ["관련도순", "최신순", "오래된순"] 

search_combobox = ttk.Combobox(input_frame,width=20 , height=5, values=search_value, state="readonly")
search_combobox.current(0)
search_combobox.pack(side="left",padx=5, pady=5)

# 추천 키워드
recommand_frame = Frame(root)
recommand_frame.pack(fill="x", padx=10, pady=10)

recommand_label = Label(recommand_frame, text= "추천 키워드")
recommand_label.pack()

recommand_txt = Entry(recommand_frame, width=20)
recommand_txt.pack()
# progress 창
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack( fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 시작 버튼
start_frame = Frame(root)
start_frame.pack( fill="x", padx=5, pady=10)

def btncmd1():
    pass

def btncmd2():
    pass

start_btn1 = Button(start_frame,width=10, height=3 ,text="1차 크롤링", command=btncmd1)
start_btn1.pack(side="left", padx=10)

start_btn2 = Button(start_frame,width=10, height=3 ,text="재크롤링", command=btncmd2)
start_btn2.pack(side="right", padx=10)

root.mainloop()
