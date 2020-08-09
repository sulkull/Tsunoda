from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from home.models import DanhMucTinTuc, Tintuc
from quanly.froms.tintuc import ThemLoaiTinTucForm, ThemTinTucForm


@login_required(login_url='/user/dang-nhap')
def Quyen404(request):
    data = {"item": {'title': 'Lỗi truy cập'}}
    return render(request, 'quanly/page/404-user.html', data)

class ThemLoaiTinTuc(SuccessMessageMixin,CreateView):
    model = DanhMucTinTuc
    form_class = ThemLoaiTinTucForm
    template_name = 'quanly/page/tintuc/chuyenmuc/them.html'
    success_url = reverse_lazy('quanly:Them-chuyenmuc')
    success_message = "Thêm loại tin tức thành công!"
    extra_context = {
        'class_tp': 'active',
        'title': 'Thêm loại tin tức mới',
        'item': 'Thêm loại tin tức mới'

    }
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['chuyenmuc'] = DanhMucTinTuc.objects.order_by('-id')
        return data
# Kiem tra quyen truy cap
    @method_decorator(login_required(login_url=reverse_lazy('user:dangnhap')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('user:dangnhap')
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)


class SuaLoaiTinTuc(SuccessMessageMixin, UpdateView):
    model = DanhMucTinTuc
    template_name = "quanly/page/tintuc/chuyenmuc/them.html"
    form_class= ThemLoaiTinTucForm
    success_message = "Sửa thành công"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['chuyenmuc'] = DanhMucTinTuc.objects.order_by('-id')
        return data

    # permet de retourner a l'URL pointant vers le membre modifie
    def get_success_url(self):
        return reverse_lazy('quanly:Them-chuyenmuc',kwargs={'pk': self.get_object().id})
#
class XoaDanhMucTinTuc(SuccessMessageMixin, DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công !"
    success_url = reverse_lazy('quanly:Them-chuyenmuc')
    extra_context = {
        'title': 'Xoá ',
        'item': 'Xoá '
    }
    def get_object(self, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(DanhMucTinTuc, id=id_)


##### Tin tuc
class ThemTintuc(SuccessMessageMixin,CreateView):
    model = Tintuc
    form_class = ThemTinTucForm
    template_name = 'quanly/page/tintuc/them-tin-tuc.html'
    success_url = reverse_lazy('quanly:Danh-sach-Tintuc')
    success_message = "Thêm sản thành công!"
    extra_context = {
        'class_tp': 'active',
        'item': 'Thêm tin mới'
    }
# Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('main:trang-chu')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('main:trang-chu')
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)

@login_required
def SuaTintuc(request, id):
    obj = get_object_or_404(Tintuc, id=id)
    form = ThemTinTucForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid() :
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Cập nhật thông tin  thành công")
        context = {'form': form}
        return render(request, 'quanly/page/tintuc/them-tin-tuc.html', context)

    else:
        context = {'form': form,
                   'error': 'Có gì đó sai sai'}
        return render(request, 'quanly/page/tintuc/them-tin-tuc.html', context)
#


class DanhSachTintuc(ListView):
    model = Tintuc
    paginate_by = 200  # if pagination is desired
    template_name = 'quanly/page/tintuc/tin-tuc.html'
    queryset = Tintuc.objects.all()
    context_object_name = 'tintuc'
    extra_context = {
        'title': 'Danh sách sản phẩm',
        'item' : 'Danh sách sản phẩm'
    }

    # Kiem tra quyen truy cap - duc
    @method_decorator(login_required(login_url=reverse_lazy('main:trang-chu')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('main:trang-chu')
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('main:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)

class XoaTintuc(SuccessMessageMixin,DeleteView):
    template_name = 'quanly/page/xoa-post.html'
    success_message = "Xoá thành công!"
    success_url = reverse_lazy('quanly:Danh-sach-Tintuc')
    extra_context = {
        'title': 'Xoá ',
        'item': 'Xoá '
    }

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Tintuc, id=id_)