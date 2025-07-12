from django import forms
from .models import product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'
        widgets = {
            'img': forms.ClearableFileInput(attrs={'class': 'image-upload-input'}),
            'im1': forms.ClearableFileInput(attrs={'class': 'image-upload-input'}),
            'im2': forms.ClearableFileInput(attrs={'class': 'image-upload-input'}),
            'im3': forms.ClearableFileInput(attrs={'class': 'image-upload-input'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['img', 'img1', 'img2', 'img3']:
            self.fields[field_name].widget.attrs.update({'style': 'display: visible;'})  # Hide input field
