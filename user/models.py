from django.db import models
from MySQLdb.constants.FLAG import AUTO_INCREMENT

class User(models.Model):
    id = models.CharField(max_length=30, verbose_name="아이디", primary_key=True)
    passwd = models.CharField(max_length=30, verbose_name="비밀번호", null=False)
