from django.db import models
from django.utils import timezone

class Comment(models.Model):
    content = models.TextField()
    pubDate = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=15)
    likes = models.PositiveIntegerField(default=0)

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    pubDate = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=15)
    lectName = models.CharField(max_length=20)
    comments = models.ManyToManyField(Comment)
    likes = models.IntegerField(default=0) #좋아요 수 필드 추가
    files = models.FileField(upload_to='post_files', blank=True, null=True)
    images = models.ImageField(upload_to='post_images', blank=True, null=True)
    font = models.CharField(max_length=50, blank=True)
    fontSize = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.pk}. {self.title} - {self.author} ({self.pubDate})"
    # 글 번호, 제목, 작성자, 작성시간 표시

class TestPost(models.Model):
    postname = models.CharField(max_length=50)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname
