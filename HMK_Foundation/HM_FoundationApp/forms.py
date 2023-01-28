from django import forms 
from .models import Add_Image

class Add_Image(forms.ModelForm): 
    class Meta: 
        model = Add_Image 
        fields = [ 'images'] 