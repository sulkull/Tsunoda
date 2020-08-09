from django.shortcuts import render, redirect

# Create your views here.
from sanpham.models import sanpham, Danhmuc, Thuonghieu


def chitietsp(request,slug):
    dm = Danhmuc.objects.all()
    th = Thuonghieu.objects.all()
    try:
        sp = sanpham.objects.get(slug=slug)
    except sanpham.DoesNotExist:
        return redirect('main:trang-chu')
    sp.luotxem += 1
    sp.save()

    data ={
        'sp':sp,
        'dm':dm,
        'th':th,
    }
    return render(request,'hatok/page/chitetsp.html',data)

def danhsachsp(request):
    sp = sanpham.objects.all()
    spmoi = sanpham.objects.all()[0:8]
    dm = Danhmuc.objects.all()
    th = Thuonghieu.objects.all()
    data = {
        'sp':sp,
        'spmoi':spmoi,
        'dm':dm,
        'th':th,
    }
    return render(request,'hatok/page/danhsachsp.html',data)

def chitietdanhsach(request,slug):
    sp = sanpham.objects.all()
    spmoi = sanpham.objects.all()[0:8]
    dm = Danhmuc.objects.all()
    th =Thuonghieu.objects.all()
    try:
        dmd = Danhmuc.objects.get(slug=slug)
        sp_dm = sanpham.objects.filter(danhmucsp=dmd)
    except Danhmuc.DoesNotExist:
        return redirect('main:trang-chu')
    data = {
        'dm':dm,
        'dmd':dmd,
        'th':th,
        'sp':sp,
        'sp_dm':sp_dm,
        'spmoi':spmoi,
    }
    return render(request,'hatok/page/danhmuc.html',data)


# thuong hieu
def danhsach_th(request):
    sp = sanpham.objects.all()
    spmoi = sanpham.objects.all()[0:8]
    dm = Danhmuc.objects.all()
    th = Thuonghieu.objects.all()
    data = {
        'sp':sp,
        'spmoi':spmoi,
        'th':th,
        'dm':dm,
    }
    return render(request,'hatok/page/danhsach-th.html',data)

def chitietdanhsach_th(request,slug):
    sp = sanpham.objects.all()
    spmoi = sanpham.objects.all()[0:8]
    th = Thuonghieu.objects.all()
    dm =Danhmuc.objects.all()
    try:
        tht = Thuonghieu.objects.get(slug=slug)
        sp_th = sanpham.objects.filter(thuonghieusp=tht)
    except Thuonghieu.DoesNotExist:
        return redirect('main:trang-chu')
    data = {
        'th':th,
        'tht':tht,
        'sp_th':sp_th,
        'sp':sp,
        'dm':dm,
        'spmoi':spmoi,
    }
    return render(request,'hatok/page/thuonghieu.html',data)