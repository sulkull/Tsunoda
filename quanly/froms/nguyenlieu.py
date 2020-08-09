from django import forms
from sanpham.models import nguyenlieu, loxo, xulybemat, xulynhiet, xulytaycam


class Nguyenlieufr(forms.ModelForm):
    class Meta:
        model = nguyenlieu
        fields = '__all__'
        # labels = {
        # }
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tên ',
                'required': False
            }),
        }

class Loxofr(forms.ModelForm):
    class Meta:
        model = loxo
        fields = '__all__'
        # labels = {
        # }
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tên ',
                'required': False
            }),
        }

class Xulybematfr(forms.ModelForm):
    class Meta:
        model = xulybemat
        fields = '__all__'
        # labels = {
        # }
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tên ',
                'required': False
            }),
        }

class Xulynhietfr(forms.ModelForm):
    class Meta:
        model = xulynhiet
        fields = '__all__'
        # labels = {
        # }
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tên ',
                'required': False
            }),
        }

class Xulytaycamfr(forms.ModelForm):
    class Meta:
        model = xulytaycam
        fields = '__all__'
        # labels = {
        # }
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tên ',
                'required': False
            }),
        }