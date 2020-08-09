from django.db import models

Default_title = 'Tsunoda Việt Nam'
Default_key = 'kìm cắt,các loại kìm,kìm điện,kìm điện đa năng,kìm nhật bản,kìm cắt sắt giá rẻ'
Default_des = 'Tsunoda việt nam chuyên cung cấp sỉ & lẻ kìm cắt , kìm bấm , kìm điện ,kìm cầm tay các loại  chất lượng ✅Chính hãng ✅Giá rẻ nhất ✅Giao hàng hoả tốc 1-2h ☎️Tư vấn sâu.'
Default_fav= '/media/logo-1.png'
Default_robot = {
    ('index,follow' , 'Lập chỉ mục trang web (index,follow)'),
    ('noindex,nofollow' , 'Chặn google lập chỉ mục trang web :(noindex,nofollow)')
}

# Create your models herec
class CauHinhSeo(models.Model):
    title = models.CharField(max_length=200,default=Default_title,verbose_name='Tiêu đề website')
    keyword = models.CharField(max_length=300,default=Default_key,verbose_name='Từ khóa website',help_text='Từ khóa được phân cách bằng dầu phẩy')
    des = models.TextField(max_length=300,default=Default_des,verbose_name='Mô tả website')
    favico = models.ImageField(null=True,default=Default_fav,verbose_name='Favico')
    google = models.CharField(max_length=100,blank='',default='Mã google site',verbose_name='Google-Webmaster')
    fb_app = models.CharField(max_length=100,blank='',default='123456767890',verbose_name='Facebook app id')
    robots = models.CharField(max_length=100,choices=Default_robot,verbose_name='Robots' ,help_text='Tùy chỉnh lập chỉ mục trang web với google',default='index,follow')

    youtube = models.CharField(max_length=100,default='https://www.youtube.com/channel/UCBNPt04r_cpQncTQ-YT7E5A/')
    logo = models.ImageField(null=True,default='https://hatoktools.com/wp-content/uploads/2020/07/logo-1.png',verbose_name='Logo')

    catalog = models.CharField(max_length=100,default='https://www.youtube.com/channel/UCBNPt04r_cpQncTQ-YT7E5A/')
    lienhe = models.CharField(max_length=100,default='https://hatoktools.com/')
    gioithieu = models.CharField(max_length=100,default='https://hatoktools.com/')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Cấu Hình SEO'




