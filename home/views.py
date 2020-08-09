from django.db.models.functions import Lower
from django.shortcuts import render, redirect

from home.models import Slider, Tintuc, DanhMucTinTuc
from sanpham.models import sanpham, Danhmuc, Thuonghieu

def main(request):
    sp = sanpham.objects.all()[0:15]
    dm = Danhmuc.objects.filter(hienthi=True)
    th = Thuonghieu.objects.filter(hienthi=True)
    banner = Slider.objects.filter(action=True).order_by(Lower('thutu').asc())
    tt = Tintuc.objects.all()[0:6]
    data ={
        'sp':sp,
        'dm':dm,
        'th':th,
        'tt':tt,
        'banner':banner,
    }
    return render(request,'hatok/index.html',data)


def tintuc(request,slug,id):
    dm = Danhmuc.objects.all()
    th = Thuonghieu.objects.all()
    dmtt = DanhMucTinTuc.objects.all()
    try:
        tt = Tintuc.objects.get(slug=slug,id=id)
    except Tintuc.DoesNotExist:
        return redirect('main:trang-chu')
    tt.luotxem += 1
    tt.save()

    data ={
        'tt':tt,
        'dm':dm,
        'dmtt':dmtt,
        'th':th,
    }
    return render(request,'hatok/page/tintuc/tintuc.html',data)

def danhsachtt(request):
    sp = sanpham.objects.all()
    spmoi = sanpham.objects.all()[0:8]
    dm = Danhmuc.objects.all()
    th = Thuonghieu.objects.all()
    #
    tt = Tintuc.objects.all()
    dmtt = DanhMucTinTuc.objects.all()
    data = {
        'sp':sp,
        'spmoi':spmoi,
        'dm':dm,
        'th':th,
        'tt':tt,
        'dmtt':dmtt,
    }
    return render(request,'hatok/page/tintuc/danhsach.html',data)

def chitietdanhsach(request,slug):
    sp = sanpham.objects.all()
    spmoi = sanpham.objects.all()[0:8]
    dm = Danhmuc.objects.all()
    th =Thuonghieu.objects.all()
    #
    tt = Tintuc.objects.all()
    dmtt = DanhMucTinTuc.objects.all()
    try:
        chitietdm = DanhMucTinTuc.objects.get(slug=slug)
        tt_dm = Tintuc.objects.filter(danhmuc=chitietdm)
    except DanhMucTinTuc.DoesNotExist:
        return redirect('main:trang-chu')
    data = {
        'dm':dm,
        'chitietdm':chitietdm,
        'th':th,
        'tt_dm':tt_dm,
        'sp':sp,
        'spmoi':spmoi,
        'tt': tt,
        'dmtt': dmtt,
    }
    return render(request,'hatok/page/tintuc/danh-muc.html',data)
