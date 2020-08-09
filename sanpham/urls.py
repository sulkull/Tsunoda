from django.urls import path, re_path
from sanpham.views import *

app_name = 'sanpham'
urlpatterns = [
    path('<str:slug>.html',chitietsp,name="chi-tiet-sp"),
    path('danhmuc/',danhsachsp,name="danh-sach-sp"),
    path('danhmuc/<str:slug>.html',chitietdanhsach,name="danh-muc-sp"),

    # thuog hieu
    path('thuonghieu/', danhsach_th, name="danh-sach-th"),
    path('thuonghieu/<str:slug>.html', chitietdanhsach_th, name="danh-muc-th"),
]