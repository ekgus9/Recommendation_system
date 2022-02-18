import pandas as pd
import re
import json
import numpy as np
from image import image_craw

text = pd.read_excel('netflix_sep.xlsx')
text = pd.DataFrame(text)
text = text.fillna("None")

title = []
year = []
age = []
season = []
genre = []
story = []
people = []
title_sp = []

jsonf = []

for i in range(len(text)):

    title.append(text.iloc[i][0])
    year.append(str(text.iloc[i][1]))
    age.append(text.iloc[i][2])
    season.append(text.iloc[i][3])
    genre.append(text.iloc[i][4])
    story.append(text.iloc[i][5])
    people.append(text.iloc[i][6])
    
    a = re.compile('[\s\:\;\!~@#$%\^\&\*\-\+\=\[\]\{\}\<\>\,\.\?\/]')
    a = a.sub('',text.iloc[i][0])
    title_sp.append(a)
    image_url = image_craw(text.iloc[i][0])
    
    jsonf.append({'model':"polls.title_data","fields": {'title':text.iloc[i][0],'year':str(text.iloc[i][1]),'age':text.iloc[i][2],'season':text.iloc[i][3],\
        'genre':text.iloc[i][4],'story':text.iloc[i][5],'people':text.iloc[i][6],'title_sp':a,'photo_url':image_url}})

with open('./mysite/polls/fixtures/posts-data.json', 'w') as f:
	json.dump(jsonf, f)

# python manage.py loaddata polls/fixtures/posts-data.json