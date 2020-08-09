from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import model_to_dict
from django.http import JsonResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from quanly.froms.danhmuc import ThemDanhmucForm, ThemTTDanhmucForm
from sanpham.models import Danhmuc, Thuoctinh


@login_required(login_url='/user/dang-nhap')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)


class ThemDanhmuc(SuccessMessageMixin, CreateView):
    model = Danhmuc
    form_class = ThemDanhmucForm
    template_name = 'quanly/page/danhmuc/them.html'
    success_url = reverse_lazy('quanly:Them-danh-muc')
    success_message = "Cập nhật thành công!"
    paginate_by = 10
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm nhà mạng'
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['danhmuc'] = Danhmuc.objects.order_by('-id')
        return data

    # Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('main:trang-chu')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)


class SuaDanhMuc(SuccessMessageMixin, UpdateView):
    model = Danhmuc
    template_name = "quanly/page/danhmuc/them.html"
    form_class= ThemDanhmucForm
    success_message = "Sửa thành công"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['danhmuc'] = Danhmuc.objects.order_by('-id')
        return data

    # permet de retourner a l'URL pointant vers le membre modifie
    def get_success_url(self):
        return reverse_lazy('quanly:Them-danh-muc',kwargs={'pk': self.get_object().id})
#
class Xoadanhmuc(SuccessMessageMixin, DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công !"
    success_url = reverse_lazy('quanly:Them-danh-muc')
    extra_context = {
        'title': 'Xoá ',
        'item': 'Xoá '
    }
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Danhmuc, id=id_)



##  Thuoc tinh danh muc
class ThemDanhmuctt(SuccessMessageMixin, CreateView):
    model = Thuoctinh
    form_class = ThemTTDanhmucForm
    template_name = 'quanly/page/tt_danhmuc/them.html'
    success_url = reverse_lazy('quanly:Them-tt-danh-muc')
    success_message = "Cập nhật thành công!"
    paginate_by = 10
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm danh mục'
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['ttdanhmuc'] = Thuoctinh.objects.order_by('-id')
        return data

    # Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('main:trang-chu')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)


class SuaDanhMuctt(SuccessMessageMixin, UpdateView):
    model = Thuoctinh
    template_name = "quanly/page/tt_danhmuc/them.html"
    form_class= ThemTTDanhmucForm
    success_message = "Sửa thành công"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['ttdanhmuc'] = Thuoctinh.objects.order_by('-id')
        return data

    # permet de retourner a l'URL pointant vers le membre modifie
    def get_success_url(self):
        return reverse_lazy('quanly:Them-danh-muc',kwargs={'pk': self.get_object().id})
#
class Xoadanhmuctt(SuccessMessageMixin, DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công !"
    success_url = reverse_lazy('quanly:Them-tt-danh-muc')
    extra_context = {
        'title': 'Xoá ',
        'item': 'Xoá '
    }
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Thuoctinh, id=id_)
