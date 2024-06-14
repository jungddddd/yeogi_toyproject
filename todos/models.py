
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(blank=True, null=False)
    detail = models.TextField(blank=True, null=False)
    priority = models.IntegerField(default=1)  # 1: 낮음, 2: 중간, 3: 높음
    #image = models.ImageField(upload_to='todos/', null=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    #original_url = models.URLField()  # 원본 자료를 볼 수 있는 URL
    #related_site_url = models.URLField()  # 관련 자료조사 사이트로 이동할 수 있는 URL
    last_modified = models.DateTimeField(auto_now=True)  # 최근 수정일
    #due_date = models.DateTimeField()  # 마감 기한 (날짜와 시간 포함)



    def __str__(self):
        return self.title

