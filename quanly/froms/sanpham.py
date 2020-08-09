from gettext import gettext
from django import forms
from sanpham.models import sanpham
class ThemSanPhamForm(forms.ModelForm):
    class Meta:
        model = sanpham
        fields = '__all__'
        exclude = ['slug','luotxem']
        # labels = {
        # }
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tên',
                'required': False
            }),

            'gia': forms.NumberInput(attrs={
                'class': 'input pr-16 w-full border col-span-4',
                'placeholder': '500000',
                'required': False
            }),
            'motangan': forms.Textarea(attrs={
                'class': 'summernote',
                'data-feature': 'all',
                'required': False
            }),
            'masp': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Mã sản phẩm',
                'required': False
            }),
            'thuoctinhsp': forms.SelectMultiple(attrs={
                'class': 'select2 w-full',
                'multiple': True,
                'required': False
            }),
            'thuonghieusp': forms.Select(attrs={
                'class': 'select2 w-full',
                'required': False
            }),
            'danhmucsp': forms.Select(attrs={
                'class': 'select2 w-full',
                'required': False
            }),
            'linkshoppe': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'type':'url',
                'placeholder': 'https://shopee.vn/phamminhduc996',
                'required': False
            }),
            'linksendo': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'type': 'url',
                'placeholder': 'https://shopee.vn/phamminhduc996',
                'required': False
            }),
            'linklazada': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'type': 'url',
                'placeholder': 'https://shopee.vn/phamminhduc996',
                'required': False
            }),
            'linkshop': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'https://tooljapan.net',
                'required': False
            }),

            'mota': forms.Textarea(attrs={
                'class': 'summernote',
                'data-feature': 'all',
                'required': False
            }),
            'chitietthongso': forms.Textarea(attrs={
                'class': 'summernote',
                'data-feature': 'all',
                'required': False
            }),

            'nguyenlieusp': forms.Select(attrs={
                'class': 'select2 w-full',
                'required': False
            }),
            'xulynhietsp': forms.Select(attrs={
                'class': 'select2 w-full',
                'required': False
            }),
            'xulybematsp': forms.Select(attrs={
                'class': 'select2 w-full',
                'required': False
            }),
            'xulytaycamsp': forms.Select(attrs={
                'class': 'select2 w-full',
                'required': False
            }),
            'loxo': forms.Select(attrs={
                'class': 'select2 w-full',
                'required': False
            }),

            'docungthan': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'https://tooljapan.net',
                'required': False
            }),

            'docungluoicat': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': '45-50',
                'required': False
            }),

            'docung': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': '85',
                'required': False
            }),

            # 'hinhthongso': forms.FileInput(attrs={
            #     'class': 'input w-full border mt-2',
            #     'accept': 'image/*',
            #     'required': False
            # }),
            # 'hinhsp': forms.FileInput(attrs={
            #     'class': 'input w-full border mt-2',
            #     'accept': 'image/*',
            #     'required': True
            # }),

        }