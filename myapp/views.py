from django.shortcuts import render
# Create your views here.
from django.views import generic
from django.http import HttpResponse
from django.template import Context, loader
from myapp.models import Area, Category
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import resolve_url

def index(request):
    #areas = Area.objects.all()
    areas = Category.objects.all()
    context = {"areas": areas,}
    return render(request,'index.html',context)

class CategoryList(ListView):
    #Categoryテーブル連携
    model = Category
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "category_list"
    #テンプレートファイル連携
    template_name = "category.html"

class CreateView(CreateView):
    #操作するモデルを指示
    model = Category
    #成功した時のJUMP先を指示
    success_url = reverse_lazy("myapp:list")
    template_name = 'category_form.html'

    #フィール設定（ないとエラー）
    fields = ['is_check', 'title', 'title_num', 'foreign_number']
    # 投稿に成功した時に実行される処理
    def get_success_url(self):
        messages.success(self.request, '記事を投稿しました。')
        return resolve_url("myapp:list")
