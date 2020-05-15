from bs4 import BeautifulSoup
import requests as re
import pandas as pd
from sys import argv
from time import sleep
import time
from tqdm import tqdm
ts = time.time()

url = 'https://www.ptt.cc/bbs/NBA/index.html'
r = re.get(url) # 200 is ok
soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find_all(class_ = 'title') # list of all titles
author = soup.find_all(class_ = 'author') # list of all authors
date = soup.find_all(class_ = 'date') # list of all dates
titles = []
authors = []
dates = []
# Put everything into lists

for t,a,d in zip(title, author, date):
    titles.append(t.text)
    authors.append(a.text)
    dates.append(d.text)

# TODO: Get content of next page
q = int(argv[1])
for n in tqdm(range(q)):
    sleep(0.1)
    next_page_btn = soup.find_all(class_="btn wide")[1]
    url= 'https://www.ptt.cc' + next_page_btn.get('href')
    # print(url)
    r = re.get(url) # 200 is ok
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find_all(class_ = 'title') # list of all titles
    author = soup.find_all(class_ = 'author') # list of all authors
    date = soup.find_all(class_ = 'date') # list of all dates
    # Put everything into lists
    for t,a,d in zip(title, author, date):
        titles.append(t.text)
        authors.append(a.text)
        dates.append(d.text)
# 
#
#

# Convert list to dictionary
dict = {
    '標題':titles,
    '作者':authors,
    '日期':dates
}
# Convert dictionary into dataFrame
df = pd.DataFrame(dict)


# print('The shape is: ', df.shape)
print(df)

# TODO: save df to csv
df.to_csv('test.csv', encoding ="utf_8_sig")
te = time.time()
print(te-ts)
# 1.re 抓網頁內容
# 2.bs4 解析內容
# 3.soup.find(class_)
# 4.存進List
# 5. list轉成dictionary
# 6. dictionary轉成 dataFrame
# 7. 把dataFrame存成csv