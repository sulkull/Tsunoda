from gettext import gettext
from django import forms

from home.models import DanhMucTinTuc, Tintuc


class ThemTinTucForm(forms.ModelForm):
    class Meta:
        model = Tintuc
        fields = '__all__'
        exclude = ['slug','luotxem','ngaytao']
        widgets = {
            'danhmuc': forms.SelectMultiple(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Chọn loại tin tức',
                'required': False
            }),
            'ten': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tiêu đề',
                'required': False
            }),

            'mota': forms.Textarea(attrs={
                'class': 'summernote',
                'placeholder': 'Nhập nội dung',
                'required': False
            }),

        }


class ThemLoaiTinTucForm(forms.ModelForm):
    class Meta:
        model = DanhMucTinTuc
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tiêu đề',
                'required': False
            }),
        }

