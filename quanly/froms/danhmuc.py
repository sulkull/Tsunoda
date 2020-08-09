from django import forms
from sanpham.models import Danhmuc, Thuoctinh


class ThemDanhmucForm(forms.ModelForm):
    class Meta:
        model = Danhmuc
        fields = '__all__'
        exclude = ['slug']
        # labels = {
        # }
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tên ',
                'required': False
            }),
            'chitiet': forms.SelectMultiple(attrs={
                'class': 'select2 w-full',
                'multiple': True,
                'required': False
            }),
            # 'hinh': forms.FileInput(attrs={
            #     'class': 'input w-full border mt-2',
            #     'accept': 'image/*',
            #     'required': False
            # }),
            'hienthi': forms.CheckboxInput(attrs={
                'class': 'input input--switch border',
                'required': False
            }),
        }


class ThemTTDanhmucForm(forms.ModelForm):
    class Meta:
        model = Thuoctinh
        fields = '__all__'
        # exclude = ['slug']
        # labels = {
        # }
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tên ',
                'required': False
            }),
        }