from django.contrib import admin

# Register your models here.
from sanpham.models import *


class nguyenlieuad(admin.ModelAdmin):
    list_display = ['ten', 'id']
    list_filter = ['ten']
    # exclude = ['slug']
    list_per_page = 10
admin.site.register(nguyenlieu, nguyenlieuad)

class xulynhietad(admin.ModelAdmin):
    list_display = ['ten', 'id']
    list_filter = ['ten']
    # exclude = ['slug']
    list_per_page = 10
admin.site.register(xulynhiet, xulynhietad)

class xulytaycamad(admin.ModelAdmin):
    list_display = ['ten', 'id']
    list_filter = ['ten']
    # exclude = ['slug']
    list_per_page = 10
admin.site.register(xulytaycam, xulytaycamad)

class xulybematad(admin.ModelAdmin):
    list_display = ['ten', 'id']
    list_filter = ['ten']
    # exclude = ['slug']
    list_per_page = 10
admin.site.register(xulybemat, xulybematad)

class loxoad(admin.ModelAdmin):
    list_display = ['ten', 'id']
    list_filter = ['ten']
    # exclude = ['slug']
    list_per_page = 10
admin.site.register(loxo, loxoad)

class Thuoctinhad(admin.ModelAdmin):
    list_display = ['ten', 'id']
    list_filter = ['ten']
    # exclude = ['slug']
    list_per_page = 10
admin.site.register(Thuoctinh, Thuoctinhad)

# class Thuoctinhdanhmucad(admin.ModelAdmin):
#     list_display = ['ten', 'id']
#     list_filter = ['ten']
#     # exclude = ['slug']
#     list_per_page = 10
# admin.site.register(Thuoctinhdanhmuc, Thuoctinhdanhmucad)

class Thuonghieuad(admin.ModelAdmin):
    list_display = ['ten', 'id']
    list_filter = ['ten']
    # exclude = ['slug']
    list_per_page = 10
admin.site.register(Thuonghieu, Thuonghieuad)

class Danhmucad(admin.ModelAdmin):
    list_display = ['ten', 'id']
    list_filter = ['ten']
    # exclude = ['slug']
    list_per_page = 10
admin.site.register(Danhmuc, Danhmucad)


class sanphamad(admin.ModelAdmin):
    list_display = ['ten','slug', 'id']
    list_filter = ['ten']
    exclude = ['slug']
    list_per_page = 10
admin.site.register(sanpham, sanphamad)