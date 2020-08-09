from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

from CauHinh.models import CauHinhSeo
from quanly.froms.cauhinh import ThemCauHinhSEOForm


@login_required(login_url='/user/dang-nhap')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)

@login_required
def SuaCauHinhSEO(request):
    obj = CauHinhSeo.objects.filter().last()
    form = ThemCauHinhSEOForm(request.POST or None, instance=obj)
    context = {'form': form,
                'title': 'Cấu hình SEO',
                'item': 'Cấu hình SEO'}

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Cập nhật thông tin thành công")
        context = {'form': form,
                    'title': 'Cấu hình SEO',
                    'item': 'Cấu hình SEO'}
        return render(request, 'quanly/page/cauhinh/cau-hinh-seo.html', context)

    else:
        context = {'form': form,
                   'error': 'Có gì đó sai sai',
                   'title': 'Cấu hình SEO',
                    'item': 'Cấu hình SEO'}
    return render(request, 'quanly/page/cauhinh/cau-hinh-seo.html', context)