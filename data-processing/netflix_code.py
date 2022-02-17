from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
import re

wb = openpyxl.Workbook()
sheet = wb.active

def code_crawling():
    url = 'https://www.netflix.com/kr/login'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe",options=options)
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    driver.find_element_by_name('userLoginId').send_keys('아이디')
    driver.find_element_by_name('password').send_keys('비밀번호')
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
    time.sleep(5) # NoSuchElementException 오류 해결
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div').click()
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/ul/li[3]/a').click() # 시리즈
    #driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/ul/li[4]/a').click() # 영화
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/button').click()
    time.sleep(5)
    
    i1 = 0
    i2 = 0
    n = 2
    while True:
        try:
            code = driver.find_element_by_css_selector(f'#title-card-{i1}-{i2} > div.ptrack-content > a').get_attribute('href')
            a = re.compile('watch/([0-9]+)\?tctx')
            code = a.findall(code)
            
            sheet[f'A{n}'] = code[0]
            
            i2 += 1
            n += 1
            
            if i2 > 5 : 
                i1 += 1
                i2 = 0
                
                scroll_location = driver.execute_script("return document.body.scrollHeight")
                # 스크롤 다운
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        except: break

code_crawling()
wb.save('netflix_code.xlsx')
