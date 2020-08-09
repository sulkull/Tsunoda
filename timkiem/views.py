from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from sanpham.models import sanpham, Danhmuc, Thuonghieu


def timkiem(request):
    sp = sanpham.objects.all()
    dm = Danhmuc.objects.all()
    th = Thuonghieu.objects.all()
    search = request.GET.get('q')
    if search:
        sp = sp.filter(
            Q(ten__icontains=search) | Q(mota__contains=search)| Q(masp__icontains=search)
        )
    context = {
        "sp": sp,
        "th": th,
        "dm": dm,
        "search":search,
    }
    return render(request, 'hatok/page/tim-kiem.html', context)