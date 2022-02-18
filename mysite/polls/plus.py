from io import BytesIO
import magic
import requests
import pandas as pd

def download(url):
    response = requests.get(url)
    binary_data = response.content
    temp_file = BytesIO()
    temp_file.write(binary_data)
    temp_file.seek(0)
    return temp_file

# 파일 확장자 추출
def get_buffer_ext(buffer):
    buffer.seek(0)
    mime_info = magic.from_buffer(buffer.read(), mime=True)
    buffer.seek(0)
    return mime_info.split('/')[-1]

def recommend_save(code,title,pk):

    ex = pd.read_excel('C:/Users/user/OneDrive/문서/파이썬/netflix/netflix_sim.xlsx')
    ex = pd.DataFrame(ex).values.tolist()
        
    code = ex[pk-1][1]
    title = ex[pk-1][2]
        
    return code, title
