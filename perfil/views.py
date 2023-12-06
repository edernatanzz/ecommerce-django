from msilib.schema import ListView
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views import View

# Create your views here.

class Criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('criar')
class Uptade(View):
    def get(self, *args, **kwargs):
        return HttpResponse('update') 

class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('login')

class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('logout')