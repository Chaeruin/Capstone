from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse, JsonResponse


class User(View):
    def get(self, request):
        template = loader.get_template("testing.html")
        context = {        }
        return HttpResponse(template.render( context, request ))

    def post(self, request):
        template = loader.get_template("testing.html")
        context = {        }
        return HttpResponse(template.render( context, request ))