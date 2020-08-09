from django.urls import path, re_path

from home.views import main, danhsachtt, chitietdanhsach, tintuc

app_name = 'main'
urlpatterns = [
    path('',main,name="trang-chu"),
    path('index.html',main,name="index-trangchu"),
    # tin tuc
    path('blog/',danhsachtt,name="danh-sach-tin-tuc"),
    path('blog/<str:slug>',chitietdanhsach,name="danh-muc-tin-tuc"),
    path('<str:slug>-<id>.html',tintuc,name="tin-tuc"),
]