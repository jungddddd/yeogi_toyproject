
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    priority = models.IntegerField(default=1)  # 1: 낮음, 2: 중간, 3: 높음
    image = models.ImageField(upload_to='todos/', null=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

