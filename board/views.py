from django.shortcuts import render, redirect
from .models import *
from django.http import HttpRequest, HttpResponse

def Bulletinboard(request): #게시판 렌더링 함수
    if request.method == 'POST':   #POST 요청인지 확인, POST 요청이면 새로운 게시물 생성
        postTitle = request.POST.get('title')
        postContent = request.POST.get('content')
        postAuthor = request.POST.get('author')
        postLectName = request.POST.get('lectName') #전달된 데이터 변수에 할당
        postIt = Post.objects.create(
            title=postTitle,
            content=postContent,
            author=postAuthor,
            lectName=postLectName
        ) # 새 postIt 개체를 생성하여 데이터 할당
        return redirect('BulletinBoard') # 사용자를 게시판 페이지로 리디렉션
    
    
    if request.method == 'GET' and 'COMMENT' in request.GET:
        # 메서드가 GET이고, 매개변수에 COMMENT가 있는 경우 새로운 댓글 생성
        commentContent = request.GET.get('COMMENT')
        commentAuthor = request.GET.get('commentAuthor')
        postID = request.GET.get('postID')
        # 전달된 데이터 변수에 할당

        if commentContent and commentAuthor and postID:
        # commentContent, commentAuthor, postID가 모두 존재할경우
            post = Post.objects.get(pk=postID) # 해당 postID에 해당하는 Post 객체를 가져옴
            comment = Comment.objects.create(
                content=commentContent,
                author=commentAuthor
            ) # 새 comment 객체 생성하여 데이터를 할당
            post.comments.add(comment) # post 객체의 comments 필드에 새로운 comment 추가
     

def Vision(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = TestPost.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴 
    return render(request, 'board/blog.html', {'postlist':postlist})

def Posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = TestPost.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'board/posting.html', {'post':post})

def NewPost(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=TestPost.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=TestPost.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/board/')
    return render(request, 'board/newpost.html')

def RemovePost(request, pk):
    post = TestPost.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/board/')
    return render(request, 'board/remove_post.html', {'Post': post})

# 로그인한 사용자에게만 게시판 표시하는 함수
def index(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("/accounts/login")
    qs = Post.objects.all()
    return render(request, "board/blog.html", context={"postList": qs})

# 게시글 좋아요 함수
def likePost(request, postId):
    if request.method == "POST":
        try:
            post = Post.objects.get(pk=postId)
            if post.is_liked_by_user:  # 이미 좋아요를 눌렀을 경우
                post.likes -= 1  # 좋아요 수 감소
                post.is_liked_by_user = False  # 좋아요 상태 변경
            else:  # 좋아요를 누르지 않았을 경우
                post.likes += 1  # 좋아요 수 증가
                post.is_liked_by_user = True  # 좋아요 상태 변경
            post.save()
        except Post.DoesNotExist:
            pass
    return redirect('post_detail')

# 댓글 좋아요 함수
def likeComment(request, commentId):
    if request.method == "POST":
        try:
            comment = Comment.objects.get(pk=commentId)
            if comment.is_liked_by_user:  # 이미 좋아요를 눌렀을 경우
                comment.likes -= 1  # 좋아요 수 감소
                comment.is_liked_by_user = False  # 좋아요 상태 변경
            else:
                comment.likes += 1  # 좋아요 수 증가
                comment.is_liked_by_user = True  # 좋아요 상태 변경
            comment.save()
        except Comment.DoesNotExist:
            pass
    return redirect('post_detail')
