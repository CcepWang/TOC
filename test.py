import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/NBA/index.html")
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser

#u = soup.select("div.btn-group.btn-group-paging a")#上一頁按鈕的a標籤
#url = "https://www.ptt.cc"+ u[1]["href"] #組合出上一頁的網址

#import requests
#from bs4 import BeautifulSoup
#url = "https://www.ptt.cc/bbs/joke/index.html"
#for i in range(3): #往上爬3頁
 #   r = requests.get(url)
 #   soup = BeautifulSoup(r.text,"html.parser")
 #   sel = soup.select("div.title a") #標題
 #   u = soup.select("div.btn-group.btn-group-paging a") #a標籤
 #   #print ("本頁的URL為"+url)
 #   url = "https://www.ptt.cc"+ u[1]["href"] #上一頁的網址

#a = ""
#for s in sel: #印出網址跟標題
#    a=a+(s.text)
#    a=a+"\n"
#print(a)

sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
print(sel)

a = ""
for s in sel:
    a=a+(s.text)
    a=a+"\n"
print(a)
#print(list_a) 
#soup = BeautifulSoup(r.text,"html.parser")

#data=soup.find_all("table", class_="FcstBoxTable01")

#data2=soup.find_all("tbody")

#print(data)


#print(r.encoding) #查看網頁返回的字符集類型
#print(r.apparent_encoding) #自動判斷字符集類型

#data2=soup.find_all("div", id="ftext")
#print(data2)

