from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView
from quanly.froms.thuonghieu import ThemThuonghieuForm
from sanpham.models import Danhmuc, Thuonghieu


@login_required(login_url='/admin')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)


class ThemThuonghieu(SuccessMessageMixin, CreateView):
    model = Thuonghieu
    form_class = ThemThuonghieuForm
    template_name = 'quanly/page/thuonghieu/them.html'
    success_url = reverse_lazy('quanly:Them-thuong-hieu')
    success_message = "Cập nhật thành công!"
    paginate_by = 10
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm nhà mạng'
    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['nguyenlieu'] = Thuonghieu.objects.order_by('-id')
        return data

    # Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('main:trang-chu')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)


class SuaThuonghieu(SuccessMessageMixin, UpdateView):
    model = Thuonghieu
    template_name = "quanly/page/thuonghieu/them.html"
    form_class= ThemThuonghieuForm
    success_message = "Sửa thành công"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['nguyenlieu'] = Thuonghieu.objects.order_by('-id')
        return data

    # permet de retourner a l'URL pointant vers le membre modifie
    def get_success_url(self):
        return reverse_lazy('quanly:Them-thuong-hieu',kwargs={'pk': self.get_object().id})
#
class XoaThuonghieu(SuccessMessageMixin, DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công !"
    success_url = reverse_lazy('quanly:Them-thuong-hieu')
    extra_context = {
        'title': 'Xoá ',
        'item': 'Xoá '
    }
    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Thuonghieu, id=id_)
