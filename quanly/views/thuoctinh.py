from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView

from quanly.froms.nguyenlieu import Nguyenlieufr, Loxofr, Xulybematfr, Xulytaycamfr, Xulynhietfr
from quanly.froms.thuonghieu import ThemThuonghieuForm
from sanpham.models import Danhmuc, Thuonghieu, nguyenlieu, loxo, xulybemat, xulytaycam, xulynhiet


@login_required(login_url='/admin')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)


class Themnguyenlieu(SuccessMessageMixin, CreateView):
    model = nguyenlieu
    form_class = Nguyenlieufr
    template_name = 'quanly/page/thongsosp/nguyenlieu/them.html'
    success_url = reverse_lazy('quanly:Them-nguyenlieu')
    success_message = "Cập nhật thành công!"
    paginate_by = 10
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm nguyên liệu '
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['nguyenlieu'] = nguyenlieu.objects.order_by('-id')
        return data

    # Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('main:trang-chu')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)


class Suanguyenlieu(SuccessMessageMixin, UpdateView):
    model = nguyenlieu
    template_name = "quanly/page/thongsosp/nguyenlieu/them.html"
    form_class= Nguyenlieufr
    success_message = "Sửa thành công"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['nguyenlieu'] = nguyenlieu.objects.order_by('-id')
        return data

    # permet de retourner a l'URL pointant vers le membre modifie
    def get_success_url(self):
        return reverse_lazy('quanly:Them-nguyenlieu',kwargs={'pk': self.get_object().id})

class Xoanguyenlieu(SuccessMessageMixin, DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công !"
    success_url = reverse_lazy('quanly:Them-nguyenlieu')
    extra_context = {
        'title': 'Xoá ',
        'item': 'Xoá '
    }
    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(nguyenlieu, id=id_)

# #############################
class Themloxo(SuccessMessageMixin, CreateView):
    model = loxo
    form_class = Loxofr
    template_name = 'quanly/page/thongsosp/loxo/them.html'
    success_url = reverse_lazy('quanly:Them-loxo')
    success_message = "Cập nhật thành công!"
    paginate_by = 10
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm lò xo'
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['loxo'] = loxo.objects.order_by('-id')
        return data

    # Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('main:trang-chu')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)


class Sualoxo(SuccessMessageMixin, UpdateView):
    model = loxo
    template_name = "quanly/page/thongsosp/loxo/them.html"
    form_class= Loxofr
    success_message = "Sửa thành công"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['loxo'] = loxo.objects.order_by('-id')
        return data

    # permet de retourner a l'URL pointant vers le membre modifie
    def get_success_url(self):
        return reverse_lazy('quanly:Them-loxo',kwargs={'pk': self.get_object().id})
#
class Xoaloxo(SuccessMessageMixin, DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công !"
    success_url = reverse_lazy('quanly:Them-loxo')
    extra_context = {
        'title': 'Xoá ',
        'item': 'Xoá '
    }
    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(loxo, id=id_)
#
# #############################

class Themxulybemat(SuccessMessageMixin, CreateView):
    model = xulybemat
    form_class = Xulybematfr
    template_name = 'quanly/page/thongsosp/xulybemat/them.html'
    success_url = reverse_lazy('quanly:Them-xulybemat')
    success_message = "Cập nhật thành công!"
    paginate_by = 10
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm '
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['xulybemat'] = xulybemat.objects.order_by('-id')
        return data

    # Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('main:trang-chu')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)


class Suaxulybemat(SuccessMessageMixin, UpdateView):
    model = xulybemat
    template_name = "quanly/page/thongsosp/xulybemat/them.html"
    form_class= Xulybematfr
    success_message = "Sửa thành công"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['xulybemat'] = xulybemat.objects.order_by('-id')
        return data

    # permet de retourner a l'URL pointant vers le membre modifie
    def get_success_url(self):
        return reverse_lazy('quanly:Them-xulybemat',kwargs={'pk': self.get_object().id})
#
class Xoaxulybemat(SuccessMessageMixin, DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công !"
    success_url = reverse_lazy('quanly:Them-xulybemat')
    extra_context = {
        'title': 'Xoá ',
        'item': 'Xoá '
    }
    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(xulybemat, id=id_)

# #############################
class Themxulytaycam(SuccessMessageMixin, CreateView):
    model = xulytaycam
    form_class = Xulytaycamfr
    template_name = 'quanly/page/thongsosp/xulytaycam/them.html'
    success_url = reverse_lazy('quanly:Them-xulytaycam')
    success_message = "Cập nhật thành công!"
    paginate_by = 10
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm'
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['xulytaycam'] = Thuonghieu.objects.order_by('-id')
        return data

    # Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('main:trang-chu')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)


class Suaxulytaycam(SuccessMessageMixin, UpdateView):
    model = xulytaycam
    template_name = "quanly/page/thongsosp/xulytaycam/them.html"
    form_class= Xulytaycamfr
    success_message = "Sửa thành công"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['xulytaycam'] = xulytaycam.objects.order_by('-id')
        return data

    # permet de retourner a l'URL pointant vers le membre modifie
    def get_success_url(self):
        return reverse_lazy('quanly:Them-xulytaycam',kwargs={'pk': self.get_object().id})
#
class Xoaxulytaycam(SuccessMessageMixin, DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công !"
    success_url = reverse_lazy('quanly:Them-xulytaycam')
    extra_context = {
        'title': 'Xoá ',
        'item': 'Xoá '
    }
    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(xulytaycam, id=id_)

# #############################
class Themxulynhiet(SuccessMessageMixin, CreateView):
    model = xulynhiet
    form_class = Xulynhietfr
    template_name = 'quanly/page/thongsosp/xulynhiet/them.html'
    success_url = reverse_lazy('quanly:Them-xulynhiet')
    success_message = "Cập nhật thành công!"
    paginate_by = 10
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm '
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['xulynhiet'] = xulynhiet.objects.order_by('-id')
        return data

    # Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('main:trang-chu')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)


class Suaxulynhiet(SuccessMessageMixin, UpdateView):
    model = Xulynhietfr
    template_name = "quanly/page/thongsosp/xulynhiet/them.html"
    form_class= ThemThuonghieuForm
    success_message = "Sửa thành công"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['xulynhiet'] = xulynhiet.objects.order_by('-id')
        return data

    # permet de retourner a l'URL pointant vers le membre modifie
    def get_success_url(self):
        return reverse_lazy('quanly:Them-xulynhiet',kwargs={'pk': self.get_object().id})
#
class Xoaxulynhiet(SuccessMessageMixin, DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công !"
    success_url = reverse_lazy('quanly:Them-xulynhiet')
    extra_context = {
        'title': 'Xoá ',
        'item': 'Xoá '
    }
    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(xulynhiet, id=id_)
