from bs4 import BeautifulSoup
import requests
import time
import re

def image_craw(title):
    hdr={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=wlsrur&qdt=0&ie=utf8&query=' + title
    response = requests.get(url=url, headers=hdr)
    time.sleep(0.5)
    if response.status_code == 200:
        html = response.text
        time.sleep(0.5)
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(0.5)
        try:
            title = soup.find_all('div','detail_info')[0]
            ok = re.compile("<img.+src=\"(.+)\" width=\".+\"/> </a>")
        
            title = ok.findall(str(title))[0]
        except:
            title = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAyMTAyMDZfMjQy%2FMDAxNjEyNTg5ODg5NTIx.2sfBoxki3By0wxDuUFH_-ZgRGjgR2v9JNun0UUbYeHcg.DF9slgHgmxA75hLSZlxBAuL1DZI_I635S9TGVDak2mog.PNG%2FIFeGq4eGcKZvhfV75MkLa2aL_bhU.jpg&type=a340'

        image = title
        
    return title
