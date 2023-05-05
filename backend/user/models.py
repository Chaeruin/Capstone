from django.db import models
from MySQLdb.constants.FLAG import AUTO_INCREMENT

class User(models.Model):
    no = models.AutoField(verbose_name="번호", primary_key=True)
    id = models.CharField(verbose_name="아이디",null=False,max_length=30 )
    name = models.CharField(verbose_name="이름", null=False, max_length=30)
    nickname = models.CharField(verbose_name="닉네임", null=False, max_length=10)
    pw = models.CharField(verbose_name="비밀번호", max_length=30,  null=False)
    email = models.CharField(verbose_name="이메일", null=False, max_length=10)
    phone = models.CharField(verbose_name="전화번호", null=False, max_length=13)