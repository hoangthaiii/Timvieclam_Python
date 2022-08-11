from django import forms
from .models import Post, Post_cv

class FormPost(forms.ModelForm):
    image = forms.FileField(required=False)
    class Meta:
        model = Post
        fields = ('nameJob', 'catalogy', 'nhatuyen', 'motacv', 'phucloi', 'yeucaucv', 'salary', 'diachi', 'image')

        widgets = {
            'nameJob': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name Job'}),
            'catalogy': forms.Select(attrs={'class': 'form-control'}),
            'nhatuyen': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'elder', 'type': 'hidden' }),
            'motacv': forms.Textarea(attrs={'class': 'form-control'}),
            'phucloi': forms.Textarea(attrs={'class': 'form-control'}),
            'yeucaucv': forms.Textarea(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'diachi': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    image = forms.FileField(required=False)
    class Meta:
        model = Post
        fields = ('nameJob', 'catalogy', 'nhatuyen', 'motacv', 'phucloi', 'yeucaucv', 'salary', 'diachi', 'image')

        widgets = {
            'nameJob': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name Job'}),
            'catalogy': forms.Select(attrs={'class': 'form-control'}),
            'nhatuyen': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'elder', 'type': 'hidden' }),
            'motacv': forms.Textarea(attrs={'class': 'form-control'}),
            'phucloi': forms.Textarea(attrs={'class': 'form-control'}),
            'yeucaucv': forms.Textarea(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'diachi': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField,
        }

class CV_Form(forms.ModelForm):
    
    class Meta:
        model = Post_cv
        fields = ('post_id', 'user_id', 'name', 'email', 'cv_file')
        widgets = {
            'post_id': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'post_name','type': 'hidden'}),
            'user_id': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'elder', 'type': 'hidden' }),
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nhập họ và tên'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Địa chỉ email'}),
        }
