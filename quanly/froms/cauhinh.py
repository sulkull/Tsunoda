from gettext import gettext
from django import forms

from CauHinh.models import CauHinhSeo, Default_robot

class ThemCauHinhSEOForm(forms.ModelForm):
    class Meta:
        model = CauHinhSeo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập tiêu đề',
                'required': False
            }),
            'keyword': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập từ khóa',
                'required': False
            }),
            'des': forms.Textarea(attrs={
                'class': 'summernote',
                'placeholder': 'Nhập mô tả',
                'required': False
            }),
            'google': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập mã google',
                'required': False
            }),
            'fb_app': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập facebook app',
                'required': False
            }),
            'robots': forms.Select(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Nhập robots',
                'required': False
            },choices=Default_robot),

            'youtube': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Link youtube',
                'required': False
            }),
            'lienhe': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'Liên hệ',
                'required': False
            }),
            'catalog': forms.TextInput(attrs={
                'class': 'input w-full border mt-2',
                'placeholder': 'catalog',
                'required': False
            }),
        }