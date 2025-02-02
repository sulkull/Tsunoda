# Generated by Django 3.0.8 on 2020-08-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CauHinhSeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Sim số đẹp - Thương hiệu sim số uy tín nhất việt nam', max_length=200, verbose_name='Tiêu đề website')),
                ('keyword', models.CharField(default='Mua sim ,bán sim , Sim số đẹp, sim tứ quý ,sim năm sinh', help_text='Từ khóa được phân cách bằng dầu phẩy', max_length=300, verbose_name='Từ khóa website')),
                ('des', models.TextField(default='Sim số đẹp - Thương hiệu uy tín trong ngành sim số đẹp từ hơn 10 năm qua, giao sim Miễn phí,dịch vụ tốt nhất thị trường', max_length=300, verbose_name='Mô tả website')),
                ('favico', models.ImageField(default='/favico.png', null=True, upload_to='', verbose_name='Favico')),
                ('google', models.CharField(blank='', default='Mã google site', max_length=100, verbose_name='Google-Webmaster')),
                ('fb_app', models.CharField(blank='', default='123456767890', max_length=100, verbose_name='Facebook app id')),
                ('robots', models.CharField(choices=[('noindex,nofollow', 'Chặn google lập chỉ mục trang web :(noindex,nofollow)'), ('index,follow', 'Lập chỉ mục trang web (index,follow)')], default='index,follow', help_text='Tùy chỉnh lập chỉ mục trang web với google', max_length=100, verbose_name='Robots')),
            ],
            options={
                'verbose_name_plural': 'Cấu Hình SEO',
            },
        ),
    ]
