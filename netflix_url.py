from bs4 import BeautifulSoup
import pandas as pd
import requests
import openpyxl
from time import sleep

wb = openpyxl.Workbook()
sheet = wb.active

code = pd.read_excel('netflix_code.xlsx')
code = sum(pd.DataFrame(code).values.tolist(), [])

for i in range(len(code)):
    url = 'https://www.netflix.com/kr/title/' + str(code[i])

    response = requests.get(url)
    sleep(1)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('#section-hero > div.hero-container > div.info-container > div.details-container > div').text
    
        sheet[f'A{i+2}'] = title
    
wb.save('net_text.xlsx')