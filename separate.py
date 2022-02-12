# -*- coding: utf-8 -*-
import pandas as pd
import re
import openpyxl

text = pd.read_excel('netflix_text.xlsx')
text = sum(pd.DataFrame(text).values.tolist(), [])

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = '제목' ; sheet['B1'] = '제작년도' ; sheet['C1'] = '관람가' ; sheet['D1'] = '길이' ; sheet['E1'] = '장르' ; sheet['F1'] = '줄거리' ; sheet['G1'] = '주연'

for i in range(len(text)):

    pattern = re.compile('(?P<title>.+)(?P<year>[0-9]{4}) \| (?P<age>.+)\s+\| (?P<season>.+) \| (?P<genre>코미디 시리즈|액션 애니|청소년 시리즈|경쟁 리얼리티 시리즈|로맨틱 코미디 시리즈|사회 문제·TV 드라마|리얼리티 시리즈|스릴러 시리즈|범죄 시리즈|청소년 시리즈|가족이 함께 보는 시리즈|시트콤|망가 원작 시리즈|액션 & 어드벤처 시리즈|만화책 원작 TV 프로그램|로맨스 애니메이션|음악 & 뮤지컬|토크쇼|라이프스타일|범죄 실화 다큐멘터리|중국 본토 시리즈|SF 시리즈|키즈 시리즈|TV 만화|라이트 노벨 원작 애니메이션|호러 시리즈|미국 TV 프로그램|어린이 음악|키즈 교육 영화|애니 시리즈|다큐멘터리·역사|코미디|스릴러|가족 영화|드라마 장르|애니메이션 영화|로맨스·엉뚱하고 기발|도서 원작 영화|호러 영화|로맨틱한 영화|밀리터리 영화|액션 & 어드벤처|청춘 영화|인디 영화|미스터리|다큐멘터리 영화|어린이 & 가족 영화|영화·법정|LGBTQ 영화|시대물|스릴러 영화|실존 인물 다큐멘터리|무술 영화|과학 & 자연 다큐멘터리|미국 영화|밀리터리 영화|관능적 로맨틱 영화|발리우드 영화|어린이 음악|SF 영화|아프리카 영화|결혼식 & 로맨스 리얼리티 TV|TV 프로그램·법정|한국 드라마|메디컬 시리즈|여행 & 어드벤처 다큐멘터리|판타지 시리즈|중동 TV 쇼|도서 원작 시리즈|일본 소년 만화를 만나다|로맨스 애니메이션|스탠드업 코미디|고전 영화|블록버스터 코미디|사회 이슈 드라마 장르 영화|웹툰 원작 한국 드라마|드라마|힌디어 TV 쇼|다큐멘터리·밀리터리|비디오게임 원작 애니메이션|TV 프로그램·음식 & 여행|학교 배경 애니|실화 바탕 영화|중국 본토 영화|영화·스파이|중국 영화|다큐멘터리·정치|취미와 여가|과학 & 자연 TV 프로그램|콘서트 실황|로맨틱한 드라마|자연 & 생태 다큐멘터리)(?P<story>.+)주연:(?P<person>.+)')
    a = pattern.search(text[i])

    if a == None:
        pattern = re.compile('(?P<title>.+)(?P<year>[0-9]{4}) \| (?P<age>.+)\s+\| (?P<season>.+) \| (?P<genre>코미디 시리즈|액션 애니|청소년 시리즈|경쟁 리얼리티 시리즈|로맨틱 코미디 시리즈|사회 문제·TV 드라마|리얼리티 시리즈|스릴러 시리즈|범죄 시리즈|청소년 시리즈|가족이 함께 보는 시리즈|시트콤|망가 원작 시리즈|액션 & 어드벤처 시리즈|만화책 원작 TV 프로그램|로맨스 애니메이션|음악 & 뮤지컬|토크쇼|라이프스타일|범죄 실화 다큐멘터리|중국 본토 시리즈|SF 시리즈|키즈 시리즈|TV 만화|라이트 노벨 원작 애니메이션|호러 시리즈|미국 TV 프로그램|어린이 음악|키즈 교육 영화|애니 시리즈|다큐멘터리·역사|코미디|스릴러|가족 영화|드라마 장르|애니메이션 영화|로맨스·엉뚱하고 기발|도서 원작 영화|호러 영화|로맨틱한 영화|밀리터리 영화|액션 & 어드벤처|청춘 영화|인디 영화|미스터리|다큐멘터리 영화|어린이 & 가족 영화|영화·법정|LGBTQ 영화|시대물|스릴러 영화|실존 인물 다큐멘터리|무술 영화|과학 & 자연 다큐멘터리|미국 영화|밀리터리 영화|관능적 로맨틱 영화|발리우드 영화|어린이 음악|SF 영화|아프리카 영화|결혼식 & 로맨스 리얼리티 TV|TV 프로그램·법정|한국 드라마|메디컬 시리즈|여행 & 어드벤처 다큐멘터리|판타지 시리즈|중동 TV 쇼|도서 원작 시리즈|일본 소년 만화를 만나다|로맨스 애니메이션|스탠드업 코미디|고전 영화|블록버스터 코미디|사회 이슈 드라마 장르 영화|웹툰 원작 한국 드라마|드라마|힌디어 TV 쇼|다큐멘터리·밀리터리|비디오게임 원작 애니메이션|TV 프로그램·음식 & 여행|학교 배경 애니|실화 바탕 영화|중국 본토 영화|영화·스파이|중국 영화|다큐멘터리·정치|취미와 여가|과학 & 자연 TV 프로그램|콘서크 실황|로맨틱한 드라마|자연 & 생태 다큐멘터리)(?P<story>.+)')
        a = pattern.search(text[i])
        
    if a == None:
        pattern = re.compile('(?P<title>.+)(?P<year>[0-9]{4}) \| (?P<age>.+)\s+\| (?P<season>([0-9]+시간 [0-9]+분|시즌 [0-9]+개|[0-9]+시간|[0-9]+분))(?P<story>.+)주연:(?P<person>.+)')
        a = pattern.search(text[i])
        
    if a == None:
        pattern = re.compile('(?P<title>.+)(?P<year>[0-9]{4}) \| (?P<age>.+)\s+\| (?P<season>([0-9]+시간 [0-9]+분|시즌 [0-9]+개|[0-9]+시간|[0-9]+분))(?P<story>.+)')
        a = pattern.search(text[i])
        
    print(a)
    
    sheet[f'A{i+2}'] = a.group('title')
    sheet[f'B{i+2}'] = a.group('year')
    sheet[f'C{i+2}'] = a.group('age')
    
    try:
        sheet[f'D{i+2}'] = a.group('season')
    except:
        sheet[f'D{i+2}'] = ''
        
    try:
        sheet[f'E{i+2}'] = a.group('genre')
    except:
        sheet[f'E{i+2}'] = ''
        
    story = a.group('story')
    
    if '크리에이터' in story:
        pattern = re.compile('크리에이터:.+')
        person = pattern.sub('',story)
    sheet[f'F{i+2}'] = story
    
    try:
        person = a.group('person')
        if '크리에이터' in person:
            pattern = re.compile('크리에이터:.+')
            person = pattern.sub('',person)
        sheet[f'G{i+2}'] = person
    except:
        sheet[f'G{i+2}'] = ''

wb.save('netflix_sep.xlsx')