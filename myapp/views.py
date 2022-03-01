from django.shortcuts import render
# Create your views here.
from django.views import generic
from django.http import HttpResponse
from django.template import Context, loader
from myapp.models import Area, Category
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.generic import ListView,DetailView

def index(request):
    #areas = Area.objects.all()
    areas = Category.objects.all()
    context = {"areas": areas,}
    return render(request,'index.html',context)

class CategoryList(ListView):
    #Categoryテーブル連携
    model = models.Category
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "category_list"
    #テンプレートファイル連携
    template_name = "Category.html"
