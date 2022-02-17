# Model 파일을 수정할 시 필수 사항



0. model 파일 수정
1. 마이그레이션 생성

```
$ python manage.py makemigrations
```

2. 마이그레이션 마이그레이트

```
$ python manage.py migrate
```

3. 서버 실행

```
$ python manage.py runserver
```

\+ 1 에서 "No migrations to apply."라고 뜨는데 서버 실행에서 에러가 발생한다면 'migrations' 폴더에 마지막 파일을 지우고 다시 시도해본다.
