from django.db import models

# Create your models here.
from WEBHATOK.utils import get_unique_slug

thutu = (
        ('1', 'Đầu tiên'),
        ('2', 'Thứ 2'),
        ('3', 'Thứ 3'),
        ('4', 'Thứ 4'),
        ('5', 'Thứ 5'),
        ('6', 'Thứ 6'),
        ('7', 'Thứ 7')
)
class Slider(models.Model):
    title = models.CharField(max_length=100,null=False,unique=True)
    link = models.CharField(max_length=150,null=False,default='https://tsunoda.vn')
    hinh = models.ImageField(upload_to='slider/',verbose_name='Hình slide',null=True)
    hinh_mobile = models.ImageField(upload_to='slider-m/',verbose_name='Hình slide moblie',null=True)
    thutu = models.CharField(choices=thutu,unique=True,verbose_name='Chọn thứ tự hiện thị',max_length=20,default='2')
    action = models.BooleanField(default=False, verbose_name='Hiện thị ngoài trang chủ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Banner '


class DanhMucTinTuc(models.Model):
    ten = models.CharField(max_length=500 ,null=True,unique=True, verbose_name='Tên danh mục')
    slug = models.SlugField(max_length=100, null=False, verbose_name='Đường dẫn')

    def __str__(self):
        return self.ten

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'ten', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Danh mục tin tức'

class Tintuc(models.Model):
    ten = models.CharField(max_length=200,null=False,verbose_name='Tiêu đề',unique=True)
    slug = models.SlugField(max_length=200,null=False,verbose_name='Đường dẫn',unique=True)
    danhmuc = models.ManyToManyField(DanhMucTinTuc,null=False, verbose_name='Danh mục tin tức')
    hinh = models.ImageField(upload_to='tintuc/', null=False)
    luotxem = models.IntegerField(default=1)
    mota = models.TextField(verbose_name='Mô tả',blank=True)
    ngaytao = models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')

    def __str__(self):
        return self.ten

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'ten', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Tin tức'