from django import forms
from sanpham.models import Danhmuc , Thuonghieu


class ThemThuonghieuForm(forms.ModelForm):
    class Meta:
        model = Thuonghieu
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

            'hienthi': forms.CheckboxInput(attrs={
                'class': 'input input--switch border',
                'required': False
            }),
        }
