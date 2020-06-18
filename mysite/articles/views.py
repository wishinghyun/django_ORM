from django.shortcuts import render, redirect
# (index) 모델 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 전체 데이터 가져오기
    # 그 데이터 템플릿에게 넘겨주기
    # 템플릿에서 반복문으로 각각의 게시글의 pk, title 보여주기
    articles = Article.objects.all()[::-1]
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 데이터 생성을 위한 ORM 활용
    Article.objects.create(title=title, content=content)
    #DB에 데이터가 바뀌므로 redirect 시켜준다
    return redirect('articles:index')

#1. 상세페이지를 보기 위한 경로
#1-1 특정 게시글에 대한 고유 값
#1-2 /articles/1/, /articles/2/
# 값을 넘겨주는 곳에서 아래 2개와 같이 pk값을 넘겨준다.
# /articles/{{ article.pk }}
# {% url 'articles:detail' article.pk %}
#2. 해당 게시글에 대한 상세 내용
#2-1 게시글의 pk,title,...
#3 인덱스 페이지로 돌아가는 링크

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

#1 특정 글 삭제를 위한 경로 작성
#1-1 /articles/1/delete/
#2 글 삭제 처리를 해주는 view 작성
#3 글 삭제 후, index page로 redirect
#4 글 삭제를 위한 링크 detail에 작성

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # request.method로 어떻게 해서 POST일때만 삭제되게 
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    #POST가 아니면 원래의 detail로 보냄
    return redirect('articles:detail', article.pk)

#edit
#1 특정 글 수정을 위한 경로 생성
#1-1 /articles/1/edit/
#2 글 수정 template을 render하는 edit view작성
#2-1 해당 template에 form tag 작성
#2-2 각 input tag 내부에 기존 내용이 들어있어야 함
#2-3 value속성을 활용
#update
#3 edit 보낸 데이터 처리를 위한 경로 생성
#3-1 /articles/1/update/
#4 글 수정 처리를 하는 update view작성
#5 해당 글 상세 페이지로 redirect
#6 글 수정을 위한 edit 링크 해당 글 상세 페이지에 생성
#6-1 {% url 'articles:edit' article.pk %}
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article_pk)


#1. /introduce/
#2. h1태그로 이루어진 제목
#2-1. 각각의 p 태그에 이름과 나이 작성
#3. back 링크로 index로 돌아갈 수 있는 링크 하나
#4. index에서 introduce 이동할 수 있는 링크 하나
#5. base.html 상속받아서 block body 안에 작성

def introduce(request):
    return render(request, 'articles/introduce.html')