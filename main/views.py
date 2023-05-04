from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse, JsonResponse
import imageread
from datetime import datetime
from ..rspi import testDHT22 as dht
import pymysql, logging, sys
import dataprocess
import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_secret_key.json'


# Imports the Google Cloud client library
from google.cloud import vision 
from google.cloud.vision_v1 import types


class Main(View):   #main
    def get(self, request):
        template = loader.get_template("base.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("base.html")
        context = {        }
        return HttpResponse(template.render( context, request ))
    
class Login(View):  #로그인
    def get(self, request):
        template = loader.get_template("login.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("login.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

class Signup(View): #회원가입
    def get(self, request):
        template = loader.get_template("signup.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("signup.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

class Scandata(View):
    def get(self, request):
        template = loader.get_template("scandata.html")
        ident = imageread.texts[0].description

        # Decide the result of ident
        if ident == '11' or 'II':
            result = '양성'
        elif ident == '1' or 'I':
            result = '음성'
        else:
            result = '검출 오류'

        # Take real date time
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # id, humidity and temp

        # id = 0                        # auto increament, 자동 생성으로 바꾸기
        humidity = dht.humidity         # rsp 바로 연동해서 그 값 가져오기
        temp = dht.temperature          # rsp 바로 연동해서 그 값 가져오기
    

        
        # cursor.execute("show tables")
        #print(cursor.fetchall())

        # 무ㅓ넣을까
        # 일단 DB 새로 생성해놓고 (result db)
        # result, datetime, temp, humidity? 넘겨야 하나
        # 아니면 result fk fk ? 이건 너무 복잡할듯..
        query = """INSERT INTO result(result, date_time, temp, humidity)
                    VALUES (%s, %s, %.1f, %.1f)"""
        
        context = {        }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("scandata.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

class Datainner(View):
    def get(self, request):
        template = loader.get_template("datainner.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("datainner.html")
        context = {        }
        return HttpResponse(template.render( context, request ))