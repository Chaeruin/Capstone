from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class User(View):
    def get(self, request):
        template = loader.get_template("testing.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("testing.html")
        context = {        }
        return HttpResponse(template.render( context, request ))
    
class Login(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self,request):
        template = loader.get_template("login.html")
        context = {}
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        pass

class Signin(View):
    def get(self, request):
        template = loader.get_template("signin.html")
        context = {}
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        pass