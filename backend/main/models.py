from django.db import models
from MySQLdb.constants.FLAG import AUTO_INCREMENT
# Create your models here.

class Member(models.Model):
    no = models.AutoField(verbose_name="번호", primary_key=True)
    name = models.CharField(verbose_name="이름", null=False, max_length=255)
    id = models.CharField(verbose_name="아이디",null=False,max_length=255 )
    phone = models.CharField(verbose_name="전화번호", null=False, max_length=255)
    email = models.CharField(verbose_name="이메일", null=False, max_length=255)
    pw = models.CharField(verbose_name="비밀번호", max_length=30,  null=False)
    
class Result(models.Model):
    no = models.AutoField(verbose_name="번호", primary_key=True)
    image = models.ImageField(verbose_name="이미지", upload_to='result/', null=True)
    result = models.CharField(verbose_name="결과", max_length=10)
    date_time = models.DateTimeField(verbose_name="날짜")
    humidity = models.FloatField(verbose_name="습도")
    temp = models.FloatField(verbose_name="온도")

class ImageUpload(models.Model):
    no = models.AutoField(verbose_name="번호", primary_key=True)
    image = models.ImageField(verbose_name="이미지", null=True)