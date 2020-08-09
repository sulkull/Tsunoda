from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Sum
from django.shortcuts import render, redirect

from home.models import Tintuc
from sanpham.models import sanpham, Thuonghieu


@login_required(login_url='/user/dang-nhap')
def main_ql(request):
   if request.user:
      sp = sanpham.objects.all()
      th = Thuonghieu.objects.all()
      tt = Tintuc.objects.all()
   else:
      return redirect('main:trang-chu')

   data = {
      'sp':sp,
      'th':th,
      'tt':tt,

   }

   return render(request ,'quanly/page/dashboards.html',data)