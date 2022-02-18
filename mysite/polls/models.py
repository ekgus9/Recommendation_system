from urllib.parse import urlparse

from django.core.files import File
from django.db import models

from polls.plus import download, get_buffer_ext


class Post(models.Model):
    postname = models.CharField(max_length=50)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    
    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname
    
class Title_data(models.Model):
    title = models.CharField(max_length=50)
    year = models.TextField()
    age = models.TextField()
    season = models.TextField()
    genre = models.TextField()
    story = models.TextField()
    people = models.TextField()
    title_sp = models.TextField()
    photo_url = models.URLField('URL', max_length=350, blank=True)
    photo = models.ImageField('이미지', upload_to='items', blank=True)
    re_code = models.TextField(blank=True)
    re_title = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
    def save_file(self, *args, **kwargs):
        if not args :return 
        # ImageField에 파일이 없고, url이 존재하는 경우에만 실행
        if args[0]:
            
            # 우선 purchase_url의 대표 이미지를 크롤링하는 로직은 생략하고, 크롤링 결과 이미지 url을 임의대로 설정  
            item_image_url = args[0]

            if not args[1]:
                temp_file = download(item_image_url)
                file_name = '{urlparse}.{ext}'.format(
                    # url의 마지막 '/' 내용 중 확장자 제거
                    # ex) url = 'https://~~~~~~/bag-1623898_960_720.jpg'
                    #     -> 'bag-1623898_960_720.jpg'
                    #     -> 'bag-1623898_960_720'
                    urlparse=urlparse(item_image_url).path.split('/')[-1].split('.')[0],
                    ext='jpg'#get_buffer_ext(temp_file)
                )
                args[1].save(file_name, File(temp_file))

