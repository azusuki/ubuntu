#新規作成ファイル
from django.urls import path
from . import views


app_name = 'myapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('',views.CategoryList.as_view(), name='list'),
    ]
