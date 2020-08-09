from django.contrib import admin

# Register your models here.
from home.models import *


class slide(admin.ModelAdmin):
    list_display = ['title', 'id']
    list_filter = ['title']
    # exclude = ['slug']
    list_per_page = 10
admin.site.register(Slider, slide)

class danhmuc(admin.ModelAdmin):
    list_display = ['ten', 'id']
    list_filter = ['ten']
    exclude = ['slug']
    list_per_page = 10
admin.site.register(DanhMucTinTuc, danhmuc)

class tintuc(admin.ModelAdmin):
    list_display = ['ten', 'id']
    list_filter = ['ten','danhmuc']
    exclude = ['slug']
    list_per_page = 10
admin.site.register(Tintuc, tintuc)