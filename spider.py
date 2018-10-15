import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

import requests
import re
import threading
from bs4 import BeautifulSoup
import jieba
from webs.models import Post


urls = ["https://new.qq.com/cmsn/20180904/20180904002887.html",
        "https://new.qq.com/omn/20180904/20180904A1LIKH.html",
        "https://new.qq.com/omn/20180904/20180904A11MQ9.html",
        "https://new.qq.com/omn/20180904/20180904C0C4IE.html",
        "https://new.qq.com/omn/20180904/20180904A17NLY.html",
        "https://new.qq.com/cmsn/20180904/20180904081340.html",
        "https://new.qq.com/cmsn/20180904/20180904081437.html",
        "https://new.qq.com/omn/20180904/20180904A1JWHF.html",
        "https://new.qq.com/cmsn/20180904/20180904076532.html",
        "https://new.qq.com/cmsn/20180904/20180904080267.html"]


class myThread (threading.Thread):
    def __init__(self, threadID, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.url = url
    def run(self):
        response = requests.get(self.url)
        html = response.text

        soup = BeautifulSoup(html, 'lxml')

        titles = soup.find('title').get_text()
        
        links = soup.find_all('p') #文章内容
        body = ""
        for link in links:
            if link.get_text().strip() !=  '':
                body = body + link.get_text().strip() + '\n'
        
        Post.objects.create(title = titles, content = body, site = self.url)


        


Post.objects.all().delete()
# 创建新线程
thread = []
a = 0
for url in urls:
    thread.append(myThread(a+1, url))
    a = a + 1

# 开启新线程
thread[0].start()
thread[1].start()
thread[2].start()
thread[3].start()
thread[4].start()
thread[5].start()
thread[6].start()
thread[7].start()
thread[8].start()
thread[9].start()
thread[0].join()
thread[1].join()
thread[2].join()
thread[3].join()
thread[4].join()
thread[5].join()
thread[6].join()
thread[7].join()
thread[8].join()
thread[9].join()

