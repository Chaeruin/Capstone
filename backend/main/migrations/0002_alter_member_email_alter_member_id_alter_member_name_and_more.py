# Generated by Django 4.2 on 2023-05-10 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=255, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.CharField(max_length=255, verbose_name='아이디'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=255, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='전화번호'),
        ),
    ]
