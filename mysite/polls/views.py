from django.shortcuts import render, redirect
# View에 Model(Post 게시글) 가져오기
from .models import Title_data
from django import forms
from django.db.models import Q
from .plus import recommend_save
from django.views.generic import TemplateView, ListView

# index.html 페이지를 부르는 index 함수
def index(request):
    ost = Title_data.objects.all()
    search_key = request.GET.get('search_key')
    if search_key:
        ost = Title_data.objects.filter(title_sp__icontains=search_key)
    return render(request, 'main/index.html', {'ost':ost})

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Title_data.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴 
    return render(request, 'main/blog.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Title_data.objects.get(pk=pk)
    
    Title_data().save_file(post.photo_url,post.photo)
    
    if not post.re_code and not post.re_title:
        post.re_code,post.re_title = recommend_save(post.re_code,post.re_title,int(pk))
        post.save()
    
    sp_code = post.re_code.split(',')
    sp_title = post.re_title.split('*')
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post,'sp0':sp_code[0],'sp1':sp_code[1],'sp2':sp_code[2],'sp3':sp_code[3],'sp4':sp_code[4],\
        'spt0':sp_title[0],'spt1':sp_title[1],'spt2':sp_title[2],'spt3':sp_title[3],'spt4':sp_title[4]})

def get_queryset(request): # new
    ost = Title_data.objects.all()
    search_key = request.GET.get('search_key')
    if search_key:
        ost = Title_data.objects.filter(title__icontains=search_key)
    return render(request, 'main/index.html', {'ost':ost})
    
def new_post(request):
    if request.method == 'Title_data':
        if request.Title_data['photo']:
            new_article=Title_data.objects.create(
                title=request.POST['title'],
                photo=request.POST['photo'],
            )
        else:
            new_article=Title_data.objects.create(
                title=request.POST['title'],
                photo=request.POST['photo'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')
