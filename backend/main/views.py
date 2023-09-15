from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import request
from django.core.exceptions import ObjectDoesNotExist
from main.models import Member, Result, ImageUpload
from django.http import JsonResponse


import os
import subprocess



from jobs import jobs

class Main(View):   #main
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template("base.html")
        memid = request.session.get('memid')
        name = request.session.get('name')
        images = ImageUpload.objects.raw(
                '''
                select * from main_imageupload order by no desc limit 1
                '''
           )
        if memid :
            
            context ={
                'memid' :memid,
                'name' : name,
                'images':images,
                }
        else:
            context={
                'images' : images,
                }
        return HttpResponse(template.render( context, request ))
   
    def post(self, request):
        temperature = jobs.get_temperature()
        humidity = jobs.get_humidity()
        data = {
            'temperature': temperature,
            'humidity': humidity,
        }
        return JsonResponse(data)
    
class Login(View):  #로그인
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template("login.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        id = request.POST["id"]
        pw = request.POST["pw"]
        message = ""
        try :
            dto = Member.objects.get( id=id )
            if pw == dto.pw:
                request.session["memid"] = id
                request.session["name"] = dto.name
                return redirect('/main/main')
            else :
                message = "입력하신 비밀번호가 다릅니다"
        except ObjectDoesNotExist :
            message = "입력하신 아이디가 없습니다"  
        template = loader.get_template( "login.html" )    
        context = {
            "message" : message,
            }
        return HttpResponse( template.render( context, request ) )

class Signup(View): #회원가입
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template("signup.html")
        context = {        }
        return HttpResponse(template.render( context, request ))
    
    def post(self, request):
        dto = Member(
            name=request.POST['name'],
            id=request.POST['id'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            pw=request.POST['pw'],
        )
        dto.save()                          #회원관리 DB 저장
       
        return redirect('/main/login')      #회원가입 후 로그인 페이지로 이동
    
class LogoutView( View ) :
    def get( self, request ) :
        del( request.session["memid"] )
        return redirect( "/main/main" )

import logging
logger = logging.getLogger(__name__)

class Scandata(View):
    def get(self, request):
        template = loader.get_template("scandata.html")
        memid = request.session.get('memid')
        name = request.session.get('name')

        py_file_path_datatran = os.path.join(os.getcwd(), 'main/datatrans.py')

        # datarans.py 실행
        subprocess.run(["python", py_file_path_datatran])

        if memid :
            results = Result.objects.raw(
                '''
                select * from main_result order by no desc limit 1
                '''
            )
            time = Result.objects.filter(no__isnull=False).raw(
                '''
                SELECT DATE_FORMAT(date_time, '%%Y년 %%m월 %%d일 %%H시 %%i분') AS formatted_date, no FROM main_result order by no desc limit 1
                '''
            )
            
            images = ImageUpload.objects.order_by('-no')[:1]  # 최신 이미지 1개 가져오기
            names = Member.objects.order_by('-no')[:1]  # 최신 멤버 1명 가져오기
            context = { 
                'memid' :memid,
                'name' : name,
                'names' : names,
                'images' : images,
                'results': results,
                'time': time,
                }
        else:
            context={ }
        return HttpResponse(template.render( context, request ))

class ImageUploadView(View):
    def get(self, request):
        template = loader.get_template("imageupload.html")
        context = {}
        return HttpResponse(template.render(context, request))
    def post(self,request):
       if request.method == 'POST' and 'result_img' in request.FILES:
            image = request.FILES['result_img']
            dto = ImageUpload(image=image)
            dto.save()
            return redirect('/main/scandata')


class Totaldata(View):
    def get(self, request):
        template = loader.get_template("totaldata.html")
        memid = request.session.get('memid')
        name = request.session.get('name')
        if memid :
            context ={
                'memid' :memid,
                'name' : name,
                
                }
        else:
            context={
                }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("totaldata.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

class Averagedata(View):
    def get(self, request):
        template = loader.get_template("averagedata.html")
        memid = request.session.get('memid')
        name = request.session.get('name')
        if memid :
            context ={
                'memid' :memid,
                'name' : name,
                
                }
        else:
            context={
                }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("averagedata.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

class Perioddata(View):
    def get(self, request):
        template = loader.get_template("perioddata.html")
        memid = request.session.get('memid')
        name = request.session.get('name')
        if memid :
            context ={
                'memid' :memid,
                'name' : name,
                
                }
        else:
            context={
                }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("perioddata.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

class Alarm(View):
    def get(self, request):
        template = loader.get_template("alarm.html")
        memid = request.session.get('memid')
        name = request.session.get('name')
        if memid :
            context ={
                'memid' :memid,
                'name' : name,
                
                }
        else:
            context={
                }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("alarm.html")
        context = {        }
        return HttpResponse(template.render( context, request ))
    
class IdChkView(View):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template("idchk.html")
        context = {}
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        template = loader.get_template("signup.html")
        id = request.POST["id"]
        dto = Member.objects.get(id=id)
        result = 0
        try:
            # 아이디가 있을때
            Member.objects.get(id=id)
            result = 1
        except ObjectDoesNotExist:
            # 아이디가 없을때
            result = 0
        context = {
            "id" : id,
            "result" : result,
            }
        return HttpResponse(template.render(context, request))
