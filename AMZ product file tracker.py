import bs4 as bs
import  sys
import schedule
import time
import  urllib.request
from PyQt5.QtCore import  QUrl
from PyQt5.QtWidgets import  QApplication
from PyQt5.QtWebEngineWidgets import  QWebEnginePage

import  winsound

frequency = 2500
duration = 1000

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def  _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load Finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

def exact_url(url):
    index = url.find("B0")
    index = index + 10
    current_url = ""
    current_url = url [:index]
    return  current_url


def main_prog():
    url = "https://www.amazon.de/Amazon-Echo-Vorherige-Generation-general%C3%BCberholt/dp/B01DFKBNHU"
    exacturl = exact_url(url)
    page = Page(exact_url)
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    js_test = soup.find('span', id='priceblock_ourprice')

    if js_test is None:
        js_test =  soup.find('span', id='priceblock_dealprice')
    str = ""

    for line in js_test.stripped_strings:
        str  = line

    str = str.replace(", ", "")
    current_price = int(float(str))
    your_price = 600
    if  current_price < your_price :
            print("Price decreased")
            winsound.Beep(frequency,duration)
    else:
        print("price is still high")

def job():
    print("Tracking.......")
    main_prog()

#schedule
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

print(Page)

#self  in def


