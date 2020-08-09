from django.core.exceptions import ValidationError
from django.db import models
# Create your models here.
from WEBHATOK.utils import get_unique_slug


class nguyenlieu(models.Model):
    ten = models.CharField(max_length=50,unique=True, verbose_name='Tên nguyên liệu',null=False)
    def __str__(self):
        return self.ten

    class Meta:
        verbose_name_plural = 'Nguyên liệu'

class xulynhiet(models.Model):
    ten = models.CharField(max_length=50,unique=True,  verbose_name='Nhập tên loại',null=False)
    def __str__(self):
        return self.ten

    class Meta:
        verbose_name_plural = 'Xử lý nhiệt'

class xulytaycam(models.Model):
    ten = models.CharField(max_length=50,unique=True,  verbose_name='Nhập tên loại',null=False)
    def __str__(self):
        return self.ten

    class Meta:
        verbose_name_plural = 'Xử lý tay cầm'

class xulybemat(models.Model):
    ten = models.CharField(max_length=50,unique=True,  verbose_name='Nhập tên loại',null=False)
    def __str__(self):
        return self.ten

    class Meta:
        verbose_name_plural = 'Xử lý bề mặt'

class loxo(models.Model):
    ten = models.CharField(max_length=50,unique=True,  verbose_name='Nhập tên loại',null=False)
    def __str__(self):
        return self.ten

    class Meta:
        verbose_name_plural = 'Lò xo'

## Thuộc tính sản phẩm
class Thuoctinh(models.Model):
    ten = models.CharField(max_length=50,verbose_name='Tên thuộc tính',null=False,unique=True)
    hinh = models.ImageField(upload_to='thuoctinh/',null=False)
    def __str__(self):
        return self.ten

    class Meta:
        verbose_name_plural = 'Thuộc tính'


# ## Thuộc tính danh mục
# class Thuoctinhdanhmuc(models.Model):
#     ten = models.CharField(max_length=50, verbose_name='Tên thuộc tính', null=False, unique=True)
#     def __str__(self):
#         return self.ten
#     class Meta:
#         verbose_name_plural = 'Thuộc tính danh mục'

## Thương hiệu
class Thuonghieu(models.Model):
    ten = models.CharField(max_length=100,verbose_name='Tên thương hiệu',unique=True,null=False)
    slug = models.SlugField(max_length=255)
    hinh = models.ImageField(upload_to='nguyenlieu/',null=False)
    banner = models.ImageField(upload_to='nguyenlieu/banner/',null=False)
    hienthi = models.BooleanField(default=False,verbose_name='Hiển thị ở trang chủ')

    def __str__(self):
        return self.ten

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'ten', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Thương hiệu'

## Danh mục
class Danhmuc(models.Model):
    ten = models.CharField(max_length=100,verbose_name='Tên danh mục',unique=True,null=False)
    slug = models.SlugField(max_length=255)
    chitiet = models.ManyToManyField(Thuoctinh,verbose_name='Chon')
    hinh = models.ImageField(upload_to='danhmuc/',null=False,verbose_name='Hình đại diện')
    hienthi = models.BooleanField(default=False,verbose_name='Hiển thị ở trang chủ')

    def __str__(self):
        return self.ten

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'ten', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Danh mục'

class sanpham(models.Model):
    ten = models.CharField(max_length=200,unique=True,verbose_name='Tên sản phẩm')
    slug = models.SlugField(max_length=255)
    luotxem = models.IntegerField(default=1)
    motangan = models.TextField(max_length=5000,verbose_name='Mô tả ngắn')
    masp = models.CharField(max_length=50,verbose_name='Mã sản phẩm')
    thuoctinhsp = models.ManyToManyField(Thuoctinh,verbose_name='Chọn thuộc tính')
    thuonghieusp = models.ForeignKey(Thuonghieu,on_delete=models.CASCADE,verbose_name='Thương hiệu')
    danhmucsp = models.ForeignKey(Danhmuc,on_delete=models.CASCADE,verbose_name='Danh mục')
    gia = models.IntegerField(verbose_name='Nhập giá ',null=True,blank=True)
    # link mua sản phẩm
    linkshoppe = models.CharField(max_length=255,null=True,blank=True,verbose_name='Nhập link  shoppe')
    linklazada = models.CharField(max_length=255,null=True,blank=True,verbose_name='Nhập link mua lazada')
    linksendo = models.CharField(max_length=255,null=True,blank=True,verbose_name='Nhập link mua sendo')
    linkshop = models.CharField(max_length=255,null=True,blank=True,verbose_name='Nhập link mua shop')
    # mo ta
    mota = models.TextField(verbose_name='Mô tả')
    chitietthongso = models.TextField(max_length=50000, verbose_name='Chi tiết thông số')
    # thông số sản phẩm
    nguyenlieusp = models.ForeignKey(nguyenlieu,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Nguyên liệu')
    xulynhietsp = models.ForeignKey(xulynhiet,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Xử lý nhiệt')
    xulybematsp = models.ForeignKey(xulybemat,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Xử lý bề mặt')
    xulytaycamsp = models.ForeignKey(xulytaycam,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Xử lý tay cầm')
    loxo = models.ForeignKey(loxo,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Lò xo')
    docungthan = models.CharField(max_length=100,null=True,blank=True,verbose_name='Độ cứng thân')
    docungluoicat = models.CharField(max_length=100,null=True,blank=True,verbose_name='Độ cứng lưỡi cắt')
    docung = models.CharField(max_length=100,null=True,blank=True,verbose_name='Độ cứng')
    # # Hình ảnh thông số
    hinhthongso = models.ImageField(upload_to='sanpham/thong-so/',blank=True,null=True,verbose_name='Hình ảnh thông số')
    hinhsp = models.ImageField(upload_to='sanpham/',null=False,verbose_name='Hình đại diện')

    def __str__(self):
        return self.ten

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'ten', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Sản phẩm'









