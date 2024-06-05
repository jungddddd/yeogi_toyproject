from django.db import models

# Create your models here.

class Member(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    email = models.CharField(max_length=64,verbose_name = '이메일',unique=True)
    password = models.CharField(max_length=20,verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='가입일자')#저장되는 시점의 시간을 자동으로 삽입해준다.


    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'member'

