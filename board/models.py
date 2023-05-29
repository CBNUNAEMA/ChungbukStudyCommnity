from django.db import models

class Comment(models.Model):
    content = models.TextField()
    pubDate = models.DateTimeField()
    author = models.CharField(max_length=15)

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    pubDate = models.DateTimeField()
    author = models.CharField(max_length=15)
    lectName = models.CharField(max_length=20)
    comments = models.ManyToManyField(Comment)

class TestPost(models.Model):
    postname = models.CharField(max_length=50)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname