from django.conf.urls.static import static
from django.urls import path, re_path

from WEBHATOK import settings
from quanly.views.cauhinh import SuaCauHinhSEO
from quanly.views.danhmuc import *
from quanly.views.main import main_ql
from quanly.views.sanpham import ThemSanPham, DanhSachSanPham, SuaSanPham, XoaSanPham
from quanly.views.thuoctinh import *
from quanly.views.thuonghieu import *
from quanly.views.tintuc import *

app_name = 'quanly'

urlpatterns = [
    path('main/', main_ql, name='main'),

    path('themsanpham/', ThemSanPham.as_view(), name='Them-san-pham'),
    path('sua-sanpham/<int:id>', SuaSanPham, name='sua-san-pham'),
    path('danhmuc-sanpham', DanhSachSanPham.as_view(), name='Danh-sach-san-pham'),
    path('xoa-sanpham/<int:id>', XoaSanPham.as_view(), name='xoa-san-pham'),

    #danh-muc
    path('danhmuc/', ThemDanhmuc.as_view(), name='Them-danh-muc'),
    path('danhmuc/<pk>', SuaDanhMuc.as_view(), name='sua-danh-muc'),
    path('xoa-danhmuc/<int:id>', Xoadanhmuc.as_view(), name='xoa-danh-muc'),

    # thuoc tính danh-muc
    path('ttdanhmuc/', ThemDanhmuctt.as_view(), name='Them-tt-danh-muc'),
    path('ttdanhmuc/<pk>', SuaDanhMuctt.as_view(), name='sua-tt-danh-muc'),
    path('xoa-ttdanhmuc/<int:id>', Xoadanhmuctt.as_view(), name='xoa-tt-danh-muc'),

    # Thương hiệu
    path('thuonghieu/', ThemThuonghieu.as_view(), name='Them-thuong-hieu'),
    path('thuonghieu/<pk>', SuaThuonghieu.as_view(), name='sua-thuong-hieu'),
    path('xoa-thuonghieu/<int:id>', XoaThuonghieu.as_view(), name='xoa-thuong-hieu'),

    # path('error', Quyen404, name='Quyen-truy-cap'),

# nguyen lieu
    path('nguyenlieu/', Themnguyenlieu.as_view(), name='Them-nguyenlieu'),
    path('nguyenlieu/<pk>', Suanguyenlieu.as_view(), name='sua-nguyenlieu'),
    path('xoa-nguyenlieu/<int:id>', Xoanguyenlieu.as_view(), name='xoa-nguyenlieu'),
# lo xo
    path('loxo/', Themloxo.as_view(), name='Them-loxo'),
    path('loxo/<pk>', Sualoxo.as_view(), name='sua-loxo'),
    path('xoa-loxo/<int:id>', Xoaloxo.as_view(), name='xoa-loxo'),

# XU LY BE MAT
    path('xulybemat/', Themxulybemat.as_view(), name='Them-xulybemat'),
    path('xulybemat/<pk>', Suaxulybemat.as_view(), name='sua-xulybemat'),
    path('xoa-xulybemat/<int:id>', Xoaxulybemat.as_view(), name='xoa-xulybemat'),

# XU LY TAY CAM
    path('xulytaycam/', Themxulytaycam.as_view(), name='Them-xulytaycam'),
    path('xulytaycam/<pk>', Suaxulytaycam.as_view(), name='sua-xulytaycam'),
    path('xoa-xulytaycam/<int:id>', Xoaxulytaycam.as_view(), name='xoa-xulytaycam'),

# XU LY NHIET
    path('xulynhiet/', Themxulynhiet.as_view(), name='Them-xulynhiet'),
    path('xulynhiet/<pk>', Suaxulynhiet.as_view(), name='sua-xulynhiet'),
    path('xoa-xulynhiet/<int:id>', Xoaxulynhiet.as_view(), name='xoa-xulynhiet'),

#cau hinh,
    path('cau-hinh',SuaCauHinhSEO,name='cau-hinh-seo'),

# Chuyen muc
    path('chuyenmuc/', ThemLoaiTinTuc.as_view(), name='Them-chuyenmuc'),
    path('chuyenmuc/<pk>', SuaLoaiTinTuc.as_view(), name='sua-chuyenmuc'),
    path('xoa-chuyenmuc/<int:id>', XoaDanhMucTinTuc.as_view(), name='xoa-chuyenmuc'),

# Tin tuc
    path('tintuc/', ThemTintuc.as_view(), name='Them-Tintuc'),
    path('tintuc/<int:id>', SuaTintuc, name='Sua-Tintuc'),
    path('danhsach-tintuc', DanhSachTintuc.as_view(), name='Danh-sach-Tintuc'),
    path('xoa-tintuc/<int:id>', XoaTintuc.as_view(), name='xoa-Tintuc'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)