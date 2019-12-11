import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.cwb.gov.tw/V7/forecast/taiwan/Tainan_City.htm")
#r.encoding = "gbk"
r.encoding = r.apparent_encoding

soup = BeautifulSoup(r.text,"html.parser")

data=soup.find_all("table", class_="FcstBoxTable01")

#data2=soup.find_all("tbody")

print(data)


#print(r.encoding) #查看網頁返回的字符集類型
#print(r.apparent_encoding) #自動判斷字符集類型

#data2=soup.find_all("div", id="ftext")
#print(data2)

