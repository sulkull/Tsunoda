# Generated by Django 3.0.8 on 2020-07-28 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Danhmuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=100, unique=True, verbose_name='Tên danh mục')),
                ('slug', models.SlugField(max_length=255)),
                ('hinh', models.ImageField(upload_to='danhmuc/', verbose_name='Hình đại diện')),
                ('hienthi', models.BooleanField(default=False, verbose_name='Hiển thị ở trang chủ')),
            ],
            options={
                'verbose_name_plural': 'Danh mục',
            },
        ),
        migrations.CreateModel(
            name='loxo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=50, unique=True, verbose_name='Nhập tên loại')),
            ],
            options={
                'verbose_name_plural': 'Lò xo',
            },
        ),
        migrations.CreateModel(
            name='nguyenlieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=50, unique=True, verbose_name='Tên nguyên liệu')),
            ],
            options={
                'verbose_name_plural': 'Nguyên liệu',
            },
        ),
        migrations.CreateModel(
            name='Thuoctinh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=50, unique=True, verbose_name='Tên thuộc tính')),
                ('hinh', models.ImageField(upload_to='thuoctinh/')),
            ],
            options={
                'verbose_name_plural': 'Thuộc tính',
            },
        ),
        migrations.CreateModel(
            name='Thuoctinhdanhmuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=50, unique=True, verbose_name='Tên thuộc tính')),
            ],
            options={
                'verbose_name_plural': 'Thuộc tính danh mục',
            },
        ),
        migrations.CreateModel(
            name='Thuonghieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=100, unique=True, verbose_name='Tên thương hiệu')),
                ('slug', models.SlugField(max_length=255)),
                ('hinh', models.ImageField(upload_to='nguyenlieu/')),
                ('banner', models.ImageField(upload_to='nguyenlieu/banner/')),
                ('hienthi', models.BooleanField(default=False, verbose_name='Hiển thị ở trang chủ')),
            ],
            options={
                'verbose_name_plural': 'Thương hiệu',
            },
        ),
        migrations.CreateModel(
            name='xulybemat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=50, unique=True, verbose_name='Nhập tên loại')),
            ],
            options={
                'verbose_name_plural': 'Xử lý bề mặt',
            },
        ),
        migrations.CreateModel(
            name='xulynhiet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=50, unique=True, verbose_name='Nhập tên loại')),
            ],
            options={
                'verbose_name_plural': 'Xử lý nhiệt',
            },
        ),
        migrations.CreateModel(
            name='xulytaycam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=50, unique=True, verbose_name='Nhập tên loại')),
            ],
            options={
                'verbose_name_plural': 'Xử lý tay cầm',
            },
        ),
        migrations.CreateModel(
            name='sanpham',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=200, unique=True, verbose_name='Tên sản phẩm')),
                ('slug', models.SlugField(max_length=255)),
                ('luotxem', models.IntegerField(default=1)),
                ('motangan', models.TextField(max_length=5000, verbose_name='Mô tả ngắn')),
                ('masp', models.CharField(max_length=50, verbose_name='Mã sản phẩm')),
                ('gia', models.IntegerField(blank=True, null=True, verbose_name='Nhập giá ')),
                ('linkshoppe', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nhập link  shoppe')),
                ('linklazada', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nhập link mua lazada')),
                ('linksendo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nhập link mua sendo')),
                ('linkshop', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nhập link mua shop')),
                ('mota', models.TextField(max_length=50000, verbose_name='Mô tả')),
                ('chitietthongso', models.TextField(max_length=50000, verbose_name='Chi tiết thông số')),
                ('docungthan', models.CharField(blank=True, max_length=100, null=True, verbose_name='Độ cứng thân')),
                ('docungluoicat', models.CharField(blank=True, max_length=100, null=True, verbose_name='Độ cứng lưỡi cắt')),
                ('docung', models.CharField(blank=True, max_length=100, null=True, verbose_name='Độ cứng')),
                ('hinhthongso', models.ImageField(blank=True, null=True, upload_to='sanpham/thong-so/', verbose_name='Hình ảnh thông số')),
                ('hinhsp', models.ImageField(upload_to='sanpham/', verbose_name='Hình đại diện')),
                ('danhmucsp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanpham.Danhmuc', verbose_name='Danh mục')),
                ('loxo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sanpham.loxo', verbose_name='Lò xo')),
                ('nguyenlieusp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sanpham.nguyenlieu', verbose_name='Nguyên liệu')),
                ('thuoctinhsp', models.ManyToManyField(to='sanpham.Thuoctinh', verbose_name='Chọn thuộc tính')),
                ('thuonghieusp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanpham.Thuonghieu', verbose_name='Thương hiệu')),
                ('xulybematsp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sanpham.xulybemat', verbose_name='Xử lý bề mặt')),
                ('xulynhietsp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sanpham.xulynhiet', verbose_name='Xử lý nhiệt')),
                ('xulytaycamsp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sanpham.xulytaycam', verbose_name='Xử lý tay cầm')),
            ],
            options={
                'verbose_name_plural': 'Sản phẩm',
            },
        ),
        migrations.AddField(
            model_name='danhmuc',
            name='chitiet',
            field=models.ManyToManyField(to='sanpham.Thuoctinhdanhmuc', verbose_name='Chon'),
        ),
    ]
