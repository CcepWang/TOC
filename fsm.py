from transitions.extensions import GraphMachine

from utils import send_text_message

import requests
from bs4 import BeautifulSoup

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "go to state3"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
        sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel

        a = ""
        for s in sel:
            a=a+(s.text)
            a=a+"\n"

        reply_token = event.reply_token
        send_text_message(reply_token, a)
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        r = requests.get("https://www.ptt.cc/bbs/joke/index.html")
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
        sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel

        b = ""
        for s in sel:
            b=b+(s.text)
            b=b+"\n"

        reply_token = event.reply_token
        send_text_message(reply_token, b)
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        r = requests.get("https://www.ptt.cc/bbs/NBA/index.html")
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
        sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel

        c = ""
        for s in sel:
            c=c+(s.text)
            c=c+"\n"


        reply_token = event.reply_token
        send_text_message(reply_token, c)
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")
