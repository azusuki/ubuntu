from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from myapp.models import Area

def index(request):
    areas = Area.objects.all()
    context = {"areas": areas,}
    return render(request,'index.html',context)
