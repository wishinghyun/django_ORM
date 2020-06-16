from django.db import models

# Create your models here.
class Article(models.Model) : 
    # articles_article
    title = models.CharField(max_length=150) # CharField : 글자수 제한할때 사용
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 생성될 때의 시간
    uadated_at = models.DateTimeField(auto_now=True) # 변경될 때의 시간

    def __str__(self):
        return f'{self.id}번째글 - {self.title} : {self.content}'